# Generated by Django 4.2.4 on 2023-09-06 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0002_team_rename_created_by_project_created_by_user_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Team_User',
        ),
    ]
