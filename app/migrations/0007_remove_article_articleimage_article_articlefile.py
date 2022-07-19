# Generated by Django 4.0.2 on 2022-07-19 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_article_articleimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='articleimage',
        ),
        migrations.AddField(
            model_name='article',
            name='articlefile',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Article file'),
        ),
    ]