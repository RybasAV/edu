from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_courses_page, name="courses"),
    path('category/<int:category_id>/', views.get_courses_page, name='category_filter'),
]
