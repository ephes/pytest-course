# Installation und erste Tests 14:00 - 14:30

## Python Package + Abhängigkeiten

Installation von `flit` und Installation des locnus-Pakets.

```shell
python -m pip install flit
flit install -s # symlink - similar to pip install -e
pip list | grep pytest-django # verify it worked
du -ch venv | tail -2 # biggish, eh?
```

## Django Example Applikation

```shell
cd example
python manage.py migrate # Migrationen ausführen
python manage.py createsuperuser # User für Django Admin erzeugen
python manage.py runserver
```

Danach sollte der Entwicklungsserver laufen.

## Fixtures und Marker

Nur soweit, wie man zum Verstehen der Django-Tests braucht.

### Fixtures

```python
import pytest


class Server:
	def __init__(self, url):
		self.url = url


@pytest.fixture
def server():
	return Server("https://example.com")


def test_example_server(server):
	assert "foo" in server.url
```

### Marker

```python
@pytest.mark.slow  
def test_marked_slow():  
	import time  
	time.sleep(1)
```

## Viewtests

Source: [[Erste View-Tests]]

```shell
pytest # nicht vergessen, DJANGO_SETTINGS_MODULE in pyproject.toml zu setzen!
```

- Erklären wie das mit dem context funktioniert
- Man könnte auch `HTTPStatus.ok` statt 200 verwenden, mache ich aber nicht!

## Formulartests

Wir fangen nicht mit views an, weil es da schon ein etwas komisches Detail gibt, das dann zur Überleitung in den nächsten Teil genutzt werden kann. Ok, bei Formularen haben wir jetzt auch schon einen Marker dran, das ist auch komisch 😬.

**Source**: [[Erste Formular-Tests]]


# Übung 3 14:30 - 15:15

1. Schreibe einen Test, der eine Fixture verwendet
2. Markiere einen Test mit einem nicht eingebauten Marker und lasse nur den Laufen
3. Schreibe einen Test für das AccountForm, der sicherstellt, dass `form.is_valid` False ist, wenn die Eingabedaten falsch sind
4. Schreibe einen Test, der dafür sorgt, dass ein ordentlicher 404-Status zurückkommt, wenn eine Server-ID angegeben wird, die es nicht gibt


# Kleine Pause 15:15 - 15:30

# Model-Tests 15:30 - 16:00

```python
import pytest  
  
from locnus import models  
  
  
@pytest.fixture()  
def client():  
	return models.Client(name="test_client")  
  
  
def test_server_with_client(client):  
	server = models.Server(api_base_url="https://example.com", client=client)  
	assert server.client.name == client.name


@pytest.mark.django_db  
def test_server_got_saved(client):  
	server = models.Server(api_base_url="https://example.com", client=client)  
	server.client.save()  
	server.save()  
	assert server.id is not None  
	assert models.Server.objects.count() == 1
```


# Übung 4 16:00 - 16:45

1. Schreibe einen Test, der sicherstellt, dass sich ein Account nur erstellen lässt,  wenn server gesetzt ist
2. Schreibe eine Fixture für server und teste, dass die Anzahl der Accounts 1 beträgt, wenn man einen Account in der Datenbank speichert
3. Bonus: Schreibe einen Formulartest, der einen Server in der Datenbank speichert

Source: [[Übung 4 - Lösungen]]

# Fixture Scopes und Conftest 16:45 - 17:15

# Fragen, noch eine Übung? 17:15 - 18:00
