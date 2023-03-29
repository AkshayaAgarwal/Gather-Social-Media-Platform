# Generated by Django 4.1.7 on 2023-03-21 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Users", "0013_posts_friends_comments"),
    ]

    operations = [
        migrations.CreateModel(
            name="Requests",
            fields=[
                ("rid", models.AutoField(primary_key=True, serialize=False)),
                ("email2", models.CharField(max_length=255)),
                ("status", models.CharField(default="unconfirmed", max_length=255)),
                (
                    "email1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Users.users_table",
                    ),
                ),
            ],
        ),
    ]