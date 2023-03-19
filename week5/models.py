import sys
from django.utils.timezone import now

try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()

from django.conf import settings
import uuid


# Instructor model
class Instructor5(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    def __str__(self):
        return self.user.username


# Learner model
class Learner5(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    STUDENT = "student"
    DEVELOPER = "developer"
    DATA_SCIENTIST = "data_scientist"
    DATABASE_ADMIN = "dba"
    OCCUPATION_CHOICES = [
        (STUDENT, "Student"),
        (DEVELOPER, "Developer"),
        (DATA_SCIENTIST, "Data Scientist"),
        (DATABASE_ADMIN, "Database Admin"),
    ]
    occupation = models.CharField(
        null=False, max_length=20, choices=OCCUPATION_CHOICES, default=STUDENT
    )
    social_link = models.URLField(max_length=200)

    def __str__(self):
        return self.user.username + "," + self.occupation


# Course model
class Course5(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30, default="online course")
    image = models.ImageField(upload_to="course_images/")
    description = models.CharField(max_length=1000)
    pub_date = models.DateField(null=True)
    instructors = models.ManyToManyField(Instructor5)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Enrollment5")
    total_enrollment = models.IntegerField(default=0)
    is_enrolled = False

    def __str__(self):
        return "Name: " + self.name + "," + "Description: " + self.description


# Enrollment model
# <HINT> Once a user enrolled a class, an enrollment entry should be created between the user and course
# And we could use the enrollment to track information such as exam submissions
class Enrollment5(models.Model):
    AUDIT = "audit"
    HONOR = "honor"
    BETA = "BETA"
    COURSE_MODES = [(AUDIT, "Audit"), (HONOR, "Honor"), (BETA, "BETA")]
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course5, on_delete=models.CASCADE)
    date_enrolled = models.DateField(default=now)
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)
    rating = models.FloatField(default=5.0)


# Lesson model
class Lesson5(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="title")
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course5, on_delete=models.CASCADE)
    content = models.TextField()


class Question5(models.Model):
    # dct ={}
    id = models.AutoField(primary_key=True)
    course = models.ManyToManyField(Course5)
    question_text = models.CharField(max_length=200)
    grade = models.FloatField(default=1.0)

    def __str__(self):
        return "Question: " + self.question_text

    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(
            is_correct=True, id__in=selected_ids
        ).count()

        if all_answers == selected_correct:
            return True
        else:
            return False


class Choice5(models.Model):
    # dct= {}
    A = "A"
    B = "B"
    C = "C"
    CHOICE_ANSWER = [(A, "A"), (B, "B"), (C, "C")]
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question5, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, choices=CHOICE_ANSWER)
    answer = models.CharField(max_length=200, default="write your answer")
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text + " - " + self.answer


class Submission5(models.Model):
    id = models.AutoField(primary_key=True)
    enrollment = models.ForeignKey(Enrollment5, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice5)
    # question = models.ManyToManyField(Question)

    def __str__(self):
        return "self.pk"


# TODO store grade and answers to questions
# Exams grades to link with foreign key and add a colum examgrades above in class lessons or learner
class examGrades5(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course5, on_delete=models.CASCADE)
    #    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    #    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    exam_question = models.ManyToManyField(Question5)
    exam_answer = models.ManyToManyField(Choice5)
    grade = models.FloatField(default=0)

    def __str__(self):
        return self.exam_answer + "\n" + self.grade
