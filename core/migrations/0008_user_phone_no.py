# Generated by Django 4.1 on 2022-08-21 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_user_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_no',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='user', to='core.userphonenumber'),
            preserve_default=False,
        ),
    ]
