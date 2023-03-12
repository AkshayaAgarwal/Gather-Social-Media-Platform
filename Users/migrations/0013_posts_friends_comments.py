# Generated by Django 4.1.7 on 2023-03-12 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Users", "0012_users_table_delete_user_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Posts",
            fields=[
                ("post_id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=255)),
                ("date", models.DateField()),
                ("posts", models.FileField(upload_to="posts")),
                ("caption", models.CharField(max_length=255, null=True)),
                ("total_likes", models.BigIntegerField(default=0)),
                (
                    "email",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Users.users_table",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Friends",
            fields=[
                ("fid", models.AutoField(primary_key=True, serialize=False)),
                ("email2", models.CharField(max_length=255)),
                (
                    "email1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Users.users_table",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comments",
            fields=[
                ("cid", models.AutoField(primary_key=True, serialize=False)),
                ("category", models.CharField(max_length=255)),
                ("comment", models.CharField(max_length=255, null=True)),
                ("date", models.DateField(null=True)),
                (
                    "email",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Users.users_table",
                    ),
                ),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Users.posts"
                    ),
                ),
            ],
        ),
    ]
