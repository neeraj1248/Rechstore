# Generated by Django 3.0.3 on 2020-04-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('number', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=50)),
                ('ac_id', models.CharField(max_length=50)),
            ],
        ),
    ]