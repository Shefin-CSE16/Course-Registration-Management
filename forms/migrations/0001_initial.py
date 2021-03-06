# Generated by Django 2.0.2 on 2019-09-05 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField(default=1)),
                ('regno', models.IntegerField(default=1)),
                ('session', models.CharField(default='', max_length=255, null='true')),
                ('name', models.CharField(default='', max_length=255, null='true')),
                ('semester', models.CharField(default='', max_length=255, null='true')),
                ('backlog', models.TextField(default='', null='true')),
                ('courseno', models.TextField(blank=True, default='', null=True)),
                ('title', models.TextField(blank=True, default='', null=True)),
                ('credit', models.TextField(blank=True, default='', null=True)),
                ('totalcredit', models.FloatField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
