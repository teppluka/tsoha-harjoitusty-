# Reseptisovellus

## Toiminnallisuus

- Etusivulla voi kirjautua sisään tai luoda uuden käyttäjän.
- Kirjautumisen jälkeen etusivulla voi luoda uusia reseptejä tai siirtyä luotujen reseptien sivuille.
  - Uudelle reseptille kirjoitetaan luontivaiheessa nimi, ainesosat ja valmistusohje.
  - Reseptin sivulta näkee sen tiedot ja voi poistaa reseptin.
- Kaverit -sivulla näkee saapuneet kaveripyynnöt, oman kaverilistan, ja voi hakea muita käyttäjiä nimen perusteella.
  - Kaverilistasta voi siirtyä kavereiden sivuille, josta näkee heidän reseptinsä.
  - Hakutoiminnon avulla voi siirtyä kenen tahansa sivulle, mutta vain kavereiden reseptien sisältöä pääsee katsomaan.
  - Kaveripyyntöjä voi lähettää muiden käyttäjien sivuilla.


## Sovelluksen asennus

Luo virtuaaliympäristö komennolla "python3 -m venv venv" ja käynnistä se komennolla "source venv/bin/activate". Asenna tarvittavat kirjastot komennolla "pip install -r requirements.txt". Asenna koneellesi myös PostgreSQL ja käynnistä se kommennolla "start-pg.sh".

Ennen sovelluksen ensimmäistä käyttökertaa luo tarvittavat taulut komennolla "psql < schema.sql". Luo myös tiedosto ".env" ja lisää siihen rivi "SECRET_KEY= *satunnainen avain* ".

Käynnistä sovellus ajamalla komento "flask run" ja siirtymällä viimeiselle riville tulostuneeseen osoitteeseen.

