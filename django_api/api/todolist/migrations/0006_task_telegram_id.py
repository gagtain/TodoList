# Generated by Django 4.2.4 on 2024-09-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_alter_task_dead_line_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='telegram_id',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
