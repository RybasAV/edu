from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Courses, Category, Comment
from .services import category_list_func, get_comments
from django.views.generic import ListView, DetailView
from .forms import CommentForm


class CategoryMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


class CoursView(CategoryMixin, ListView):
    template_name = "courses.html"
    model = Courses
    paginate_by = 4
    context_object_name = "cours_list"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        self.category_list, cours_list = category_list_func(category_id)
        return cours_list


class CoursDetail(CategoryMixin, DetailView):
    model = Courses
    template_name = "cours_card.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        context["comments"] = get_comments(self.object.pk)
        return context


def Create_comment(request, cours_id):
    if request.method != "POST":
        return redirect("CoursDetail", pk=cours_id)

    form = CommentForm(request.POST)
    if form.is_valid():
        user = request.user
        is_anon = False

        if user.is_anonymous:
            user = None
            is_anon = True

        new_comment = Comment(
            name_course_id=cours_id,
            user=user,
            is_anon=is_anon,
            text=form.cleaned_data["text"],
        )
        new_comment.save()
    return redirect("CoursDetail", pk=cours_id)
