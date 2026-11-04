import asyncio

baza_korisnika = [
    {"korisnicko_ime": "mirko123", "email": "mirko123@gmail.com"},
    {"korisnicko_ime": "ana_anic", "email": "aanic@gmail.com"},
    {"korisnicko_ime": "maja_0x", "email": "majaaaaa@gmail.com"},
    {"korisnicko_ime": "zdeslav032", "email": "deso032@gmail.com"},
]

baza_lozinka = [
    {"korisnicko_ime": "mirko123", "lozinka": "lozinka123"},
    {"korisnicko_ime": "ana_anic", "lozinka": "super_teska_lozinka"},
    {"korisnicko_ime": "maja_0x", "lozinka": "s324SDFfdsj234"},
    {"korisnicko_ime": "zdeslav032", "lozinka": "deso123"},
]


async def autorizacija(korisnik_iz_baze, lozinka):
    await asyncio.sleep(2)
    korisnicko_ime = korisnik_iz_baze["korisnicko_ime"]
    zapis = next((z for z in baza_lozinka if z["korisnicko_ime"] == korisnicko_ime), None)
    if zapis and zapis["lozinka"] == lozinka:
        return f"Korisnik {korisnicko_ime}: Autorizacija uspješna."
    return f"Korisnik {korisnicko_ime}: Autorizacija neuspješna."


async def autentifikacija(korisnik):
    await asyncio.sleep(3)
    korisnicko_ime = korisnik["korisnicko_ime"]
    korisnik_iz_baze = next(
        (
            k
            for k in baza_korisnika
            if k["korisnicko_ime"] == korisnicko_ime and k["email"] == korisnik["email"]
        ),
        None,
    )
    if korisnik_iz_baze is None:
        return f"Korisnik {korisnicko_ime} nije pronađen."
    return await autorizacija(korisnik_iz_baze, korisnik["lozinka"])


async def main():
    korisnik = {
        "korisnicko_ime": "ana_anic",
        "email": "aanic@gmail.com",
        "lozinka": "super_teska_lozinka",
    }
    rezultat = await autentifikacija(korisnik)
    print(rezultat)


asyncio.run(main())
