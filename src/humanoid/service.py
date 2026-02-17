import uuid

from humanoid.models import InitiateInteractionResponse, InteractionResponse, InitiateInteractionRequest
from humanoid import cache


async def initiate_interaction(request: InitiateInteractionRequest) -> InitiateInteractionResponse:
    session_id = str(uuid.uuid4())
    await cache.set(session_id, request)
    return InitiateInteractionResponse(session_id=session_id)


async def interact(session_id: str) -> InteractionResponse:
    return InteractionResponse(next_interaction=session_id)
