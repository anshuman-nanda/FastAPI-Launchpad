"""
Common response schemas
"""

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """
    Health check response
    """
    status: str = Field(description = "Service health status")
    environment: str = Field(description = "Current environment")


class AppInfoResponse(BaseModel):
    """
    Application information response
    """
    name: str = Field(description = "Application name")
    version: str = Field(description = "Application version")
    description: str = Field(description = "Application description")
    status: str = Field(description = "Service status")
