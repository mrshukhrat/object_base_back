# Generated by Django 4.2.6 on 2023-11-29 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_district_alter_visit_museum_delete_museum'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectsDesk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectsDesk1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectsGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
            ],
        ),
        migrations.DeleteModel(
            name='Visit',
        ),
    ]
