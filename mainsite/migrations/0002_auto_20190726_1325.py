# Generated by Django 2.2.3 on 2019-07-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_body',
        ),
        migrations.AddField(
            model_name='article',
            name='article_paragraph1',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='article_paragraph2',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='article_paragraph3',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='article_paragraph4',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='article_paragraph5',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='article_paragraph6',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='article_paragraph7',
            field=models.TextField(blank=True, default=''),
        ),
    ]