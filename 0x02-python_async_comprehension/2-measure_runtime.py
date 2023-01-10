#!/usr/bin/env python3
'''Run time for four parallel comprehensions'''
import asyncio
import time
async_comp = __import__('1-async_comprehension.py').async_comprehension


async def measure_runtime() -> float:
    '''Running parellel comprehensions 4 times'''
    start = time.time()
    tasks = [async_comp() for i in range(4)]
    await asyncio(*tasks)
    end = time.time()
    return start - end
