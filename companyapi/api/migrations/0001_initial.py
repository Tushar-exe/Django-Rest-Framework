# Generated by Django 3.2.25 on 2024-04-19 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('Non-IT', 'Non-IT'), ('Mobile', 'Mobile')], max_length=20)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
