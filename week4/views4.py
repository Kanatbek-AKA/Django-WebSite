from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Course4, Lesson4, Enrollment4
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.urls import reverse
from django.views import generic, View
from collections import defaultdict
# 
from django.contrib.auth import login, logout, authenticate
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create authentication related views
def registration_request(request):
    context ={}
    if request.method == 'GET':
       return render(request, 'onlinecourse/user_registration.html', context)

    elif request.method == "POST":
       username = request.POST['username']
       firstname = request.POST['firstname']
       lastname = request.POST['lastname']
       password = request.POST['pws']

       user_exist = False

       try:
         # check if user already exists
         User.objects.get(username=username)
         user_exist = True
       except :
         logger.debug("{} is new user".format(username))

       if not user_exist:
          # Create user 
          user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, password=password)
          login(request, user)
          return redirect("onlinecourse:popular_course_list3")   # urls.py
       else:
          return render(request, 'onlinecourse/user_registration.html', context)



def login_request(request):
   context= {}
   if request.method == "POST":
      # get username and password from request.POST dictionary
      username = request.POST['username']
      password = request.POST['pws']
      # Try to check if provide credentials can be authenticated
      user = authenticate(username=username, password=password)
      if user is not None:
         # valid user call login
         login(request, user)
         return redirect('onlinecourse:popular_course_list3')
      else:
         return render(request, 'onlinecourse/user_login.html', context)
   else:
      return render(request, 'onlinecourse/user_login.html', context)


def logout_request(request):
   print("Log out the user `{}` ".format(request.user.username))
   # logout user 
   logout(request)
   return redirect("onlinecourse:popular_course_list3")   # also the name for html pages inside views


# Add a class-based course list view
class CourseListView2(generic.ListView):
    template_name = 'onlinecourse/course_list.html'
    context_object_name = 'course_list'

    def get_queryset(self):
       courses = Course4.objects.order_by('-total_enrollment')[:10]
       return courses


# Add a generic course details view
class CourseDetailsView2(generic.DetailView):
    model = Course4
    template_name = 'onlinecourse/course_detail.html'


class EnrollView2(View):
    # Handles get request
    def post(self, request, *args, **kwargs):
        course_id = kwargs.get('pk')
        course = get_object_or_404(Course4, pk=course_id)
        # Create an enrollment
        course.total_enrollment += 1
        course.save()
        return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details3', args=(course.id,)))
