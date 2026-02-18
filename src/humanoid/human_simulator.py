from litellm import completion
from humanoid.session_context import SessionContext
from humanoid import cache
from typing import Optional

async def talk(context: SessionContext, message: Optional[str] = None) -> str:
    user_message = message or "Hello, how are you?" # TODO: Replace with prompt
    context.add_message(user_message, "user")

    response = completion(
        model=context.model,
        messages=context.history
    )

    result_message = response.choices[0].message
    context.add_message(result_message.content, result_message.role)

    await cache.set(context.session_id, context)

    return result_message.content



