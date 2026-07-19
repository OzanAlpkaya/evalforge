from fastapi.testclient import TestClient

from evalforge.core.config import Settings
from evalforge.main import create_app


def test_liveness_endpoint_returns_ok() -> None:
    application = create_app(
        Settings(environment="test"),
    )

    with TestClient(application) as client:
        response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
