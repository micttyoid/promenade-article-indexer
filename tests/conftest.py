import pytest

pytest_plugins = ["tests.fixtures.debugs"]


# Core fixtures that must be available immediately
@pytest.fixture(autouse=True)
def setup_test_environment(monkeypatch):
    monkeypatch.setenv("TESTING", "True")
