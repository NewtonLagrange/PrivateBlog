# Generated by Django 2.2 on 2019-04-25 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190424_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='toc',
            field=models.TextField(null=True),
        ),
    ]
