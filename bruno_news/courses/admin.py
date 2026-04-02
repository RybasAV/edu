from django.contrib import admin
from .models import Category, Courses, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Courses)


@admin.register(Comment)
class CommentModel(admin.ModelAdmin):
    list_display = (
        "name_course",
        "user",
        "text",
        "is_anon",
        "created_at",
        "updated_at",
    )
