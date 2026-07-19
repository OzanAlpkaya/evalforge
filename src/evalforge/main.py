"""FastAPI application entry point."""

from fastapi import FastAPI

from evalforge.api.routes.health import router as health_router
from evalforge.core.config import Settings, get_settings


def create_app(settings: Settings | None = None) -> FastAPI:
    resolved_settings = settings if settings is not None else get_settings()

    application = FastAPI(
        title=resolved_settings.app_name,
        version="0.1.0",
        debug=resolved_settings.debug,
    )

    application.include_router(health_router)

    return application