# Generated by Django 2.0.2 on 2019-10-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, null='true')),
                ('Email', models.CharField(max_length=255, null='true')),
                ('Department', models.CharField(max_length=255, null='true')),
                ('Designation', models.CharField(max_length=255, null='true')),
            ],
        ),
    ]