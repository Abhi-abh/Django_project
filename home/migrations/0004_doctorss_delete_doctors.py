# Generated by Django 5.1.1 on 2024-10-12 06:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_doctors"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctorss",
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
                ("doc_name", models.CharField(max_length=255)),
                ("doc_spec", models.CharField(max_length=255)),
                ("doc_image", models.ImageField(upload_to="doctors")),
                (
                    "dep_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.departments",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="doctors",
        ),
    ]
