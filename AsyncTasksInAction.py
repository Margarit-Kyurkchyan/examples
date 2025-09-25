import asyncio


async def task(name, delay):
    print(f"Start {name}")
    await asyncio.sleep(delay)
    print(f"End {name}")


async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 6),
        task("C", 4),
    )

asyncio.run(main())