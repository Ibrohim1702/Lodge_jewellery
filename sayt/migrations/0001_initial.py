# Generated by Django 4.2.2 on 2023-07-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=128)),
                ('message', models.TextField()),
            ],
        ),
    ]
