from datetime import datetime, timezone

from pydantic import BaseModel, Field

from humanoid.models import Persona


class SessionContext(BaseModel):
    persona: Persona
    context: str
    model: str
    history: list = []
    session_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def add_message(self, content: str, role: str):
        self.history.append({"content": content, "role": role})