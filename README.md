# Reseptisovellus

## Vaatimusmäärittely

- Käyttäjä voi luoda uuden tunnuksen sekä kirjautua sisään ja ulos.
- Käyttäjä voi luoda omia reseptejään sekä poistaa tai muokata luomiaan reseptejä.
  - Käyttäjä kirjoittaa reseptiin nimen, ainekset ja vaiheet.
- Käyttäjä näkee etusivulla omat reseptinsä, ja voi siirtyä niiden sivuille.
- Käyttäjä voi hakea etusivulla reseptejä nimen perusteella.

### Mahdollinen lisäkehitys

- Käyttäjä voi hakea toisen käyttäjän hänen käyttäjätunnuksensa perusteella ja lähettää hänelle kaveripyynnön.
- Käyttäjä näkee etusivulla reseptien lisäksi kaverilistansa ja uudet kaveripyynnöt, jotka hän voi hyväksyä tai hylätä.
- Käyttäjä voi siirtyä kaverilistansa kautta toisen käyttäjän sivulle, jossa hän näkee tämän käyttäjän reseptit ja voi halutessaan poistaa käyttäjän kavereistaan.

## Sovelluksen asennus

Luo virtuaaliympäristö komennolla "python3 -m venv venv" ja käynnistä se komennolla "source venv/bin/activate". Asenna tarvittavat kirjastot komennolla "pip install -r requirements.txt". Asenna koneellesi myös PostgreSQL ja käynnistä se kommennolla "start-pg.sh".

Ennen sovelluksen ensimmäistä käyttökertaa luo tarvittavat taulut komennolla "psql < schema.sql". Luo myös tiedosto ".env" ja lisää siihen rivi "SECRET_KEY= *satunnainen avain* ".

Käynnistä sovellus ajamalla komento "flask run" ja siirtymällä viimeiselle riville tulostuneeseen osoitteeseen.

## Nykyinen toiminnallisuus

- Etusivulla voi kirjautua sisään tai luoda uuden käyttäjän.
- Kirjautumisen jälkeen etusivulla voi luoda uusia reseptejä tai siirtyä luotujen reseptien sivuille sekä kirjautua ulos.
- Uudelle reseptille kirjoitetaan luontivaiheessa nimi, ainesosat ja valmistusohje.
- Reseptin sivulla näkyvät sen tiedot, mutta tekstin muotoilu on vielä keskeneräinen.

## Tiedossa olevat ongelmat

- Muiden käyttäjien reseptejä pääsee katsomaan kirjoittamalla itse URL-osoitteen.
