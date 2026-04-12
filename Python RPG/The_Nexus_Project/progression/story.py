import asyncio


async def training_part1():
    await asyncio.sleep(1)
    print("You find yourself in a white room with nothing but a target dummy and a sword on the ground!")
    await asyncio.sleep(2)
    print("You approach the sword and try to pick it up! Do you? (Y/N)")
    action = input()
