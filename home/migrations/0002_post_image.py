# Generated by Django 4.0.1 on 2022-03-20 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=123, upload_to=''),
            preserve_default=False,
        ),
    ]
