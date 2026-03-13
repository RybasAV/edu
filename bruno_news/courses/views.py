from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Courses, Category


def get_courses_page(request, category_id=None):

    category_list = Category.objects.all()

    if category_id:
        current_category = get_object_or_404(Category, id=category_id)
        cours_list = Courses.objects.filter(category=current_category)

    else:
         cours_list = Courses.objects.all()

    return render(
        request,
        "courses.html",
        {"cours_list": cours_list, "category_list": category_list},
    )
