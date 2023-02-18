from django.contrib import admin
from .models import Category, Course

# class CourseAdmin(admin.ModelAdmin):


# Register your models here.
admin.site.register(Category)
admin.site.register(Course)