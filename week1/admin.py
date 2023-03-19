from django.contrib import admin
# from .models import Course, Instructor, Lesson

# # Associate related models a way to add Inline objects on a single model managing page
# class LessonInline(admin.StackedInline):        # <<--
#     model = Lesson
#     extra = 5


# # Customize adminSite: to select the field to be included, we create a ModelAdmin class and add fields list
# class CourseAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'name', 'description']  # you only add fields that you defined in models, otherwise re-write  models to add mode fields
#     inlines = [LessonInline]                      # <<--


# # Practice 
# class InstructorAdmin(admin.ModelAdmin):
#     fields= ['user', 'full_time']


# # Once you registered admin create managing pages  Course & Instructor
# admin.site.register(Course, CourseAdmin)  
# admin.site.register(Instructor, InstructorAdmin) 
# admin.site.register(Lesson)
