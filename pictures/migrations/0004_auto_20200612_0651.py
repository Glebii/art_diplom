# Generated by Django 3.0.6 on 2020-06-12 06:51

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0003_auto_20200612_0554'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='painter',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='picture',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='trend',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
