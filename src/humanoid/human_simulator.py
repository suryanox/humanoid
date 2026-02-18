from litellm import completion

from humanoid.models import InteractionResponse
from humanoid.prompt_builder import PromptBuilder
from humanoid.session_context import SessionContext
from humanoid import cache
from typing import Optional

async def talk(context: SessionContext, message: Optional[str] = None) -> str:
    user_message = message or PromptBuilder(context).build()
    role = "system" if message is None else "user"
    context.add_message(user_message, role)

    response = completion(
        model=context.model,
        messages=context.history,
        response_format=InteractionResponse
    )

    result_message = response.choices[0].message
    context.add_message(result_message.content, result_message.role)

    await cache.set(context.session_id, context)

    return result_message.content
