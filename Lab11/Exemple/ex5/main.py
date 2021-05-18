import asyncio

async def print_number(number):         # functie de printat un nr
    print(number)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()     # se creeaza o bucla folosind metoda get_event_loop()

    loop.run_until_complete(            # bucla ruleaza folosind methoda run_until_complete()
        asyncio.wait([                  # care primeste ca parametru functia de mai sus
            print_number(number)
            for number in range(10)
        ])
    )