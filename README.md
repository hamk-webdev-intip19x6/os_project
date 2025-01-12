# os_project

Projektin tarkoituksena on tehdä [Djangoa](https://www.djangoproject.com/) käyttäen lainausjärjestelmä, johon käyttäjä pystyy rekisteröityä ja mm. lainaamaan, palauttamaan, tarkistamaan lainauksen tilan, sekä etsimään teoksia.

Samu Savikko, Olli Kokko ja Joni Heikkonen

## Riippuvuudet

[django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks)

## Ominaisuudet

- Rekisteröityminen, sisäänkirjautuminen, salasanan vaihto
- Teoksien etsiminen
- Teoksien lainaaminen
- Teoksien palautus
- Teoksien arvostelu ja kommentointi
- Responsiivinen ulkoasu

## Käyttöönotto

```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
