# Generated by Django 3.0.6 on 2020-09-05 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentmarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('maths', models.IntegerField()),
                ('english', models.IntegerField()),
                ('hindi', models.IntegerField()),
                ('social_science', models.IntegerField()),
                ('science', models.IntegerField()),
            ],
        ),
    ]
