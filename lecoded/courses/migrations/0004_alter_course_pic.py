# Generated by Django 5.1.1 on 2024-09-29 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_lesson_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Course picture'),
        ),
    ]
