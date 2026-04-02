from django.urls import path
from . import views


urlpatterns = [
    path("", views.CoursView.as_view(), name="courses"),
    path('category/<int:category_id>/', views.CoursView.as_view(), name='category_filter'),
    path('<int:pk>/', views.CoursDetail.as_view(), name='CoursDetail'),
    path('courses/<int:cours_id>/add_comment', views.Create_comment, name='Cours_add_comment')
]
