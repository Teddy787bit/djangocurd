# Generated by Django 3.2.13 on 2022-07-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]