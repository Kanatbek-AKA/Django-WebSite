from django.contrib import admin
from .models import Course4, Lesson4, Instructor4, Learner4


class LessonInline(admin.StackedInline):
    model = Lesson4
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Course4, CourseAdmin)
admin.site.register(Lesson4, LessonAdmin)
admin.site.register(Instructor4)
admin.site.register(Learner4)
