# Generated by Django 5.1.6 on 2025-02-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("relationship_app", "0004_alter_userprofile_role"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=255)),
                ("bio", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
