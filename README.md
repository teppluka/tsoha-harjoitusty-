# Reseptisovellus

## Vaatimusmäärittely

- Käyttäjä voi luoda uuden tunnuksen sekä kirjautua sisään ja ulos.
- Käyttäjä voi luoda omia reseptejään sekä poistaa tai muokata luomiaan reseptejä.
  - Käyttäjä kirjoittaa reseptiin nimen, ainekset sekä niiden määrät ja yksitellen reseptin vaiheet.
- Käyttäjä näkee etusivulla omat reseptinsä, ja voi siirtyä niiden sivuille.
- Käyttäjä voi hakea etusivulla reseptejä nimen perusteella.

### Mahdollinen lisäkehitys

- Käyttäjä voi hakea toisen käyttäjän hänen käyttäjätunnuksensa perusteella ja lähettää hänelle kaveripyynnön.
- Käyttäjä näkee etusivulla reseptien lisäksi kaverilistansa ja uudet kaveripyynnöt, jotka hän voi hyväksyä tai hylätä.
- Käyttäjä voi siirtyä kaverilistansa kautta toisen käyttäjän sivulle, jossa hän näkee tämän käyttäjän reseptit ja voi halutessaan poistaa käyttäjän kavereistaan.

## Sovelluksen käyttö

Siirry virtuaaliymäristöön ajamalla sovelluskansiossa komento "source venv/bin/activate". Asenna tämän jälkeen tarvittavat kirjasot komennoilla "pip install flask", "pip install flask-sqlalchemy" ja "pip install psycopg2". Asenna koneellesi myös PostgreSQL.

Ennen sovelluksen ensimmäistä käyttökertaa siirry PostgreSQL-tulkkiin komennolla "psql" ja aja tulkissa komento "CREATE TABLE recipes (id SERIAL PRIMARY KEY, name TEXT, ingredients TEXT, steps TEXT);".

Käynnistä sovellus ajamalla komento "flask run" ja siirtymällä viimeiselle riville tulostuneeseen osoitteeseen.

## Nykyinen toiminnallisuus

- Etusivulla voi luoda uusia reseptejä tai siirtyä luotujen reseptien sivuille.
- Uudelle reseptille kirjoitetaan luontivaiheessa nimi, ainesosat ja valmistusohje.
- Reseptin sivulla näkyvät sen tiedot, mutta tekstin muotoilu on vielä keskeneräinen.