# Generated by Django 4.0.3 on 2022-03-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_ptameetingresolution_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schoolmanagement',
            options={'verbose_name': 'School Management', 'verbose_name_plural': 'School Management'},
        ),
        migrations.AddField(
            model_name='schoolmanagement',
            name='title',
            field=models.CharField(blank=True, help_text='E.g: Principal, Senior Teacher', max_length=25),
        ),
    ]
