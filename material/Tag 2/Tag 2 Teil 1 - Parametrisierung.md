# Parametrisierung / Conftest

## Reste von gestern

09:00 - 09:30

- Mastodon-User anlegen
- Builtin Fixtures von pytest
- Mal in die fixtures von django-test schauen
	- `django_db_setup` ist ganz interessant
	- Da sind noch ein paar schöne fixtures drin
- Fixture renaming
- Fixtures in `conftest.py` legen / fixture-precedence

## [[Übung 1]]

09:30 - 10:00

- Server und client fixture in `conftest.py` verschieben, einmal ausprobieren, eine `server` fixture lokal zu erzeugen, die eine andere url hat
- Schreibe eine Fixture `def client`, die den Namen `mastodon_client`  bekommt, wie sieht das aus, wenn man `pytest --fixtures -v` aufruft?
- Schreibe einen Test für eine Funktion, die "hello world" ausgibt und überprüft, ob tatsächlich "hello world" ausgegeben wurde
- Bonus: Setup & Teardown
	- Schreibe eine Fixture, die eine Datei erzeugt und nach dem Test wieder entfernt
	- Einen Test, der diese Fixture verwendet und überprüft, ob die Datei da ist
	- Einen weiteren Test, der sicherstellt, dass die Datei nach dem Test wieder entfernt wurde
	
## Parametrisierung

### Tests

10:00 - 10:30

- Zeigen, dass ein neuer Toot in unterschiedlichen Timelines auftaucht
-  Beispiel mit django management commands?
- Vielleicht toots syncen oder so?
- Alte toots löschen?

## [[Übung 2]]

10:30 - 11:00

- Schreibe einen Test, der für alle get views ohne Parameter aus `locnus/views.py` / `locnus/urls.conf` sicherstellt, dass eine Response mit status 200 zurückkommt

## Pause 1

11:00 - 11:15

### Fixtures

11:15 - 11:45

- Beispiel für Parametrisierung von Fixtures
- Vielleicht ein paar der parametrisierten Tests umstellen

## [[Übung 3]]

11:45 - 13:00

- Die view-Tests von eben so umschreiben, dass parametrisierte Fixtures anstatt Tests verwendet werden
- Alle Formulare, die leer invalid sind mithilfe eine parametrisierten Fixture testen



