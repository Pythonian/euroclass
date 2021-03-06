# Generated by Django 4.0.3 on 2022-03-31 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('pupil_class', models.CharField(choices=[('N1', 'Nursery One'), ('N2', 'Nursery Two'), ('N3', 'Nursery Three'), ('P1', 'Primary One'), ('P2', 'Primary Two'), ('P3', 'Primary Three'), ('P4', 'Primary Four'), ('P5', 'Primary Five'), ('P6', 'Primary Six')], max_length=2, verbose_name='Class')),
                ('image', models.ImageField(upload_to='application')),
                ('date_of_birth', models.DateField()),
                ('date_of_registration', models.DateField(blank=True, null=True)),
                ('parent_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(blank=True, max_length=13, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('home_address', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Caution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_caution', models.DateField()),
                ('reason', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('pupil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pupil.pupil')),
            ],
        ),
    ]
