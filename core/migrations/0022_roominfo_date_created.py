# Generated by Django 4.1 on 2022-08-24 22:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_rename_ikey_roominfo_key_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='roominfo',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserve',
            name='title',
            field=models.CharField(default='tst', max_length=255),
            preserve_default=False,
        ),
    ]
