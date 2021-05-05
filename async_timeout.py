# **************************************************************
# title: Python async mode exercise
# ver: 1.0
# Author: Dong Haixia
# Date: 2021-5-5
# **************************************************************


import asyncio


async def eternity():
    print('我马上开始执行')
    # 当前任务休眠2秒钟，2<3
    await asyncio.sleep(2)
    print('终于轮到我了')


async def main():
    # Wait for at most 1 second
    try:
        print('等你3秒钟哦')
        #给你3秒钟执行你的任务
        await asyncio.wait_for(eternity(), timeout=3)
    except asyncio.TimeoutError:
        print('超时了！')


asyncio.run(main())