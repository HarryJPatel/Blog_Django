# Generated by Django 3.1.3 on 2021-03-10 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_poster',
            new_name='date_posted',
        ),
    ]
