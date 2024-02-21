# Generated by Django 5.0.2 on 2024-02-21 07:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UniformResourceLocator",
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
                ("original_url", models.URLField()),
                ("shortened_url", models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
