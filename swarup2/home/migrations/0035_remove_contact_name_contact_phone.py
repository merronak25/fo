# Generated by Django 4.1.5 on 2023-03-26 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_alter_abouti_title_alter_abouti_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
