from humanoid.models import InitiateInteractionResponse, InteractionResponse


def initiate_interaction() -> InitiateInteractionResponse:
    return InitiateInteractionResponse(session_id="")


def interact(session_id: str) -> InteractionResponse:
    return InteractionResponse(next_interaction=session_id)
