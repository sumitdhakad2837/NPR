# Generated by Django 3.1.4 on 2020-12-23 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201222_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='NoOfComments',
        ),
        migrations.RemoveField(
            model_name='product',
            name='NoOfDislikes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='NoOfLikes',
        ),
    ]