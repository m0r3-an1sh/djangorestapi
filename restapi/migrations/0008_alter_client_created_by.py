# Generated by Django 4.1.2 on 2023-04-26 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0007_alter_client_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created_by',
            field=models.CharField(max_length=255),
        ),
    ]