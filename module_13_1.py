import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for b in range(1, 6):
        await  asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {b}-й шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 4))
    task2 = asyncio.create_task(start_strongman('Denis', 5))
    task3 = asyncio.create_task(start_strongman('Apollon', 7))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())
