"""
FastAPI application entry point.
Follows the Factory pattern for application creation.
"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse

from app.config import settings
from app.database import close_db, init_db
from app.utils.logger import get_logger, setup_logging

# Setup logging
setup_logging()
logger = get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Application lifespan manager.
    Handles startup and shutdown events.
    """
    # Startup
    logger.info("Starting application...")
    logger.info(f"Environment: {settings.app.environment}")
    logger.info(f"Debug mode: {settings.app.debug}")

    # Initialize database
    if settings.app.environment == "development":
        await init_db()
        logger.info("Database initialized")

    logger.info("Application started successfully")

    yield

    # Shutdown
    logger.info("Shutting down application...")
    await close_db()
    logger.info("Database connections closed")
    logger.info("Application shutdown complete")


def create_application() -> FastAPI:
    """
    Create and configure FastAPI application.
    Factory pattern for application creation.

    Returns:
        Configured FastAPI application
    """
    app = FastAPI(
        title=settings.app.app_name,
        description=settings.app.app_description,
        version=settings.app.app_version,
        debug=settings.app.debug,
        lifespan=lifespan,
        docs_url="/docs" if settings.app.debug else None,
        redoc_url="/redoc" if settings.app.debug else None,
    )

    # Add middlewares
    configure_middlewares(app)

    # Add routes
    configure_routes(app)

    # Add exception handlers
    configure_exception_handlers(app)

    return app


def configure_middlewares(app: FastAPI) -> None:
    """
    Configure application middlewares.
    Follows the Chain of Responsibility pattern.
    """
    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors.cors_origins,
        allow_credentials=settings.cors.cors_allow_credentials,
        allow_methods=settings.cors.cors_allow_methods,
        allow_headers=settings.cors.cors_allow_headers,
    )

    # GZip compression middleware
    app.add_middleware(GZipMiddleware, minimum_size=1000)

    # Trusted host middleware (only in production)
    if settings.app.environment == "production":
        app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=["*.example.com", "example.com"],
        )

    logger.info("Middlewares configured")


def configure_routes(app: FastAPI) -> None:
    """Configure application routes."""
    # TODO: Add API routers here
    # from app.api.v1 import api_router
    # app.include_router(api_router, prefix=settings.app.api_v1_prefix)

    @app.get("/", tags=["Root"])
    async def root() -> dict:
        """Root endpoint."""
        return {
            "name": settings.app.app_name,
            "version": settings.app.app_version,
            "description": settings.app.app_description,
            "status": "healthy",
        }

    @app.get("/health", tags=["Health"])
    async def health() -> dict:
        """Health check endpoint."""
        return {
            "status": "healthy",
            "environment": settings.app.environment,
        }

    logger.info("Routes configured")


def configure_exception_handlers(app: FastAPI) -> None:
    """Configure custom exception handlers."""

    @app.exception_handler(Exception)
    async def global_exception_handler(request, exc: Exception) -> JSONResponse:
        """Global exception handler."""
        logger.error(f"Unhandled exception: {exc}")
        return JSONResponse(
            status_code=500,
            content={
                "detail": "Internal server error",
                "message": str(exc) if settings.app.debug else "An error occurred",
            },
        )

    logger.info("Exception handlers configured")


# Create application instance
app = create_application()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=settings.server.reload,
        log_level=settings.logging.log_level.lower(),
    )
