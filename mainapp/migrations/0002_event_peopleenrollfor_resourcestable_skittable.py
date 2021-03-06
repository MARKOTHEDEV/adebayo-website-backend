# Generated by Django 3.2 on 2021-11-26 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=300)),
                ('event_photo', models.ImageField(upload_to='event_pictures/')),
                ('form_message', models.TextField()),
                ('email_message_confirm', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ResourcesTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_text', models.CharField(max_length=400)),
                ('blog_link', models.TextField()),
                ('heading_picture', models.ImageField(upload_to='resources/')),
            ],
        ),
        migrations.CreateModel(
            name='SkitTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_picture', models.ImageField(upload_to='skitPhotos/')),
                ('youtube_link', models.TextField()),
                ('heading_text', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='peopleEnrollfor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=300)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.event')),
            ],
        ),
    ]
