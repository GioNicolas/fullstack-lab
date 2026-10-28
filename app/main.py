"""API de eventos usada em todas as etapas do projeto."""

from datetime import date

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.database import Base, make_engine
from app.db_session import get_session
from app.models import Event, Registration
from app.registrations import router as registrations_router


class EventInput(BaseModel):
    """Dados enviados pelo cliente ao cadastrar um evento."""

    title: str = Field(min_length=1)
    date: date
    capacity: int = Field(gt=0)


def serialize_event(event: Event, session: Session) -> dict:
    registrations_count = (
        session.scalar(
            select(func.count())
            .select_from(Registration)
            .where(Registration.event_id == event.id)
        )
        or 0
    )
    return {
        "id": event.id,
        "title": event.title,
        "date": event.date.isoformat() if isinstance(event.date, date) else str(event.date),
        "capacity": event.capacity,
        "available_slots": event.capacity - registrations_count,
    }


def create_app(database_url: str | None = None) -> FastAPI:
    """Cria uma API com dados isolados para cada execução ou teste."""
    app = FastAPI(title="Eventos do Trilha")

    engine = make_engine(database_url or "sqlite://")
    Base.metadata.create_all(engine)
    app.state.engine = engine

    app.include_router(registrations_router)

    @app.get("/events")
    def list_events(session: Session = Depends(get_session)):
        events = session.scalars(select(Event).order_by(Event.id)).all()
        return [serialize_event(event, session) for event in events]

    @app.get("/events/{event_id}")
    def get_event(event_id: int, session: Session = Depends(get_session)):
        event = session.get(Event, event_id)
        if event is None:
            raise HTTPException(status_code=404, detail="Evento não encontrado")
        return serialize_event(event, session)

    @app.post("/events", status_code=201)
    def create_event(data: EventInput, session: Session = Depends(get_session)):
        event = Event(
            title=data.title,
            date=data.date,
            capacity=data.capacity,
        )
        session.add(event)
        session.commit()
        session.refresh(event)
        return serialize_event(event, session)

    return app


app = create_app("sqlite:///events.db")
