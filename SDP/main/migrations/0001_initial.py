# Generated by Django 5.1.1 on 2024-10-05 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeniorDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_abbreviation', models.CharField(max_length=4)),
                ('Location', models.CharField(max_length=100)),
                ('Poster_tittle', models.CharField(max_length=100)),
                ('Abstract', models.TextField()),
                ('num_team_members', models.IntegerField()),
                ('team_member_names', models.CharField(max_length=100)),
                ('Need_power', models.BooleanField(default=False)),
                ('two_outlets', models.BooleanField(default=False)),
                ('table', models.BooleanField(default=False)),
                ('foamboard', models.BooleanField(default=False)),
                ('clips', models.BooleanField(default=False)),
                ('large_presentaion', models.BooleanField(default=False)),
                ('sponsor_logos', models.BooleanField(default=False)),
                ('picutures', models.BooleanField(default=False)),
            ],
        ),
    ]
