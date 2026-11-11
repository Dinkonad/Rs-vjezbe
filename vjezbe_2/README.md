Vjezba 2 - Priprema podataka za web-aplikaciju

Opis: 3 korutine za frizerski salon - usluge (cijene), frizeri (tim), termini (slobodno/zauzeto). Neovisne jedna o drugoj, svaka ceka nasumicno 1-3s i vraca podatke.

Vremena cekanja: usluge 2.28s, frizeri 1.05s, termini 1.55s
Izmjereno: sekvencijalno 4.90s, konkurentno 2.30s

Odgovori:
- Sekvencijalno 4.90s jer korutine cekaju jedna drugu.
- Konkurentno 2.30s jer se cekanja preklapaju preko gather().
- Razlika: sekvencijalno ceka da jedna zavrsi prije sljedece, konkurentno sve odmah krenu i izmjenjuju se.
- time.sleep blokira dretvu pa bi konkurentno bilo isto sporo kao sekvencijalno.
- gather() vraca rezultate po redoslijedu poziva, ne zavrsetka.

Frontend URL: https://rs-vjezbe-frontend-vilh.onrender.com
