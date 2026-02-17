from typing import Any, Optional
from aiocache import Cache

_cache = Cache(Cache.MEMORY)

async def get(key: str) -> Optional[Any]:
    return await _cache.get(key)

async def set(key: str, value: Any, ttl: int = 86400) -> None:
    await _cache.set(key, value, ttl=ttl)