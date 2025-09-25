import asyncio

async def greet():
    print("Hello ...")
    await asyncio.sleep(3)
    print("Goodbye")

asyncio.run(greet())