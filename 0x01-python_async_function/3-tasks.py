#!/usr/bin/env python3
'''Tasks in asyncio'''
import asyncio
from typing import TypeVar
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creating task'''
    task1 = asyncio.create_task(wait_random(max_delay))
    return task1
