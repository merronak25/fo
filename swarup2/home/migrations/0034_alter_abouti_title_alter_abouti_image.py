# Generated by Django 4.1.5 on 2023-03-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_manage_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abouti',
            name='Title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='abouti',
            name='image',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
    ]