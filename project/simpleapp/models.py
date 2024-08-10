from django.db import models
from django.core.validators import MinValueValidator


# Товар для нашей витрины
class New(models.Model):
    name = models.CharField(
        max_length=50
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news', # все продукты в категории будут доступны через поле products
    )

    time_in = models.DateField()

    def __str__(self):
        return f'{self.name.title()}: {self.description[:25]}'


# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()