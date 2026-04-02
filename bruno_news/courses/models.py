from django.db import models


class Category(models.Model):
    name_category = models.CharField("Направление курсов", max_length=30, unique=True)

    def __str__(self):
        return self.name_category


class Courses(models.Model):
    name_course = models.CharField("Название курса", max_length=30, unique=True)
    description_course = models.CharField("Описание курса", max_length=600)
    date_start_course = models.DateField("Дата начала обучения")
    price_course = models.IntegerField("Цена курса")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )

    def __str__(self):
        return self.name_course


class Comment(models.Model):
    name_course = models.ForeignKey(
        "Courses", on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True, related_name="comments"
    )
    text = models.TextField("Текст отзыва", max_length=300)
    is_anon = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def username(self):
        return self.user.username if self.user is not None else "Анонимный пользователь"


    def save(self, *args, **kwargs):
        if self.user is None:
            self.is_anon = True
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name_course.name_course}/{self.username}"
