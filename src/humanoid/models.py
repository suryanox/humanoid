from typing import Annotated

from pydantic import BaseModel, Field

class InitiateInteractionResponse(BaseModel):
    session_id: str
    first_reply: str

class Persona(BaseModel):
    name: Annotated[str, Field(min_length=1)]
    role: Annotated[str, Field(min_length=1)]
    tone: Annotated[str, Field(min_length=1)]
    adherence: Annotated[float, Field(ge=0.0, le=1.0)]

class InitiateInteractionRequest(BaseModel):
    persona: Persona
    context: Annotated[str, Field(min_length=20)]
    model: Annotated[str, Field(min_length=1)]

class InteractionResponse(BaseModel):
    reply: str


class InteractionRequest(BaseModel):
    message: Annotated[str, Field(min_length=1)]
