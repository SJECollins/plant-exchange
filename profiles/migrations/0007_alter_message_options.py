# Generated by Django 4.1.2 on 2022-10-27 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_message_trashed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['read', '-created_on']},
        ),
    ]
