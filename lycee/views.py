from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views.generic import CreateView

from .forms import StudentForm
from .models import Cursus, Student

import logging


def index(request):
    result_list = Cursus.objects.order_by('name')
    template = loader.get_template('lycee/index.html')
    context = {
        'liste': result_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, cursus_id):
    result_list = Student.objects.filter(cursus_id=cursus_id)
    template = loader.get_template('lycee/cursus/detail_cursus.html')
    context = {
        'liste': result_list,
    }
    return HttpResponse(template.render(context, request))


def call_of_roll(request, cursus_id):
    if request.method == 'POST':
        result_list = Student.objects.filter(cursus_id=cursus_id)
        absents = []
        presents = []

        for student in result_list:
            stu = request.POST.get(str(student.id))
            if stu == 'on':
                absents.append(student)

        for student in result_list:
            if student not in absents:
                presents.append(student)

        template = loader.get_template('lycee/cursus/call_of_roll.html')
        context = {
            'liste': result_list,
        }
        return HttpResponse(template.render(context, request))
    else:
        result_list = Student.objects.filter(cursus_id=cursus_id)
        template = loader.get_template('lycee/cursus/call_of_roll.html')
        context = {
            'liste': result_list,
        }
        return HttpResponse(template.render(context, request))


def detail_student(request, student_id):
    result_list = Student.objects.get(pk=student_id)
    context = {'liste': result_list, }
    return render(request, 'lycee/student/detail_student.html', context)


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "lycee/student/create.html"

    def get_success_url(self):
        return reverse("detail_student", args=(self.object.pk,))
