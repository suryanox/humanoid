from pydantic import BaseModel


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
    next_interaction: str