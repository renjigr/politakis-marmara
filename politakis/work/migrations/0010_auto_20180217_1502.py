# Generated by Django 2.0.2 on 2018-02-17 15:02

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0009_workmodel_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workmodel',
            name='image1',
            field=models.ImageField(upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='workmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='workmodel',
            name='thumbnail',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='thumbanail/%Y/%m/%d', verbose_name='thumbnail'),
        ),
    ]
