# Generated by Django 2.2 on 2019-04-24 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_paper_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='paper',
        ),
        migrations.AddField(
            model_name='paper',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
