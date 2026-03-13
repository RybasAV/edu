from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Courses, Category


def home(request):
    cours_list = Courses.objects.all()
    category_list = Category.objects.all()
    return render(
        request, "home.html", {"cours_list": cours_list, "category_list": category_list}
    )
