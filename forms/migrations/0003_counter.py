# Generated by Django 2.0.2 on 2019-10-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20190906_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oneOdd', models.IntegerField(default=0)),
                ('oneEven', models.IntegerField(default=0)),
                ('twoOdd', models.IntegerField(default=0)),
                ('twoEven', models.IntegerField(default=0)),
                ('threeOdd', models.IntegerField(default=0)),
                ('threeEven', models.IntegerField(default=0)),
                ('fourOdd', models.IntegerField(default=0)),
                ('fourEven', models.IntegerField(default=0)),
            ],
        ),
    ]
