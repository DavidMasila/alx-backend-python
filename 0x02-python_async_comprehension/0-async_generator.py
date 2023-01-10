#!/usr/bin/env python3
''' Async Generator '''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float,None, None]:
    ''' Generator '''
    for i in random.uniform(0, 10):
        yield i
        await asyncio.sleep(1)
