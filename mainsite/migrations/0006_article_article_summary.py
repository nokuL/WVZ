# Generated by Django 2.2.3 on 2019-07-31 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_article_article_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_summary',
            field=models.CharField(default='', max_length=150),
        ),
    ]