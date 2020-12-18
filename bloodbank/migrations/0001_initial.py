# Generated by Django 3.1.3 on 2020-12-17 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField()),
                ('blood_group', models.CharField(max_length=3)),
                ('phone_number', models.IntegerField(unique=True)),
                ('location', models.CharField(max_length=50)),
                ('weight', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]