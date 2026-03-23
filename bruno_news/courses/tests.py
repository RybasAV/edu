from django.test import TestCase
from django.db import IntegrityError
from .factories import CategoryFactory, CoursesFactory
from .models import Category, Courses


class CourseTest(TestCase):

    def test_create_category(self):
        """
        Case: Проверка создания категории
        Expected: Получить имя созданной категоии, и сравнить количество
        """

        category = CategoryFactory(name_category="Python")
        self.assertEqual(category.name_category, "Python")
        self.assertEqual(Category.objects.count(), 1)

    def test_category_uniqueness(self):
        """
        Case: Проверка уникальности создаваемых имен
        Expected: Получить ошибку при попытке создания категории с существующим именем
        """

        CategoryFactory(name_category="Программирование")
        with self.assertRaises(IntegrityError):
            CategoryFactory(name_category="Программирование")

    def test_course_on_category(self):
        """
        Case: Проверка создания курсов в одной категории
        Expected: Получить имя категории
        """
        category1 = CategoryFactory(name_category="Программирование")
        courses_list = CoursesFactory.create_batch(5, category=category1)
        self.assertEqual(len(courses_list), 5)
        self.assertEqual(courses_list[0].category.name_category, "Программирование")
        self.assertEqual(Courses.objects.filter(category=category1).count(), 5)
