import factory
from factory.django import DjangoModelFactory
from courses.models import Courses, Category


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name_category = factory.Faker("text", max_nb_chars=30)


class CoursesFactory(DjangoModelFactory):
    class Meta:
        model = Courses

    name_course = factory.Faker("text", max_nb_chars=30,locale="ru_RU")
    description_course = factory.Faker("text", max_nb_chars=600, locale="ru_RU")
    date_start_course = factory.Faker("date_this_year")
    price_course = factory.Faker("pyint", min_value=600, max_value=2700)
    category = factory.SubFactory(CategoryFactory)
