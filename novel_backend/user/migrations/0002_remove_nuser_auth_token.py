# Generated by Django 4.1 on 2024-03-14 05:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="nuser",
            name="auth_token",
        ),
    ]
