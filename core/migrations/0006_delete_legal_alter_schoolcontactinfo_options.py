# Generated by Django 4.0.3 on 2022-03-22 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_title_frequentlyaskedquestion_question_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Legal',
        ),
        migrations.AlterModelOptions(
            name='schoolcontactinfo',
            options={'verbose_name': 'School Contact Information', 'verbose_name_plural': 'School Contact Information'},
        ),
    ]