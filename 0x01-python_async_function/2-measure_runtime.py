#!/usr/bin/env python3
'''Measuring run time'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_dalay: int) -> float:
    start = time.time()
    asyncio.run(wait_n(n, max_dalay))
    end = time.time()
    total_time = start - end
    return total_time / n
