# Generated by Django 4.1.5 on 2023-03-15 05:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_manage_remark_alter_manage_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manage',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
