# Generated by Django 4.2.7 on 2023-11-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_userdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='adress',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='image',
            field=models.ImageField(default='image-2282302_960_720.png', null=True, upload_to='profile_img'),
        ),
    ]