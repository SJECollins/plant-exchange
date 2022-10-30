# Generated by Django 4.1.2 on 2022-10-30 15:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plantblog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='BlogPost',
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'get_latest_by': ['created_on'], 'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'get_latest_by': ['created_on'], 'ordering': ['created_on']},
        ),
    ]