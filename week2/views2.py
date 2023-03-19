from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

# Load defined models
from .models import Course2, Lesson2, Enrollment2

#
from django.urls import reverse
from django.views import generic
from django.http import Http404

# generic view
# from django.views.generic import TemplateView


def popular_course_list(request):
    context2 = {}
    if request.method == "GET":
        # Using the object model manage to read all course list and sort them by total_enrollment descending
        course_list2 = Course2.objects.order_by("-total_enrollment")[
            :10
        ]  # descending order slice 10 values
        # Append the course list as an entry of context dictionary
        context2["course_list2"] = course_list2
        # Indicate the html file path with param and context
        return render(request, "onlinecourse/course_list.html", context2)


# Form enroll
def enroll(request, course2_id):
    if request.method == "POST":
        # try & except if course could be found
        course2 = get_object_or_404(Course2, pk=course2_id)
        # Increase the enrollment
        course2.total_enrollment += 1
        course2.save()
        # return HttpResponseRedirect(reverse(viewname= 'onlinecourse:popular_course_list'))
        return HttpResponseRedirect(
            reverse(viewname="lab2:course_details", args=(course2.id,))
        )


# Course_detail.html
def course_details(request, course2_id):
    context2 = {}
    if request.method == "GET":
        try:
            course2 = Course2.objects.get(pk=course2_id)
            context2["course2"] = course2
            # use render method to generate HTML page by combining tamplate amd context
            return render(request, "onlinecourse/course_detail.html", context2)
        except Course2.DoesNotExist:
            raise Http404("No course matches the given id.")
