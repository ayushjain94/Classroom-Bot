# Generated by Django 3.1 on 2020-09-12 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_merge_20200912_0254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='group_num',
            new_name='group_number',
        ),
        migrations.AlterField(
            model_name='course',
            name='bot_token',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='workspace_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('group_number', 'registered_course_id')},
        ),
        migrations.RemoveField(
            model_name='group',
            name='project_name',
        ),
    ]