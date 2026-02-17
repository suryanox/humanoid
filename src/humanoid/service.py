import uuid

from humanoid.models import (
    InitiateInteractionResponse,
    InteractionResponse,
    InitiateInteractionRequest,
    InteractionRequest,
    SessionContext,
)
from humanoid import cache
from humanoid.human_simulator import HumanSimulator

human_simulator = HumanSimulator()


async def initiate_interaction(request: InitiateInteractionRequest) -> InitiateInteractionResponse:
    session_id = str(uuid.uuid4())
    session_context = SessionContext(
        persona=request.persona,
        context=request.context,
    )
    await cache.set(session_id, session_context)
    return InitiateInteractionResponse(session_id=session_id)


async def interact(session_id: str, request: InteractionRequest) -> InteractionResponse:
    session_context = await cache.get(session_id)
    if session_context is None:
        raise Exception(f"Interaction not set for {session_id}")
    return await human_simulator.talk(session_context, request.message)
