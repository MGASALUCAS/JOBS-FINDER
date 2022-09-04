# Generated by Django 3.1.4 on 2021-01-01 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_profile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_id', models.IntegerField()),
                ('to_id', models.IntegerField()),
                ('application_id', models.IntegerField()),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
