import uuid

from humanoid.human_simulator import talk
from humanoid.models import (
    InitiateInteractionResponse,
    InteractionResponse,
    InitiateInteractionRequest,
    InteractionRequest,
)
from humanoid.session_context import SessionContext
from humanoid import cache



async def initiate_interaction(request: InitiateInteractionRequest) -> InitiateInteractionResponse:
    session_id = str(uuid.uuid4())
    session_context = SessionContext(
        session_id=session_id,
        persona=request.persona,
        context=request.context,
        model=request.model,
        language_code=request.language_code,
    )
    first_reply = await talk(session_context, message=None)
    return InitiateInteractionResponse(session_id=session_id, first_reply=first_reply)


async def interact(session_id: str, request: InteractionRequest) -> InteractionResponse:
    session_context = await cache.get(session_id)
    if session_context is None:
        raise Exception(f"Interaction not set for {session_id}")
    next_reply = await talk(session_context, request.message)
    return InteractionResponse(reply=next_reply)
