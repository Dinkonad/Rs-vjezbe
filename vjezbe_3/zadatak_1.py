import asyncio



async def dohvati_podatke():
    await asyncio.sleep(3)
    podaci = [broj for broj in range(1, 11)]
    print("Podaci dohvaceni uspjesno.")
    return podaci



async def main():
    rezultat = await dohvati_podatke()
    print(rezultat)


asyncio.run(main())
