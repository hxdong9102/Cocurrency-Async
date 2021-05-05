# **************************************************************
# title: new threading coroutine
# ver: 1.0
# Author: Dong Haixia
# Date: 2021-5-5
# **************************************************************

import asyncio
import time
from threading import Thread

a = lambda: time.time()


def start_loop(loop):

    # 设置一个事件循环为当前线程的事件循环
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def do_some_work(x):
    print('Waiting {}'.format(x))
    await asyncio.sleep(x)
    print('Done after {}s'.format(x))


def more_work(x):
    print('More work {}'.format(x))
    time.sleep(x)
    print('Finished more work {}'.format(x))


start = a()
# 创建一个新的事件循环
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
print('TIME: {}'.format(time.time() - start))

asyncio.run_coroutine_threadsafe(do_some_work(6), new_loop)
asyncio.run_coroutine_threadsafe(do_some_work(4), new_loop)