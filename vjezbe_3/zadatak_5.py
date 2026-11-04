import asyncio


async def secure_data(podaci):
    await asyncio.sleep(3)
    return {
        "prezime": podaci["prezime"],
        "broj_kartice": hash(podaci["broj_kartice"]),
        "CVV": hash(podaci["CVV"]),
    }


async def main():
    osjetljivi_podaci = [
        {"prezime": "Horvat", "broj_kartice": "4111111111111111", "CVV": "123"},
        {"prezime": "Kovačić", "broj_kartice": "5500000000000004", "CVV": "456"},
        {"prezime": "Babić", "broj_kartice": "340000000000009", "CVV": "789"},
    ]
    zadaci = [asyncio.create_task(secure_data(podatak)) for podatak in osjetljivi_podaci]
    rezultati = await asyncio.gather(*zadaci)
    for rezultat in rezultati:
        print(rezultat)


asyncio.run(main())
