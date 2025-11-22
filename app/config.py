"""
Configuration management using Pydantic Settings.
Follows the Single Responsibility Principle by separating configuration concerns.
"""

from functools import lru_cache

from pydantic import (
    BaseModel,
    Field,
    PostgresDsn,
    RedisDsn,
)
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseModel):
    """Application settings."""

    app_name: str = Field(default="FastAPI Production Template", description="Application name")
    app_version: str = Field(default="0.1.0", description="Application version")
    app_description: str = Field(
        default="Production-ready FastAPI template with best practices",
        description="Application description",
    )
    environment: str = Field(
        default="development", description="Environment (development/staging/production)"
    )
    debug: bool = Field(default=True, description="Debug mode")
    api_v1_prefix: str = Field(default="/api/v1", description="API v1 prefix")


class ServerSettings(BaseModel):
    """Server settings."""

    host: str = Field(default="0.0.0.0", description="Server host")
    port: int = Field(default=8000, description="Server port")
    workers: int = Field(default=4, description="Number of worker processes")
    reload: bool = Field(default=True, description="Auto-reload on code changes")


class DatabaseSettings(BaseModel):
    """Database settings."""

    database_url: PostgresDsn = Field(
        default="postgresql://postgres:postgres@localhost:5432/fastapi_db",
        description="Database URL",
    )
    database_pool_size: int = Field(default=20, description="Database connection pool size")
    database_max_overflow: int = Field(default=0, description="Database max overflow connections")
    database_echo: bool = Field(default=False, description="Echo SQL queries")


class RedisSettings(BaseModel):
    """Redis settings."""

    redis_url: RedisDsn = Field(default="redis://localhost:6379/0", description="Redis URL")
    redis_cache_ttl: int = Field(default=3600, description="Redis cache TTL in seconds")


class SecuritySettings(BaseModel):
    """Security settings."""

    secret_key: str = Field(
        default="your-secret-key-here-change-in-production", description="Secret key for JWT"
    )
    algorithm: str = Field(default="HS256", description="JWT algorithm")
    access_token_expire_minutes: int = Field(
        default=30, description="Access token expiration in minutes"
    )
    refresh_token_expire_days: int = Field(
        default=7, description="Refresh token expiration in days"
    )


class CORSSettings(BaseModel):
    """CORS settings."""

    cors_origins: list[str] = Field(
        default=["http://localhost:3000", "http://localhost:8080"],
        description="Allowed CORS origins",
    )
    cors_allow_credentials: bool = Field(default=True, description="Allow credentials")
    cors_allow_methods: list[str] = Field(default=["*"], description="Allowed methods")
    cors_allow_headers: list[str] = Field(default=["*"], description="Allowed headers")
    allowed_hosts: list[str] = Field(
        default=["*.example.com", "example.com"],
        description="Allowed hosts for TrustedHostMiddleware",
    )


class LoggingSettings(BaseModel):
    """Logging settings."""

    log_level: str = Field(default="INFO", description="Log level")
    log_format: str = Field(
        default="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>",
        description="Log format",
    )
    log_rotation: str = Field(default="100 MB", description="Log rotation size")
    log_retention: str = Field(default="30 days", description="Log retention period")
    log_compression: str = Field(default="zip", description="Log compression format")


class EmailSettings(BaseModel):
    """Email settings."""

    smtp_host: str = Field(default="smtp.gmail.com", description="SMTP host")
    smtp_port: int = Field(default=587, description="SMTP port")
    smtp_user: str = Field(default="", description="SMTP user")
    smtp_password: str = Field(default="", description="SMTP password")
    emails_from_email: str = Field(default="noreply@example.com", description="From email")
    emails_from_name: str = Field(default="FastAPI Template", description="From name")


class CelerySettings(BaseModel):
    """Celery settings."""

    celery_broker_url: str = Field(
        default="redis://localhost:6379/1", description="Celery broker URL"
    )
    celery_result_backend: str = Field(
        default="redis://localhost:6379/2", description="Celery result backend"
    )


class RateLimitSettings(BaseModel):
    """Rate limiting settings."""

    rate_limit_enabled: bool = Field(default=True, description="Enable rate limiting")
    rate_limit_per_minute: int = Field(default=60, description="Rate limit per minute")


class MonitoringSettings(BaseModel):
    """Monitoring settings."""

    sentry_dsn: str = Field(default="", description="Sentry DSN")


class Settings(BaseSettings):
    """
    Main settings class that aggregates all configuration sections.
    Follows the Composite pattern to organize related settings.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        env_nested_delimiter="__",
    )

    # Aggregate all settings
    app: AppSettings = Field(default_factory=AppSettings)
    server: ServerSettings = Field(default_factory=ServerSettings)
    database: DatabaseSettings = Field(default_factory=DatabaseSettings)
    redis: RedisSettings = Field(default_factory=RedisSettings)
    security: SecuritySettings = Field(default_factory=SecuritySettings)
    cors: CORSSettings = Field(default_factory=CORSSettings)
    logging: LoggingSettings = Field(default_factory=LoggingSettings)
    email: EmailSettings = Field(default_factory=EmailSettings)
    celery: CelerySettings = Field(default_factory=CelerySettings)
    rate_limit: RateLimitSettings = Field(default_factory=RateLimitSettings)
    monitoring: MonitoringSettings = Field(default_factory=MonitoringSettings)


@lru_cache
def get_settings() -> Settings:
    """
    Get cached settings instance.
    Uses LRU cache to ensure Singleton pattern - only one instance exists.
    """
    return Settings()


# Export settings instance
settings = get_settings()
