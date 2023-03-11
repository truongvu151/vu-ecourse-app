from django.contrib import admin
from django import forms
from django.utils.html import mark_safe
from .models import Category, Course, Lesson, Tag

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BaseAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    list_filter = ['id', 'subject', 'created_date']
    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe("<img src='/static/{}' width='120' />".format(obj.image.name))


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class TagInlineAdmin(admin.StackedInline):
    model = Lesson.tags.through
    
class CourseAdmin(BaseAdmin):
    list_display = ['id', 'subject', 'created_date', 'active']

    form = CourseForm


class LessonAdmin(BaseAdmin):
    list_display = ['id', 'subject', 'created_date', 'content']
    inlines = [TagInlineAdmin, ]
    form = LessonForm


# Register your models here.
admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)
