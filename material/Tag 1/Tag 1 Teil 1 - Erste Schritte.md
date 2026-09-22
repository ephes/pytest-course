# Vorstellungsrunde 09:00 - 09:30

Wer bin ich und was mache ich so? Vielleicht eine Präsentation als Überblick über pytest insgesamt. Von der ganz groben Struktur her würde ich immer ein neues Thema zeigen und dann gibt es ein paar Übungen dazu und wir schauen gemeinsam, ob das alles so funktioniert wie gedacht 😃.

[[Einführung]]

## Fragen an die Teilnehmer

- Wie lange macht ihr den Kram hier schon? Erfahrungslevel, wie unterschiedlich sind die Level?
- Was interessiert euch besonders?

# Umgebung aufsetzen 09:30 - 10:00

- Python installieren etc
- Das Beispielprojekt auschecken
- Dinge, die man sonst so braucht

# Erste Schritte mit Pytest 10:00 - 10:15

**Source**: [["Hello World"-Tests]]

## Hello World Test

```shell
source venv/bin/activate.fish
cd tests
# Alle bis auf den test_passing auskommentieren
pytest  # Ausgabe erklären
```

## Ein Test Failed

```shell
# den second_test.py einkommentieren
pytest  # first geht, second failed - Ausgabe erklären
pytest -v
pytest --tb=no
```

## Ein erster echter Test
```
# den add_numbers test einkommentieren -> Ausgabe erklären
pytest
pytest -v
```

# Übung 1 10:15 - 11:00

1. Lasse selbst mal pytest laufen und versuche die Ausgabe zu verstehen
2. Schreibe einen Test, der überprüft, ob die Funktion `concat_strings` auch tatsächlich Strings aneinanderhängt 😃.
3. Vielleicht mal ein paar unterschiedliche Tests und Asserts ausprobieren


# Kleine Pause 11:00

# Klassen / Discovery / Struktur 11:15 - 11:45

## Testklassen

Bitte nur zur Strukturierung von Tests, keine wilden Vererbungshirarchien, helper-Funktionen kann man auch einfach so importieren, die muss man nicht reinerben.

```shell
# Testklasse hinzufügen
pytest -v # zeigen, wo der Test aus der Klasse ausgeführt wurde
```

## Wie werden Tests gefunden?

- In Dateien, die mit `test_` anfangen oder mit `_test.py` enden
- Funktionen, die mit `test_` anfangen
- Klassen, die mit `Test` anfangen
- Wie Tests gefunden werden ist aber auch konfigurierbar

## Ausprobieren

Tests finden:
```shell
pytest
pytest -v  # Pfad zum Test wird mit angezeit -> copy & paste
pytest -v first_test.py::TestAThing::test_with_method # Pfad zur Methode
pytest -v first_test.py::TestAThing # alle Tests in der Klasse
pytest first_test.py::test_passing # eine bestimmter Test als Funktion
pytest first_test.py # alle tests in einem modul
pytest -k passing # suche nach einem keyword
pytest -k "not number"
pytest -s # output capture..
```

## Arten, wie Tests failen können

	- Assert geht schiefx
- Man ruft pytest.fail() von Hand auf
- Eine Exception wird innerhalb des Testaufrufs geworfen
- Exceptions in Fixtures führen zu einem Error, dazu später mehr

```shell
# einen test mit pytest.fail() und einen, der eine exception raised schreiben
pytest -v
pytest --lf # test that failed during the last run
pytest --ff # all tests, but last failed first
pytest -x # exit on the first failed test or error
```

## Assert

- Zeigen, wie sich pytest assert traceback und normales python assert unterscheiden - pytest macht da höhere Magie, um den assert output zu rewriten, aber das ist halt sehr hilfreich

## Teststruktur

- Arange, act, assert (AAA)
- Given, when, then
- Soll es immer nur ein assert pro Test geben? -> Nö

```shell
# Beispieltest mit einem brüllenden Löwen?
```

## Übung 2 11:45 - 13:00

1. Schreibe eine Test-Klasse, die beide Testfunktionen als Methoden enthält.
3. Schreibe einen Test, der statt assert pytest.fail verwendet und nur eine Fehlermeldung ohne Traceback ausgibt
4. Schreibe eine Klasse mit einem Attribut und einen Test der überprüft, ob das Attribut korrekt gesetzt wurde
5. Bonus
	1. Schreibe ein modul animals mit einer Klasse Duck, die unterschiedlich laut quakt, je nachdem welche Lautstärke übergeben wird
	2. Schreibe einen Test, der überprüft, ob die Ente richtig quakt und annotiere die unterschieldichen Teile des AAA-Patterns (oder given, when, then - egal 😁)

**Source**: [[Übung 2 - Bonus]]
