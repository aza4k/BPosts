# Generated by Django 4.2.7 on 2023-11-15 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
