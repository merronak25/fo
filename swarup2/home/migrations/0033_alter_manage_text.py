# Generated by Django 4.1.5 on 2023-03-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_alter_manage_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manage',
            name='text',
            field=models.CharField(max_length=10000),
        ),
    ]
