from django.shortcuts import render
from django.views.generic import TemplateView

from django.views.decorators.csrf import csrf_exempt, csrf_protect


class HomePageView(TemplateView):
    template_name = "main.html"
    #  do staff


class Week1PageView(TemplateView):
    template_name = "week1.html"
    #  do staff


class Week2PageView(TemplateView):
    template_name = "week2.html"
    #  do staff


class Week3PageView(TemplateView):
    template_name = "week3.html"
    #  do staff


class Week4PageView(TemplateView):
    template_name = "week4.html"
    #  do staff


class Week5PageView(TemplateView):
    template_name = "week5.html"
    #  do staff


# class DataPageView(TemplateView):
#     def get(self, request, **kwargs):
#         context = {
#             'data': [
#                 {
#                     'name': 'Celeb 1',
#                     'worth': '3567892'
#                 },
#                 {
#                     'name': 'Celeb 2',
#                     'worth': '23000000'
#                 },
#                 {
#                     'name': 'Celeb 3',
#                     'worth': '1000007'
#                 },
#                 {
#                     'name': 'Celeb 4',
#                     'worth': '456789'
#                 },
#                 {
#                     'name': 'Celeb 5',
#                     'worth': '7890000'
#                 },
#                 {
#                     'name': 'Celeb 6',
#                     'worth': '12000456'
#                 },
#                 {
#                     'name': 'Celeb 7',
#                     'worth': '896000'
#                 },
#                 {
#                     'name': 'Celeb 8',
#                     'worth': '670000'
#                 }
#             ]
#         }

#         return render(request, 'data.html', context)
