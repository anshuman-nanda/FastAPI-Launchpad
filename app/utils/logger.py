"""
Logging utility using Loguru.
Provides structured logging with rotation and retention.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import TYPE_CHECKING

from loguru import logger

if TYPE_CHECKING:
    from loguru import Logger

from app.config import settings


def setup_logging() -> None:
    """
    Configure logging with Loguru.
    Sets up file rotation, retention, and formatting.
    """
    # Remove default handler
    logger.remove()

    # Add console handler
    logger.add(
        sys.stdout,
        format=settings.logging.log_format,
        level=settings.logging.log_level,
        colorize=True,
        backtrace=True,
        diagnose=True,
    )

    # Create logs directory
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Add file handler with rotation
    logger.add(
        log_dir / "app.log",
        format=settings.logging.log_format,
        level=settings.logging.log_level,
        rotation=settings.logging.log_rotation,
        retention=settings.logging.log_retention,
        compression=settings.logging.log_compression,
        backtrace=True,
        diagnose=True,
        enqueue=True,  # Thread-safe logging
    )

    # Add error file handler
    logger.add(
        log_dir / "error.log",
        format=settings.logging.log_format,
        level="ERROR",
        rotation=settings.logging.log_rotation,
        retention=settings.logging.log_retention,
        compression=settings.logging.log_compression,
        backtrace=True,
        diagnose=True,
        enqueue=True,
    )

    logger.info("Logging configured successfully")


def get_logger() -> Logger:
    """Get logger instance."""
    return logger

