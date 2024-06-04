# Generated by Django 5.0.6 on 2024-06-04 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Size",
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
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Shawarma",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=15)),
                ("ingredient1", models.CharField(max_length=100)),
                ("ingredient2", models.CharField(max_length=100)),
                (
                    "special_request",
                    models.CharField(
                        blank=True,
                        help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
                        max_length=300,
                        null=True,
                    ),
                ),
                (
                    "size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shawarma.size"
                    ),
                ),
            ],
        ),
    ]
