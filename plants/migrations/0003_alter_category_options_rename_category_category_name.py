# Generated by Django 4.1.2 on 2022-10-26 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_rename_wants_plant_will_trade_for_alter_plant_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]