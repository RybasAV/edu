from .models import Courses, Category

def category_list_func(category_id):
    category_list = Category.objects.all()
    cours_list = Courses.objects.select_related("category").all()
    if category_id:
        cours_list = cours_list.filter(category_id=category_id)
    return(category_list,cours_list)