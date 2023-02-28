from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course5, Lesson5, Instructor5, Learner5, Question5, Choice5

# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInLine(admin.StackedInline):
    model = Question5
    extra = 5                    # Test
    
class ChoiceInline(admin.StackedInline):
    model = Choice5 
    extra = 3                    # Test

class LessonInline(admin.StackedInline):
    model = Lesson5
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here
admin.site.register(Question5)  #
admin.site.register(Choice5)    # 
admin.site.register(Course5, CourseAdmin)
admin.site.register(Lesson5, LessonAdmin)
admin.site.register(Instructor5)
admin.site.register(Learner5)
