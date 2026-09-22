# Toot!

## Was ist Mocking?

14:00 - 14:30

- Mal erklären wie das mit dem Mocking so prinzipiell funktioniert
- Beispiel wären Tests für Account

## [[Übung 4]]

Vielleicht mal ein bisschen TDD?

14:30 - 15:00

- Schreibe einen Test, der testet, ob `mastodon.status_post` aufgerufen wurden, wenn man einen Toot abschickt
- Schreibe einen Test für das Toot-Formular
- Schreibe einen Test für den View, der das Toot-Formular anzeigt

## Implementation Toot

15:00 - 15:30

- Erst mal alle Tests mit `xfail` markieren, dann nach und nach implementieren
- Implementationen
	- `status_post` in models.py
	- `TootForm` in forms.py
	- `post_status` in views.py
	- `create_post`-template
	- link in sidenav setzen

## Marker

15:30 - 16:00

- Eingebaute Marker
- Version von locnus setzen..
- Markieren von modulen, Klassen
- Markieren von parametrisierten Tests
- Marker müssen komplett sein, nicht wie bei Keywords
- Marker für 3 Toots etc, request.node.get_closest_marker
- `pytest --markers`

## Pause

16:00 - 16:15

## [[Übung 5]]

16:15 - 16:45

- Schreibe einen Test, der geskippt wird
- Ändere einen der post-toot-Tests so, dass er geskippt wird, wenn die locnus-Version < 0.1 ist
- Schreibe einen xfail-Test, der aber trotzdem failed und einen Grund ala "Soll bis nächste Woche von X gefixt werden"
- Markiere eine parametrisierte Fixture und damit einen Teil aller Tests, die diese Fixture verwenden

# Aufräumen

16:45 - 17:15

- Mal alles in conftest sortieren
- Vielleicht auch mal ein Unterverzeichniss mit bestimmten Tests?
- Tests in views_test, models_test etc verschieben
- Einmal coverage laufen lassen Ausgabe erklären


## [[Übung 6]]

17:15 - 17:45

- git pull 😇
- Coverage selbst laufen lassen
- Testcoverage um 10% erhöhen 😅


## Fragen / Anmerkungen

17:45 - 18:00
