# Generated by Django 3.2.12 on 2022-08-12 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationprofile',
            name='create_dt',
            field=models.DateTimeField(auto_now_add=True, default='2022-08-12 12:00:00', verbose_name='Created On'),
            preserve_default=False,
        ),
    ]
