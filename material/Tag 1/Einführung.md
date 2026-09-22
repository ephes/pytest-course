# Was ist pytest?

**Framework und CLI**

- Ein Testframework
- Ein Kommandozeilentool, das automatisierte Tests findet, ausführt und einen Report ausgibt
- Es ist durch plugins und hook-functions erweiterbar
- Mehr Spaß beim Testen 🤩

# Warum pytest?

**Wegen den asserts!**

- Einfacher Einstieg
- Wenn man mehr Funktionalität braucht, kann man die bekommen
- Tests können sehr gut lesbar sein
- Verwendung des `assert` statements
- Fixtures, Parametrisierung und Plugins
- Man kann auch unittest Tests mit pytest laufen lassen

# Wofür pytest verwenden?

**So ungefähr alles**

- Python Packages
- Python Applikationen
- Applikationen, die via Python kontrolliert werden können
- web apps / Hardware / Applikationen in anderen Programmiersprachen

# pytest vs unittest

## pytest

**Ein einzelner Test**

```python
def test_passing():
	a = 1, 2, 3
	b = 1, 2, 3
	assert a == b
```


## unittest

```python
import unittest


class TestAThing(unittest.TestCase):
	def test_passing(self):
		a = 1, 2, 3
		b = 1, 2, 3
		self.assertEqual(a, b)
```

# Themen

 **Was wollen wir machen?**
- Tests schreiben (als Funktionen oder Klassen)
- Fixtures
- Parametrisierung (Tests, Fixtures)
- Marker
- Mocking
- Teststrategien
- Plugins
- Konfiguration

# Tests Schreiben

## Tests als Funktionen

```python
def test_something():
	expected = "some value"
	actual = some_function()
	assert actual == expected
```


## Tests als Klassen

```python

class TestSomething:
	def test_some_feature():
		expected = "some value"
		actual = some_function()
		assert actual == expected
```

## Was passiert beim Ausführen von Tests?

- Wie werden Tests eigentlich gefunden?
- Erweiterte tracebacks für `assert` 
- Was macht `pytest.fail()` und andere Dinge
- Wie stellt man sicher, dass bestimmte Exceptions geworfen wurden?


# Fixtures

```python
pytest.fixture()
def db():
	... # setup
	yield _db
	... # teardown


def test_action(db):
	...
	result = db.action()
	...
```

- setup und teardown
- Verwenden mehrerer Fixtures
- Eingebaute Fixtures
- Scope: function, class, module, session
- Gemeinsam genutzte Fixtures mit `conftest.py`

# Parametrisierung

**Jeder Parameter erzeug einen eigenen Test**
```python
@pytest.mark.parametrization("state", ["todo", "in prog", "done"])
def test_finish(cards_db, state):
	# for card in any state
	c = Card("summary", state-state) A
	i = cards db.add card(c)
	# calling finish
	cards_db.finish(i)
	# results in a final state of "done"
	c = cards_db.get_card(i)
	assert c.state == "done"
```

- Parametrisierte Tests
- Parametrisierte Fixtures
- Verwenden mehrerer Parameter

# Marker

**Tests taggen und dementsprechend Laufen lassen**
```python
@pytest.mark.skip()
def test_that_wont_run():
	...

@pytest.mark.custom()
def test_custom():
	...
```

- skip, skipif, xfail
- Subsets von Tests laufen lassen
- Marker und Fixtures kombinieren

# Teststrategien

**Wie effektiv testen?**

- Testpyramide (Unit, Integration, E2E)
- Wir wollen Änderung im Verhalten testen und nicht, ob sich die Implementation geändert hat
- [TDD in High Gear and Low Gear](http://www.cosmicpython.com/book/chapter_05_high_gear_low_gear.html)

# Generieren von Testdaten

**Oder vielleicht lieber alles selber machen?**

- Kapitel „Seed Your Database with a Custom Management Command“ in  [Boost Your Django DX](https://adamchainz.gumroad.com/l/byddx)
- [Model Bakery](https://github.com/model-bakers/model_bakery) / [Factory Boy](https://github.com/model-bakers/model_bakery)
- [Test factory functions in Django](https://lukeplant.me.uk/blog/posts/test-factory-functions-in-django/)

# Mocking

**pytest-mock!**

- monkeypatch
- unittest.mock
- pytest-mock
- [My Python testing style guide](https://blog.thea.codes/my-python-testing-style-guide/)

# Plugins

**Eher verwenden als selbst schreiben** 😅

- Die Funktionalität von pytest erweitern
- pytest-xdist: Tests parallel laufen lassen
- pytest-cov: Testcoverage ermitteln

# Konfiguration

```ini
[pytest] addopts =
	--strict-markers
	﻿--strict-config
	-ra

testpaths = tests

markers =
	smoke: subset of tests
```

- Wofür man Config-Files braucht
- pytest.ini
	- pyproject.toml
	- tox.ini
- Schicke Kommandozeilenoptionen
- Nützliche Einstellungen

# Beispiel: Ein Django Third Party Package

**Megalocnus - ausgestorbenes Riesenfaultier oder ein einfacher Mastodon-Client?**

Ein simpler Mastodon-Client

- Ist ein Django Third Party Package und damit ein Python Package (für PyPi / CI / CD etc)
- Enthält eine Beispielapplikation, die das third party package verwendet
- Erfordert nicht viel Django-Vorwissen
- Web, CLI, API und Datenbank kommen vor, d.h. alles, womit man es auch sonst so zu tun hat

# Vorraussetzungen

- Ein wenig Python kennen
	- Aber Basiswissen sollte reichen
	- Ein bisschen Django wäre auch ganz nett 😄
- Python Installation (3.11?)
- Ein Terminal
	- zsh
	- bash
	- fish

# Wer bin ich?

**Jochen Wersdörfer**

- Python Freelancer aus Düsseldorf
- Podcast Host [Python Podcast](https://python-podcast.de/show/)

# Mehr Material

**Bücher**
- [[Python Testing with pytest]]
- [[Speed Up Your Django Tests]]
- [Boost Your Django DX](https://adamchainz.gumroad.com/l/byddx)
- [Architecture Patterns with Python](https://www.cosmicpython.com/)

# In welche Richtung soll es weiter gehen?

**Dinge, die wir tun könnten**

- Mehr htmx - lassen wir eine Django-App wie eine SPA aussehen
- Deployment - wie bekommen wir unsere Django-App ins Netz? (CI/CD etc..)
- LLMs verwenden, um Toots zu generieren
- Wie dokumentiert man Software (sphinx, furo)
- Eher auf IDEs eingehen, weniger CLI
- Advanced pytest
	- Debugging
	- Dynamische Parametrisierung
	- Eigene pytest-Plugins / hook-functions
