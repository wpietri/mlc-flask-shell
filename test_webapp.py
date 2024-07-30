import pytest

from webapp.main import app


@pytest.fixture
def client():
    app.config.update({
        "TESTING": True,
    })
    return app.test_client()


def test_home(client):
    response = client.get("/")
    assert "extremely" in response.text


class TestResearcherApp:
    def test_hello_world(self, client):
        response = client.get("/researcher-app")
        assert "Hello world" in response.text

    def test_name(self, client):
        name = "George"
        response = client.get("/researcher-app?name=" + name)
        assert name in response.text
