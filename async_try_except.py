# **************************************************************
# title: Python async mode exercise
# ver: 1.0
# Author: Dong Haixia
# Date: 2021-5-5
# **************************************************************

import asyncio
import time

a = lambda: time.time()


async def do_some_work(x):
    print("Waiting:", x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(6)
coroutine3 = do_some_work(4)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3),
]

start = a()
# 获得一个事件循环，如果当前线程还没有事件循环，则创建一个新的事件循环loop
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print(task.cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()

print("Time:", a()-start)
