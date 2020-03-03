# Generated by Django 3.0.3 on 2020-03-03 00:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Identifier unique')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Identifier unique')),
                ('title', models.CharField(max_length=250, verbose_name='Título')),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Date create')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='todo.Category', verbose_name='Category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
