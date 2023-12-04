# Generated by Django 4.2.6 on 2023-11-29 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_objectsdesk_objectsdesk1_objectsgoal_objecttype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objects_main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('number', models.CharField(blank=True, max_length=100, null=True)),
                ('work_time', models.CharField(blank=True, max_length=100, null=True)),
                ('images', models.ImageField(help_text='Rasmi', null=True, unique=True, upload_to='files/covers')),
                ('lat', models.CharField(max_length=100)),
                ('lng', models.CharField(max_length=100)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]