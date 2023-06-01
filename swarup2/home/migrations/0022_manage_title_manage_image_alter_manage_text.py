# Generated by Django 4.1.5 on 2023-03-21 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_chick_title_chicki_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='manage',
            name='Title',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manage',
            name='image',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='manage',
            name='text',
            field=models.CharField(max_length=10000),
        ),
    ]
