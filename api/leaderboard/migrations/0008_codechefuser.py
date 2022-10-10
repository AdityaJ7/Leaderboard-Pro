# Generated by Django 3.2.4 on 2022-08-03 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0007_githubuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodechefUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('max_rating', models.PositiveIntegerField(default=0)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('last_activity', models.PositiveIntegerField(default=253402300800.0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('avatar', models.CharField(default='', max_length=256)),
            ],
            options={
                'ordering': ['-rating'],
            },
        ),
    ]