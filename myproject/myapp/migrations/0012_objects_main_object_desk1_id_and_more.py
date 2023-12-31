# Generated by Django 4.2.7 on 2023-11-30 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_rename_category_district_regions_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='objects_main',
            name='object_desk1_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='myapp.objectsdesk1'),
        ),
        migrations.AddField(
            model_name='objects_main',
            name='object_desk_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='myapp.objectsdesk'),
        ),
        migrations.AddField(
            model_name='objects_main',
            name='object_goal_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='myapp.objectsgoal'),
        ),
        migrations.AddField(
            model_name='objects_main',
            name='object_type_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='myapp.objecttype'),
        ),
    ]
