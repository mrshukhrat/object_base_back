# Generated by Django 4.2.6 on 2023-11-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_menu_museum_visit_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Title')),
            ],
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
