# Generated by Django 3.1 on 2020-09-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_game_questionanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pointstable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('game_id', models.IntegerField()),
                ('player_id', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]