# Generated by Django 4.0.2 on 2022-07-19 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_article_explanation_alter_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='articleimage',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Article Image'),
        ),
    ]