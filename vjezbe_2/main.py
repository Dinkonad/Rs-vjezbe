import asyncio
import random
import time
import json

random.seed(42)


async def dohvacanje_usluga(cekanje):
    print('Dohvacanje usluga iz baze.')
    await asyncio.sleep(cekanje)
    print('Zavrseno dohvacanje usluga.')
    return [
        {"usluga": "sisanje", "cijena": 10},
        {"usluga": "zensko sisanje", "cijena": 20},
        {"usluga": "brijanje", "cijena": 15}
    ]

async def dohvacanje_frizera(cekanje):
    print('Dohvacanje frizera.')
    await asyncio.sleep(cekanje)
    print('Zavrseno dohvacanje frizera.')
    return [
        {"ime": "Dinko", "prezime": "Nad"},
        {"ime": "Luka", "prezime": "Relja"}
    ]

async def dohvati_slobodne_termine(cekanje):
    print("Zapocinje dohvacanje slobodnih termina...")
    await asyncio.sleep(cekanje)
    print("Zavrseno dohvacanje slobodnih termina.")
    return [
        {"datum": "11-10", "vrijeme": "09.00", "slobodno": True},
        {"datum": "11-10", "vrijeme": "10.30", "slobodno": False},
        {"datum": "11-10", "vrijeme": "12.00", "slobodno": True}
    ]


async def sekvencijalno(t1, t2, t3):
    start = time.perf_counter()
    usluge = await dohvacanje_usluga(t1)
    frizeri = await dohvacanje_frizera(t2)
    termini = await dohvati_slobodne_termine(t3)
    kraj = time.perf_counter()
    print(f"Sekvencijalno ukupno: {kraj - start:.2f}s")
    return {"usluge": usluge, "frizeri": frizeri, "termini": termini}


async def konkurentno(t1, t2, t3):
    start = time.perf_counter()
    usluge, frizeri, termini = await asyncio.gather(
        dohvacanje_usluga(t1),
        dohvacanje_frizera(t2),
        dohvati_slobodne_termine(t3),
    )
    kraj = time.perf_counter()
    print(f"Konkurentno ukupno: {kraj - start:.2f}s")
    return {"usluge": usluge, "frizeri": frizeri, "termini": termini}


async def main():
    t1 = random.uniform(1, 3)
    t2 = random.uniform(1, 3)
    t3 = random.uniform(1, 3)
    print(f"Vremena cekanja - usluge: {t1:.2f}s, frizeri: {t2:.2f}s, termini: {t3:.2f}s")

    print("sekvencijalno")
    rezultat_seq = await sekvencijalno(t1, t2, t3)

    print("konkurentno")
    rezultat_konk = await konkurentno(t1, t2, t3)

    print("test redoslijeda gather()")
    r1 = await asyncio.gather(
        dohvacanje_usluga(0.2), dohvacanje_frizera(0.1), dohvati_slobodne_termine(0.3)
    )
    print("poredak poziva: usluge, frizeri, termini ->", [type(x).__name__ for x in r1])
    r2 = await asyncio.gather(
        dohvati_slobodne_termine(0.3), dohvacanje_usluga(0.1), dohvacanje_frizera(0.2)
    )
    print("poredak poziva: termini, usluge, frizeri ->", [type(x).__name__ for x in r2])
    print("prvi element r2 (treba biti termini, ne usluge):", r2[0])

    with open("podaci.json", "w", encoding="utf-8") as f:
        json.dump(rezultat_konk, f, ensure_ascii=False, indent=2)
    print("Podaci spremljeni u podaci.json")


asyncio.run(main())
