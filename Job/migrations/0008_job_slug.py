# Generated by Django 4.1 on 2022-08-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0007_alter_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]