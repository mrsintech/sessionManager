# Generated by Django 4.1 on 2022-08-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userphonenumber',
            name='country_code',
            field=models.CharField(default='+98', max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userphonenumber',
            name='number',
            field=models.CharField(max_length=10),
        ),
    ]
