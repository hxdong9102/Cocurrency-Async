# **************************************************************
# title: asyncio---realize timer
# ver: 1.0
# Author:
# Date: 2021-5-5
# **************************************************************

import asyncio


async def delay(time):
    await asyncio.sleep(time)


async def timer(time, function):
    while True:
        future = asyncio.ensure_future(delay(time))
        await future
        future.add_done_callback(function)


def func(future):
    print('2 seconds have passed!')


if __name__ == '__main__':
    asyncio.run(timer(2, func))
