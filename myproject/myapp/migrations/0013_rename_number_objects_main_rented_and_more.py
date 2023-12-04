# Generated by Django 4.2.7 on 2023-11-30 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_objects_main_object_desk1_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objects_main',
            old_name='number',
            new_name='Rented',
        ),
        migrations.RenameField(
            model_name='objects_main',
            old_name='status',
            new_name='area',
        ),
        migrations.RenameField(
            model_name='objects_main',
            old_name='work_time',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='objects_main',
            name='description',
        ),
        migrations.AddField(
            model_name='objects_main',
            name='contracts',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='objects_main',
            name='contracts_file',
            field=models.FileField(help_text='Shartnoma', null=True, unique=True, upload_to='.'),
        ),
        migrations.AddField(
            model_name='objects_main',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='objects_main',
            name='electricity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='objects_main',
            name='gas',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='objects_main',
            name='k_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='objects_main',
            name='marked',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='objects_main',
            name='object_age',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='objects_main',
            name='regions',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='objects_main',
            name='surface',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='objects_main',
            name='water',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]