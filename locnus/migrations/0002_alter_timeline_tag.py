# Generated by Django 4.2.1 on 2023-05-09 12:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("locnus", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timeline",
            name="tag",
            field=models.IntegerField(choices=[(1, "Public"), (2, "Local"), (3, "Home")]),
        ),
    ]
