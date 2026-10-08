"""API de eventos usada em todas as etapas do projeto."""

from datetime import date

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class EventInput(BaseModel):
    """Dados enviados pelo cliente ao cadastrar um evento."""

    title: str = Field(min_length=1)
    date: date
    capacity: int = Field(gt=0)


def create_app() -> FastAPI:
    """Cria uma API com dados isolados para cada execução ou teste."""
    app = FastAPI(title="Eventos do Trilha")
    events: dict[int, dict] = {}

    @app.get("/events")
    def list_events():
        return list(events.values())

    @app.get("/events/{event_id}")
    def get_event(event_id: int):
        event = events.get(event_id)
        if event is None:
            raise HTTPException(status_code=404, detail="Evento não encontrado")
        return event

    @app.post("/events", status_code=201)
    def create_event(data: EventInput):
        event_id = max(events.keys(), default=0) + 1
        event = {"id": event_id, **data.model_dump()}
        events[event_id] = event
        return event

    return app


app = create_app()
