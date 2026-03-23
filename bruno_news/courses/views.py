from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Courses, Category
from .services import category_list_func


def get_courses_page(request, category_id=None):
    category_list,cours_list=category_list_func(category_id)

    return render(
        request,
        "courses.html",
        {"cours_list": cours_list, "category_list": category_list},
    )
