"""Rota de inscrição a completar na atividade 3."""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db_session import get_session
from app.models import Event, Registration, User


router = APIRouter()


class RegistrationInput(BaseModel):
    user_id: int


@router.post("/events/{event_id}/registrations", status_code=201)
def register(event_id: int, data: RegistrationInput, session: Session = Depends(get_session)):
    event = session.get(Event, event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado")

    user = session.get(User, data.user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    existing = session.scalar(
        select(Registration).where(
            Registration.event_id == event_id,
            Registration.user_id == data.user_id,
        )
    )
    if existing is not None:
        raise HTTPException(status_code=409, detail="Usuário já inscrito neste evento")

    current_count = (
        session.scalar(
            select(func.count())
            .select_from(Registration)
            .where(Registration.event_id == event_id)
        )
        or 0
    )
    if current_count >= event.capacity:
        raise HTTPException(status_code=409, detail="Evento sem vagas disponíveis")

    registration = Registration(event_id=event_id, user_id=data.user_id)
    session.add(registration)
    session.commit()

    return {"event_id": event_id, "user_id": data.user_id}
