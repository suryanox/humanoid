import logging

from humanoid.models import SessionContext, InteractionResponse

logger = logging.getLogger(__name__)


class HumanSimulator:
    async def talk(self, session_context: SessionContext, message: str) -> InteractionResponse:
        logger.info(f"Received message: {session_context}")
        return InteractionResponse(reply=message)
