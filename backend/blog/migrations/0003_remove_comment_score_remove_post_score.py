# Generated by Django 4.0.4 on 2022-06-17 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_comments_comment_rename_posts_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='score',
        ),
        migrations.RemoveField(
            model_name='post',
            name='score',
        ),
    ]
