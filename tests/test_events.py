from fastapi.testclient import TestClient

from app.main import create_app


def client():
    return TestClient(create_app())


def test_lists_events_and_missing_detail():
    with client() as api:
        assert api.get("/events").json() == []
        assert api.get("/events/999").status_code == 404


def test_creates_event_and_finds_it():
    with client() as api:
        response = api.post(
            "/events",
            json={"title": "Semana de Tecnologia", "date": "2026-10-10", "capacity": 2},
        )
        assert response.status_code == 201
        event = response.json()
        assert event["id"] > 0
        assert event["title"] == "Semana de Tecnologia"
        assert event["date"] == "2026-10-10"
        assert event["capacity"] == 2
        assert api.get(f"/events/{event['id']}").json()["title"] == event["title"]
        assert any(item["id"] == event["id"] for item in api.get("/events").json())


def test_assigns_different_ids():
    with client() as api:
        body = {"title": "Evento", "date": "2026-10-10", "capacity": 2}
        first = api.post("/events", json=body).json()
        second = api.post("/events", json=body).json()
        assert first["id"] != second["id"]


def test_rejects_invalid_event_without_storing_it():
    with client() as api:
        for body in (
            {"title": "", "date": "2026-10-10", "capacity": 2},
            {"title": "Evento", "date": "amanhã", "capacity": 2},
            {"title": "Evento", "date": "2026-10-10", "capacity": 0},
            {"title": "Evento", "date": "2026-10-10", "capacity": -1},
        ):
            assert api.post("/events", json=body).status_code == 422
        assert api.get("/events").json() == []
