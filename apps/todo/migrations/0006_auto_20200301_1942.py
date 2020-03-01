# Generated by Django 3.0.3 on 2020-03-01 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0005_category_uuid"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "category", "verbose_name_plural": "categories"},
        ),
        migrations.AlterField(
            model_name="todolist",
            name="category",
            field=models.ForeignKey(
                default="geral",
                on_delete=django.db.models.deletion.PROTECT,
                to="todo.Category",
                verbose_name="Category",
            ),
        ),
        migrations.AlterField(
            model_name="todolist",
            name="created",
            field=models.DateField(
                auto_now_add=True, null=True, verbose_name="Date create"
            ),
        ),
    ]
