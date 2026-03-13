from django.db import models


class Category(models.Model):
    name_category = models.CharField("Направление курсов", max_length=30, unique=True)

    def __str__(self):
        return self.name_category


class Courses(models.Model):
    name_course = models.CharField("Название курса", max_length=30, unique=True)
    description_course = models.CharField("Описание курса", max_length=300)
    date_start_course = models.DateField("Дата начала обучения")
    price_course = models.IntegerField("Цена курса")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_course
