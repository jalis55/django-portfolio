# Generated by Django 2.0 on 2019-09-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_education_about_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicinfo',
            name='cover_pic',
            field=models.ImageField(default='', upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='full_name',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='profile_pic',
            field=models.ImageField(default='null', upload_to='pics'),
            preserve_default=False,
        ),
    ]
