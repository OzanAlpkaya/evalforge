import pytest
from pydantic import ValidationError

from evalforge.core.config import Settings


def test_settings_use_default_values(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("EVALFORGE_APP_NAME", raising=False)
    monkeypatch.delenv("EVALFORGE_ENVIRONMENT", raising=False)
    monkeypatch.delenv("EVALFORGE_DEBUG", raising=False)

    settings = Settings()

    assert settings.app_name == "EvalForge"
    assert settings.environment == "local"
    assert settings.debug is False


def test_settings_read_environment_variables(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("EVALFORGE_APP_NAME", "EvalForge Test")
    monkeypatch.setenv("EVALFORGE_ENVIRONMENT", "test")
    monkeypatch.setenv("EVALFORGE_DEBUG", "true")

    settings = Settings()

    assert settings.app_name == "EvalForge Test"
    assert settings.environment == "test"
    assert settings.debug is True


def test_settings_reject_invalid_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("EVALFORGE_ENVIRONMENT", "staging")

    with pytest.raises(ValidationError):
        Settings()
        