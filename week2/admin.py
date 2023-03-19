from django.contrib import admin
from .models import Course2, Lesson2, Instructor2, Learner2


class LessonInline(admin.StackedInline):
    model = Lesson2
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ("name", "pub_date")
    list_filter = ["pub_date"]
    search_fields = ["name", "description"]


class LessonAdmin(admin.ModelAdmin):
    list_display = ["title"]


admin.site.register(Course2, CourseAdmin)
admin.site.register(Lesson2, LessonAdmin)
admin.site.register(Instructor2)
admin.site.register(Learner2)
