# Generated by Django 4.2.7 on 2023-11-10 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_post_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="slug",
        ),
    ]