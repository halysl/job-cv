# Generated by Django 2.0.5 on 2018-06-01 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jianli', '0002_auto_20180601_0337'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AlterField(
            model_name='cv',
            name='edu',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='cv',
            name='project_experience',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='cv',
            name='skill',
            field=models.CharField(max_length=2000),
        ),
        migrations.DeleteModel(
            name='Edu',
        ),
        migrations.DeleteModel(
            name='PE',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]