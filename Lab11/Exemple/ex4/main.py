import asyncio


async def factorial(name, number):          # functie pentru calculul factorialului
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)               # pentru fiecare iteratie asteapta 1 sec
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")        # printeaza rezultatul


async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(           # ruleaza functia in mod concurent
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )


if __name__ == '__main__':
    asyncio.run(main())