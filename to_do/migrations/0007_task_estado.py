# Generated by Django 4.2.4 on 2023-09-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0006_remove_task_task_assigned_to_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='estado',
            field=models.CharField(default='En desarrollo', max_length=13),
        ),
    ]
