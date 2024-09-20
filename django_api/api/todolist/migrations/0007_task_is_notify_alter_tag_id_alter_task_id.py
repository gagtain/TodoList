# Generated by Django 4.2.4 on 2024-09-19 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_task_telegram_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_notify',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.CharField(blank=True, max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.CharField(blank=True, max_length=64, primary_key=True, serialize=False),
        ),
    ]
