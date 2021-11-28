# Generated by Django 3.2.9 on 2021-11-25 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Collection_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('collection_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.collection')),
            ],
        ),
    ]