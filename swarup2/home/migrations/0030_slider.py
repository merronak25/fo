# Generated by Django 4.1.5 on 2023-03-23 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_chick_title_chick_image_peanut_title_peanut_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/')),
                ('Title', models.CharField(max_length=100)),
            ],
        ),
    ]
