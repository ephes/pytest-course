# Pytest Workshop

## Installation

### Python

Maybe this [setting up python](https://wersdoerfer.de/blogs/ephes_blog/django-beginner-series-python/)
article is helpful.

### Dependencies

Install the dependencies with pip:

```bash
python -m pip install -r requirements.txt
```

### pre-commit

Install the pre-commit hooks:

```bash
python -m pip install pre-commit
pre-commit install
```

### Django Example Project

To create the Django example project, run:

```bash
django-admin startproject locnus
cd locnus
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
