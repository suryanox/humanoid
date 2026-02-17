from datetime import datetime

from pydantic import BaseModel, Field


class InitiateInteractionResponse(BaseModel):
    session_id: str


class Persona(BaseModel):
    name: str
    role: str
    tone: str


class InitiateInteractionRequest(BaseModel):
    persona: Persona
    context: str


class InteractionResponse(BaseModel):
    reply: str


class InteractionRequest(BaseModel):
    message: str


class SessionContext(BaseModel):
    persona: Persona
    context: str
    created_at: datetime = Field(default_factory=datetime.utcnow)