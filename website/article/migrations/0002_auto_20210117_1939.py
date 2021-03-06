# Generated by Django 3.1.5 on 2021-01-17 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='remise',
            field=models.FloatField(default=0, max_length=1000),
        ),
        migrations.AddField(
            model_name='article_images',
            name='article',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='article.article'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article_images',
            name='image',
            field=models.CharField(max_length=500),
        ),
    ]
