import asyncio
import time


async def dohvati_korisnike():
    await asyncio.sleep(3)
    return [
        {"korisnicko_ime": "dinko", "email": "dinko@gmail.com"},
        {"korisnicko_ime": "Luka", "email": "Luka@gmail.com"},
    ]


async def dohvati_proizvode():
    await asyncio.sleep(5)
    return [
        {"naziv": "laptop", "cijena": 2000.00},
        {"naziv": "logi miš", "cijena": 124.99},
    ]


async def main():
    korisnici, proizvodi = await asyncio.gather(dohvati_korisnike(), dohvati_proizvode())
    print(korisnici)
    print(proizvodi)


t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")
