from django.shortcuts import render
from django.http import (
    HttpResponseRedirect,
    HttpResponse,
    HttpResponsePermanentRedirect,
)

#
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, logout, authenticate
import logging

# <HINT> Import any new Models here
from .models import (
    Course5,
    Enrollment5,
    Submission5,
    examGrades5,
    Question5,
    Choice5,
    Learner5,
    Instructor5,
)

#
# from django.core.mail import send_mail, BadHeaderError, EmailMessage, mail
# To avoid csrg_token
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Get an instance of a logger
logger = logging.getLogger(__name__)


def registration_request(request):
    context5 = {}
    if request.method == "GET":
        return render(
            request, "onlinecourse/user_registration_bootstrap.html", context5
        )
    elif request.method == "POST":
        # Check if user exists
        username = request.POST["username"]
        password = request.POST["psw"]
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
            login(request, user)
            return redirect("lab5:index")
        else:
            context5["message"] = "User already exists."
            return render(
                request, "onlinecourse/user_registration_bootstrap.html", context5
            )


def login_request(request):
    context5 = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["psw"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("lab5:index")
        else:
            context5["message"] = "Invalid username or password."
            return render(request, "onlinecourse/user_login_bootstrap.html", context5)
    else:
        return render(request, "onlinecourse/user_login_bootstrap.html", context5)


def logout_request(request):
    logout(request)
    return redirect("lab5:index")


def check_if_enrolled(user, course5):
    is_enrolled = False
    if user.id is not None:
        # Check if user enrolled
        num_results = Enrollment5.objects.filter(user=user, course=course5).count()
        if num_results > 0:
            is_enrolled = True
    return is_enrolled


# CourseListView
class CourseListView3(generic.ListView):
    template_name = "onlinecourse/course_list_bootstrap.html"
    context_object_name = "course_list5"

    def get_queryset(self):
        user = self.request.user
        courses5 = Course5.objects.order_by("-total_enrollment")[:10]
        for course in courses5:
            if user.is_authenticated:
                course.is_enrolled = check_if_enrolled(user, course)
        return courses5


class CourseDetailView3(generic.DetailView):
    model = Course5
    template_name = "onlinecourse/course_detail_bootstrap.html"


def enroll5(request, course5_id):
    course5 = get_object_or_404(Course5, pk=course5_id)
    user = request.user

    is_enrolled = check_if_enrolled(user, course5)
    if not is_enrolled and user.is_authenticated:
        Enrollment5.objects.create(user=user, course=course5, mode="honor")
        course5.total_enrollment += 1
        course5.save()

    return HttpResponseRedirect(
        reverse(viewname="lab5:course_detailsF", args=(course5.id,))
    )


#
# @csrf_exempt
def submit5(request, course5_id):
    user = request.user
    course5 = get_object_or_404(Course5, pk=course5_id)
    enrollment = Enrollment5.objects.get(user=user, course=course5)
    submission = Submission5.objects.create(enrollment=enrollment)
    try:
        get_result = extract_answers(request)
        submission.choices.set(get_result)
        return HttpResponseRedirect(
            reverse(viewname="lab5:show_exam_resultF", args=(course5.id, submission.id))
        )
    except Exception as err:
        return HttpResponse("Catched error ", str(err))


def extract_answers(request):
    submitted_anwsers = []
    for key in request.POST:
        if key.startswith("choice"):
            value = request.POST[key]
            choice_id = int(value)
            submitted_anwsers.append(choice_id)
    return submitted_anwsers


def show_exam_result(request, course5_id, submission5_id):
    total = {}
    course5 = get_object_or_404(Course5, pk=course5_id)
    submission = Submission5.objects.get(id=submission5_id)
    choices = submission.choices.all()
    total_score = 0
    total_wrong = 0
    for choice in choices:
        if choice.is_correct:
            total_score += choice.question_id  # .grade
        else:
            total_wrong += choice.question_id
    total["course"] = course5
    total["grade"] = exam_grade_score(total_score, total_wrong)
    total["choices"] = choices
    return render(request, "onlinecourse/user_result_bootstrap.html", total)


# Exam_grade_final
def exam_grade_score(score, mistakes):
    try:
        result = round((100 * (score - mistakes) / score), 2)
        return result
    except ZeroDivisionError as zero:
        return ("Error", zero)
