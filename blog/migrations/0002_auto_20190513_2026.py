# Generated by Django 2.1.7 on 2019-05-13 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='articel_id',
            new_name='article_id',
        ),
    ]
