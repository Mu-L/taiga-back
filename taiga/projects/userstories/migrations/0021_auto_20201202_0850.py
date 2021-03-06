# Generated by Django 2.2.14 on 2020-12-02 08:50

from django.db import migrations, models
import taiga.base.utils.time


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0020_userstory_swimlane'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='backlog_order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_mics, verbose_name='backlog order'),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='kanban_order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_mics, verbose_name='kanban order'),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='sprint_order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_mics, verbose_name='sprint order'),
        ),
    ]
