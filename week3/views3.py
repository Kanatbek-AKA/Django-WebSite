from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course3, Lesson3, Enrollment3
from django.urls import reverse
from django.views import generic, View
from django.http import Http404

# Create your class based views here.
# class CourseListView(generic.ListView):
#       # generic build-in views
#       template_view = 'onlinecourse/course_list_three.html'  # 
#       context_object_name = 'course_list'
#       # provide list objects
#       def get_queryset(self):
#           courses = Course3.objects.order_by('-total_enrollment')[:10] # 
#           return courses

# #     # handles get request
# #     def get(self, request):
# #         context ={}
# #         course_list = Course.objects.order_by("-total_enrollment")[:10]
# #         context["course"]= course_list
# #         return render(request, 'onlinecourse/course_list.html', context)


# class CourseEnrollView(View):
#     # handle post
#     def post(self, request, *args, **kwargs):
#        course_id = kwargs.get('pk')
#        course = get_object_or_404(Course3, pk=course_id)
#        #  Increase total by 1
#        course.total_enrollment += 1
#        course.save()
#        return HttpResponseRedirect(reverse(viewname='lab3:course_details2', args=(course.id,)))



# class CourseDetailsView(generic.DetailView):
#       model = Course3
#       template_view = 'onlinecourse/course_detail_three.html'


#   # handle get method
#   def get(self, request, *args, **kwargs):
#      context = {}
#      # get url param pk from keyword argument list as course_id
#      course_id = kwargs.get('pk')
#      try:
#          course = Course.objects.get(pk=course_id)
#          context['course'] = course
#          return render(request, 'onlinecourse/course_detail_three.html', context)
#      except Course.DoesNotExist:
#          raise Http404("No course matches the given id.")


# Function based views
# Function-based course list view
def popular_course_list_Changed(request):
   context3 = {}
   if request.method == 'GET':
       course_list3 = Course3.objects.order_by('-total_enrollment')[:10]
       context3['course_list3'] = course_list3
       return render(request, 'onlinecourse/course_list_three.html', context3)

# Function-based course_details view
def course_details__Changed(request, course3_id):
   context3 = {}
   if request.method == 'GET':
       try:
           course3 = Course3.objects.get(pk=course3_id)
           context3['course3'] = course3
           return render(request, 'onlinecourse/course_detail_three.html', context3)
       except Course3.DoesNotExist:
           raise Http404("No course matches the given id.")

# Function-based enroll view
def enroll_Changed(request, course3_id):
   if request.method == 'POST':
      course3 = get_object_or_404(Course3, pk=course3_id)
      # Create an enrollment
      course3.total_enrollment += 1
      course3.save()
      return HttpResponseRedirect(reverse(viewname='lab3:course_details2', args=(course3.id,)))
