# Pytest Workshop

## Installation

### Python

Maybe this [setting up python](https://wersdoerfer.de/blogs/ephes_blog/django-beginner-series-python/)
article is helpful.

### Clone Repository

```shell
git clone git@github.com:ephes/pytest-course.git
cd pytest-course
```

### Create Virtualenv

```shell
python -m pip install virtualenv
python -m virtualenv --prompt . venv
source venv/bin/activate  # bash and zsh
# source venv/bin/activate.fish
```

### Install pytest

```shell
python -m pip install pytest
```

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
django-admin startproject --template https://github.com/ephes/django-template/releases/download/v0.1.6/project_template.zip locnus
cd locnus
mkdir apps
cd apps
../manage.py startapp --template https://github.com/ephes/django-template/releases/download/v0.1.6/app_template.zip client
touch __init__.py
cd ..
python commands.py sync
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
