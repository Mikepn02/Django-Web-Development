# Generated by Django 4.2.5 on 2023-09-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Room",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("create", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
