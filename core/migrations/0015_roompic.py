# Generated by Django 4.1 on 2022-08-24 02:34

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_sessionroom_has_projector'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to=core.models.public_room_pic_path_generator)),
                ('pic_thumbnail', models.ImageField(blank=True, null=True, upload_to=core.models.public_room_pic_path_generator)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pics', to='core.sessionroom')),
            ],
        ),
    ]
