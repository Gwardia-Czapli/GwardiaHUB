# Generated by Django 5.0.4 on 2024-05-07 20:06

import core.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserRole",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("name", models.CharField()),
                (
                    "permissions",
                    models.CharField(
                        choices=core.models.get_permission_choices, default=""
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("discord_id", models.BigIntegerField(unique=True)),
                ("username", models.CharField()),
                ("avatar_hash", models.CharField()),
                ("roles", models.ManyToManyField(to="core.userrole")),
                (
                    "data_valid_until",
                    models.DateTimeField(
                        default=datetime.datetime(
                            1971, 1, 1, 0, 0, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
            ],
        ),
    ]
