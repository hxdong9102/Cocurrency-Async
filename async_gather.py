# **************************************************************
# title: asyncio multi tasks---asyncio.gather
# ver: 1.0
# Author:
# Date: 2021-5-5
# **************************************************************

# import asyncio
# import time
# import threading
 
# a=time.time()
 
# async def hello1():
#     print(f"Hello world 01 begin,my thread is:{threading.currentThread()}")
#     await asyncio.sleep(3)
#     print("Hello again 01 end")
 
# async def hello2():
#     print(f"Hello world 02 begin,my thread is:{threading.currentThread()}")
#     await asyncio.sleep(2)
#     print("Hello again 02 end")
 
# async def hello3():
#     print(f"Hello world 03 begin,my thread is:{threading.currentThread()}")
#     await hello2()
#     await hello1()
#     print("Hello again 03 end")
 
# loop = asyncio.get_event_loop()
# tasks = [hello3()]
# loop.run_until_complete(asyncio.wait(tasks))
 
# loop.close()
 
 
# b=time.time()
# print('---------------------------------------')
# print(b-a)


import asyncio
import time


async def hello1(a, b):
    print("Hello world 01 begin")
    # 模拟耗时任务3秒
    await asyncio.sleep(3)  
    print("Hello again 01 end")
    return a+b


async def hello2(a, b):
    print("Hello world 02 begin")
    # 模拟耗时任务2秒
    await asyncio.sleep(2)  
    print("Hello again 02 end")
    return a-b


async def hello3(a, b):
    print("Hello world 03 begin")
    # 模拟耗时任务4秒
    await asyncio.sleep(4)   
    print("Hello again 03 end")
    return a*b


async def main():
    # 封装多任务的入口函数
    task1 = asyncio.ensure_future(hello1(10, 5))
    task2 = asyncio.ensure_future(hello2(10, 5))
    task3 = asyncio.ensure_future(hello3(10, 5))
 
    results = await asyncio.gather(task1, task2, task3)
    # 通过迭代获取函数的结果，每一个元素就是相对应的任务的返回值，顺序都没变   
    for result in results:
        print(result)

loop = asyncio.get_event_loop()              
loop.run_until_complete(main())
loop.close()
