#!/usr/bin/env python3 
'''Run time for four parallel comprehensions'''
import asyncio
import time
async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Running comprehension'''
    start_time = time.time()
    await asyncio.gather(async_comp(), async_comp(), async_comp())
    end_time = time.time()
    return end_time - start_time
