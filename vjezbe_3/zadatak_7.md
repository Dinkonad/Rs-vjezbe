Zadatak 7 - objasnjenje

Kod pokrece tri timera odjednom (3, 5 i 7 sekundi) preko create_task, a onda ih
sve zajedno ceka s gather(). Zato program ne traje 3+5+7=15 sekundi nego samo
oko 7 sekundi, jer se sva tri timera vrte u isto vrijeme, ne jedan pa drugi pa treci.

Kad se pozove create_task, sva tri timera se odmah "prijave" event loopu, ali
jos nista ne rade dok loop ne dode na njih. Onda svaki od njih ispise koliko mu
jos sekundi ostaje i ode spavati jednu sekundu (await asyncio.sleep(1)). E tu je
fora - kad timer ode spavati, on ne blokira ništa, nego event loop u tom
trenutku skoci na sljedeci timer i pusti i njega da odradi svoj ispis, pa onda
na treci, i tako redom. Znaci svaka sekunda se sva tri timera naizmjence
ispisu, kao da se smjenjuju.

Ako gledamo po sekundama otprilike ovako ide:

- sekunda 0: sva tri ispisu koliko im ostaje (3, 5, 7) i odu spavati
- sekunda 1: ispisu 2, 4, 6
- sekunda 2: ispisu 1, 3, 5
- sekunda 3: prvi timer je gotov i ispise da je vrijeme isteklo, druga dva nastavljaju (2 i 4 preostalo kod njih dalje)
- sekunda 4-5: drugi timer takoder zavrsi i ispise da je isteklo
- sekunda 6-7: treci timer je zadnji koji zavrsi, i tek onda cijeli program stane jer je gather cekao bas na njega

Bitno je da se u svakom trenutku stvarno izvrsava samo jedan dio koda (python
ionako moze samo jednu stvar odjednom raditi zbog GIL-a), ali zato sto svaki
timer stalno "pusti" kontrolu dok ceka tu jednu sekundu, event loop stigne u
meduvremenu odraditi i ostale timere. Zato izgleda kao da se sve odvija
istovremeno iako to tehnicki nije paralelno nego konkurentno - samo se brzo
izmjenjuju.

Program ce zavrsiti tek kad zavrsi najduzi timer (treci, 7 sekundi), jer gather
ceka da svi zavrse prije nego sto main() moze nastaviti dalje.
