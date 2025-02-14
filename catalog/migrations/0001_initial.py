# Generated by Django 5.1.3 on 2024-12-05 15:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название категории",
                        max_length=100,
                        verbose_name="Название категории",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание продукта",
                        verbose_name="Описание продукта",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название продукта",
                        max_length=100,
                        verbose_name="Название продукта",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание продукта",
                        verbose_name="Описание продукта",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрзите фото продукта",
                        null=True,
                        upload_to="catalog/image",
                        verbose_name="Фото продукта",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        help_text="Введите категорию",
                        max_length=100,
                        verbose_name="Категория",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MaxValueValidator(10000)],
                        verbose_name="Цена за продукт",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату создания",
                        null=True,
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату последнего изменения",
                        null=True,
                        verbose_name="дата последнего изменения",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
