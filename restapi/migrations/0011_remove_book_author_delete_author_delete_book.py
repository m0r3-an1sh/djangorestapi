# Generated by Django 4.1.2 on 2023-04-27 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0010_remove_client_project_project_clientprojects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
