# Projekt
Projekt na temu "Skladište automobilske robe" za kolegij Informacijski sustavi, omogućuje lakšu organizaciju i provjeru stanja skladišta, također lakša isporuka kao i brisanje podataka

# FUNKCIONALNOSTI: 
get artikl(GET metoda)
dodaj artikl(POST metoda)
azuriraj artikl(PUT metoda)
obrisi artikl(DELETE metoda)

# Pokretanje aplikacije:
Aplikacija se pokreće pomoću Dockera, potrebno je imati docker desktop u kojemu pokrećemo docker image za kreiranje kontenjera. U Visual studio Codu je potrebno kreirati App.py uz pomoć Pythona, također potrebno je u termininalu instalirati pip i flask.Flask je potreban za pomoćne funkcije koje Python nema ugrađene u sebi. U templates se nalazi index.html koji se koristi za prikaz CRUD funkciolanosti u aplikaciji, podaci.html se na nekim funkcionalnostima automatski otvori. Za pokretanje index.html samo ga je potrebno ubaciti u preglednik ili upisati http://localhost:5500.

UPDATE 14.6.2024.:Ako se ubaci index.html i upisani podaci se ne mogu poslati preko gumba "dodaj artikl", trebalo bi raditi uz pomoć Flask-CORS, taj dodatak se skida preko Powershella pomoću komande pip install. flask-cors

