# Generated by Django 3.2 on 2021-12-11 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_detail',
            field=models.TextField(default='..'),
        ),
        migrations.CreateModel(
            name='TargetAudience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=250)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.event')),
            ],
        ),
        migrations.CreateModel(
            name='exampleOfTargetAudience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('target_audience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.targetaudience')),
            ],
        ),
    ]
