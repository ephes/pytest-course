# Tag 3 Teil 1

## Rekapitulation

09:00 - 09:30

- parametrize kann noch eine ids=function option mitgegeben werden
- Vielleicht noch mal einen Test für ein management-Command schreiben,
damit es auch noch andere Entrypoints gibt, ausser Web?
- Eine Kommandozeilenoption hinzufügen, mit der man nur die Smoke-Tests ausführen kann [pytest add option](https://docs.pytest.org/en/latest/example/markers.html#custom-marker-and-command-line-option-to-control-test-runs)


### Übung

09:30 - 10:00

- Füge einen Custom-Marker via conftest hinzu
- Test für ein management command, das eine Liste von Server-URLs importiert

## Test-Strategie

10:00 - 10:30

### Wo anfangen?

- Wenn man noch keine Tests hat, ist es wahrscheinlich nicht schlecht, mit den Views anzufangen (CRUD)
- Dann Input-Validation (Forms)
- Später kleinere Unittests für Business-Logik
- Einmal Happy Path, dann überlegen welche anderen Fälle auftreten können

### An unserem Beispiel

- Wenn man auf der Hauptseite ist und es gibt ein paar Toots in der Home-Timeline, werden die dann auch angezeigt? (Umstellen des Homeviews auf DB) 
- Was passiert, wenn die DB leer ist?

## Übung 1

10:30 - 11:00

- Welche Views haben wir noch nicht getestet? Schreibe einen Test für einen noch nicht getesteten view
-  Mache Accounts löschbar, stelle sicher, dass die entsprechenden Toots aus der Home-Timeline dann auch mit entfernt wurden

## Pause

11:00 - 11:15

## Htmx

11:00 - 11:45

Vielleicht einfach mal Toots automatisch nachladen, wenn neue ankommen? Mal schauen, ob wir das hinbekommen. Vielleicht ein zweiter Prozess / View, der neue Toots vom Server holt?

## Übung 2

11:45 - 12:15

- Einen Delete-Button für Server in der Server-List hinzufügen

## Konfiguration

12:15 - 12:45

[pytest-docs](https://docs.pytest.org/en/7.3.x/contents.html)

- pytest.ini / setup.cfg / tox.ini / pyproject.toml
- conftest.py
- -r erklären
- coverage
	- IDEs
	- html report
	- `#pragma: no cover`
- `pytest --trace-config`

### Übung 3

12:45 - 13:00

- Füge einen neuen Test im  Top-Level-Verzeichniss `additional_tests` hinzu und versuche pytest dazu zu bekommen, den mit laufen zu lassen :)
- Schreibe einen Test, der die coverage um mindestens 1% erhöht..

## Pause

13:00 - 14:00

## Deployment

14:00 - 14:30 - unklar?

- Versuche, locnus mal auf staging zu deployen

## Übung 4

- Hmm,  was könnte man da üben?

## Plugins

15:00 - 15:30

[Howto](https://docs.pytest.org/en/latest/how-to/plugins.html)
- pytest: [plugins](https://docs.pytest.org/en/7.3.x/reference/plugin_list.html)
- Auf pypi nach "Framework::Pytest" suchen
- github: [pytest-dev](https://github.com/pytest-dev/)
- Vielleicht noch mal das slow-Beispiel und alle slow tests skippen by default?

## Übung 5

15:30 - 16:00

- Installiere ein `pytest-sugar` und lasse pytest laufen - was hat sich verändert?
- Bonus: Füge via conftest ein command line flag hinzu, mit dem sich alle Tests skippen lassen, die die Datenbank verwenden

## Pause

16:00 - 16:15

## Debugging

16:15-16:45

- breakpoint
- IDEs
- --trace / --pdb
--pdbcls=IPython.terminal.debugger:TerminalPdb

## Übung 6

16:45 - 17:15

- Setze einen breakpoint und versuche mit pytest da hinzukommen
- Bonus: ipdb statt pdb verwenden

### Profiling

17:15 - 1730

- --durations
- py-spy
- suydt
- python -m cProfile -m pytest

## Fragen und Schluss?

17:30 - 18:00

Was könnten wir denn nochmal machen, oder vertiefen?

## Schluss

- [[Zusammenfassung]]

django-manage ansible modul verwenden
vielleicht auch virtualenv erzeugen?

https://shiv.readthedocs.io/en/latest/

Kann man in das environment anderer Prozesse schauen unter Linux?