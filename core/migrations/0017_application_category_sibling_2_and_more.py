# Generated by Django 4.0.3 on 2022-07-16 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_application_category_sibling_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='category_sibling_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='category_sibling_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='dob_sibling_2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='dob_sibling_3',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='gender_sibling_2',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='gender_sibling_3',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='sibling_class_2',
            field=models.CharField(blank=True, choices=[('C1', 'Creche One'), ('C2', 'Creche Two'), ('C3', 'Creche Three'), ('N1', 'Nursery One'), ('N2', 'Nursery Two'), ('N3', 'Nursery Three'), ('P1', 'Primary One'), ('P2', 'Primary Two'), ('P3', 'Primary Three'), ('P4', 'Primary Four'), ('P5', 'Primary Five'), ('P6', 'Primary Six')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='sibling_class_3',
            field=models.CharField(blank=True, choices=[('C1', 'Creche One'), ('C2', 'Creche Two'), ('C3', 'Creche Three'), ('N1', 'Nursery One'), ('N2', 'Nursery Two'), ('N3', 'Nursery Three'), ('P1', 'Primary One'), ('P2', 'Primary Two'), ('P3', 'Primary Three'), ('P4', 'Primary Four'), ('P5', 'Primary Five'), ('P6', 'Primary Six')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='sibling_name_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='sibling_name_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
