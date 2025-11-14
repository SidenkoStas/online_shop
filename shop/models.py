from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True) # Уникальность создаёт индексы

    class Meta:
        ordering = ("name",)
        indexes = (models.Index(fields=("name",)),)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"
    
class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products",
        verbose_name="Категория"
        )
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="products/%Y/%m/%d", blank=True, verbose_name="Изображение"
        )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True, verbose_name="Доступность")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
        )
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ("name",)
        indexes = (
            models.Index(fields=("id", "slug")),
            models.Index(fields=("name",)),
            models.Index(fields=("-created",)),
            )
    
    def __str__(self):
        return f"{self.name}"
