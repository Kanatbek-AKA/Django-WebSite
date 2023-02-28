from django.contrib import admin
from .models import Course3, Lesson3, Instructor3, Learner3


class LessonInline(admin.StackedInline):
    model = Lesson3
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Course3, CourseAdmin)
admin.site.register(Lesson3, LessonAdmin)
admin.site.register(Instructor3)
admin.site.register(Learner3)
