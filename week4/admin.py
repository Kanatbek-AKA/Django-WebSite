from django.contrib import admin
from .models import Course4, Lesson4, Instructor4, Learner4


class LessonInline4(admin.StackedInline):
    model = Lesson4
    extra = 5


# Register your models here.
class CourseAdmin4(admin.ModelAdmin):
    inlines = [LessonInline4]
    list_display = ("name", "pub_date")
    list_filter = ["pub_date"]
    search_fields = ["name", "description"]


class LessonAdmin4(admin.ModelAdmin):
    list_display = ["title"]


admin.site.register(Course4, CourseAdmin4)
admin.site.register(Lesson4, LessonAdmin4)
admin.site.register(Instructor4)
admin.site.register(Learner4)
