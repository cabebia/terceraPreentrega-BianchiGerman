# Generated by Django 4.2.6 on 2023-11-01 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_subtitle_alter_blogpost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='postdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
