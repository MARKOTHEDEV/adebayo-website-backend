# Generated by Django 3.2 on 2021-12-08 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_quotes_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_how_can_help',
            field=models.BooleanField(default=False),
        ),
    ]
