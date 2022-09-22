# Generated by Django 4.0.5 on 2022-09-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField(max_length=350)),
            ],
        ),
    ]
