# Generated by Django 4.0.1 on 2022-03-24 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to='post/images/%Y/%m/%d/%H/'),
        ),
    ]
