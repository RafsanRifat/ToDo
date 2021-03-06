# Generated by Django 3.2.9 on 2021-11-25 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20211125_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='collection',
        ),
        migrations.AddField(
            model_name='collection',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todolist.task'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='collection_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.TextField(null=True),
        ),
    ]
