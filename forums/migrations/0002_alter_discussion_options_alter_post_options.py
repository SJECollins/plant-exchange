# Generated by Django 4.1.2 on 2022-10-30 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discussion',
            options={'get_latest_by': ['created_on'], 'ordering': ['is_open']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': ['created_on'], 'ordering': ['created_on']},
        ),
    ]