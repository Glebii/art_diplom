# Generated by Django 3.0.6 on 2020-06-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='mood',
            field=models.CharField(choices=[('PO', 'positive'), ('NE', 'negative'), ('MI', 'middle'), ('FR', 'frightening'), ('CL', 'calm')], max_length=25),
        ),
    ]
