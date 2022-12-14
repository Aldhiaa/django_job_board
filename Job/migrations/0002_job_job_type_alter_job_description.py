# Generated by Django 4.1 on 2022-08-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('full type', 'full type'), ('part type', 'part type')], default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
