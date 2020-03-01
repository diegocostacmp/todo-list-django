# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from django.db import models
import uuid


class Category(models.Model):
    name = models.CharField(max_length=100)
    uuid = models.UUIDField(
        verbose_name="Identifier unique", default=uuid.uuid4, editable=False
    )

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class TodoList(models.Model):
    uuid = models.UUIDField(
        verbose_name="Identifier unique", default=uuid.uuid4, editable=False
    )
    title = models.CharField(verbose_name="Título", max_length=250)
    created = models.DateField(
        verbose_name="Date create", auto_now_add=True, blank=True, null=True
    )
    # due_date = models.DateField(verbose_name="Deadline", default=timezone.now().strftime("%d-%m-%Y"))
    category = models.ForeignKey(
        Category, verbose_name="Category", default="geral", on_delete=models.PROTECT
    )

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
