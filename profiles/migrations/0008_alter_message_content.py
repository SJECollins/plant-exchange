# Generated by Django 4.1.2 on 2022-10-28 09:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_message_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
