"""Health check routes."""

from fastapi import APIRouter

from evalforge.api.schemas.health import HealthResponse


router = APIRouter(prefix="/health", tags=["health"])


@router.get("/live", response_model=HealthResponse)
async def get_liveness() -> HealthResponse:
    return HealthResponse()