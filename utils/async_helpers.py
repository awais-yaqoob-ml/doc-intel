# utils/async_helpers.py

import asyncio
from typing import Callable, Any, List, Awaitable


async def run_concurrently(tasks: List[Awaitable[Any]]) -> List[Any]:
    """
    Run async tasks concurrently and return results.
    """
    return await asyncio.gather(*tasks)


def run_sync(func: Callable, *args, **kwargs) -> Any:
    """
    Run sync function safely (placeholder for threadpool execution).
    """
    return func(*args, **kwargs)


async def to_async(func: Callable, *args, **kwargs) -> Any:
    """
    Convert sync function to async wrapper (basic version).
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, lambda: func(*args, **kwargs))