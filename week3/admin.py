from django.contrib import admin
from .models import Course3, Lesson3, Instructor3, Learner3


class LessonInline3(admin.StackedInline):
    model = Lesson3
    extra = 5


# Register your models here.
class CourseAdmin3(admin.ModelAdmin):
    inlines = [LessonInline3]
    list_display = ("name", "pub_date")
    list_filter = ["pub_date"]
    search_fields = ["name", "description"]


class LessonAdmin3(admin.ModelAdmin):
    list_display = ["title"]


admin.site.register(Course3, CourseAdmin3)
admin.site.register(Lesson3, LessonAdmin3)
admin.site.register(Instructor3)
admin.site.register(Learner3)
