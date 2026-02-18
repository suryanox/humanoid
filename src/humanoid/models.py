from typing import Annotated

import langcodes
from pydantic import BaseModel, Field, field_validator


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
    language_code: Annotated[str, Field(min_length=2, max_length=10)]

    @field_validator("language_code")
    @classmethod
    def validate_language_code(cls, value: str) -> str:
        try:
            lang = langcodes.Language.get(value)

            if not lang.language:
                raise ValueError

            return lang.language
        except Exception:
            raise ValueError("Invalid ISO language code")

class InteractionResponse(BaseModel):
    reply: str


class InteractionRequest(BaseModel):
    message: Annotated[str, Field(min_length=1)]
