"""
FastAPI application entry point.
"""

import uvicorn

from app.config import settings
from app.factory import create_application

app = create_application()

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=settings.server.reload,
        log_level=settings.logging.log_level.lower(),
    )
