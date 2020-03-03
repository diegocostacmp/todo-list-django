# Generated by Django 3.0.3 on 2020-02-29 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={"verbose_name": "Categoria", "verbose_name_plural": "Categorias",},
        ),
        migrations.CreateModel(
            name="TodoList",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("content", models.TextField(blank=True)),
                ("created", models.DateField(default="29-02-2020")),
                ("due_date", models.DateField(default="29-02-2020")),
                (
                    "category",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="todo.Category",
                    ),
                ),
            ],
            options={"ordering": ["-created"],},
        ),
    ]
