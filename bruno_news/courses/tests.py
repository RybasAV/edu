from django.test import TestCase
from django.db import IntegrityError
from .factories import CategoryFactory, CoursesFactory
from .models import Category, Courses
from .services import category_list_func


class CourseTest(TestCase):

    def test_category_list_func(self):
        """
        Case: Проверка работы функции получения списка курсов
        Expected: Получить верный список курсов в зависимости от запроса
        """
        category1 = CategoryFactory(name_category="Программирование")
        category2 = CategoryFactory(name_category="Дизайн")
        courses_list = CoursesFactory.create_batch(4, category=category1)
        courses_list = CoursesFactory.create_batch(5, category=category2)

        self.assertEqual(len(category_list_func()[1]), 9)
        self.assertEqual(len(category_list_func(1)[1]), 4)
        self.assertEqual(len(category_list_func(2)[1]), 5)
        self.assertEqual(category_list_func(1)[1][0].category.name_category, "Программирование")
        self.assertEqual(category_list_func(2)[1][0].category.name_category, "Дизайн")
