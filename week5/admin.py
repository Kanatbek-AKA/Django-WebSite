from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course5, Lesson5, Instructor5, Learner5, Question5, Choice5, Submission5, examGrades5

# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInLine5(admin.StackedInline):
    model = Question5
    extra = 6                    
    
class ChoiceInline5(admin.StackedInline):
    model = Choice5
    extra = 3

class LessonInline5(admin.StackedInline):
    model = Lesson5
    extra = 5
        
# Additional 
class ExameGradeInline5(admin.StackedInline):
    list_display = ['course5', 'exam_question', 'exam_answer', 'grade']
    model = examGrades5
        
    
# Register your models here.
@admin.register(Course5)                       # define register of Course here using @
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline5]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

@admin.register(Lesson5)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here
admin.site.register(Question5)  #
admin.site.register(Choice5)    # 
# admin.site.register(Course, CourseAdmin)     # Or define register of Course here
# admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor5)
admin.site.register(Learner5)
#
admin.site.register(examGrades5)
