from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from .forms import StudentForm, CursusForm, RollForm
from .models import Cursus, Student, Roll, RollDetail


def index(request):
    result_list = Cursus.objects.order_by('name')
    template = loader.get_template('lycee/index.html')
    context = {
        'liste': result_list,
    }
    return HttpResponse(template.render(context, request))


### Rolls ###
def rolls(request):
    result_list = Roll.objects.order_by('date')
    context = {
        'liste': result_list,
    }
    return render(request, 'lycee/calls/call_list.html', context)


def roll_detail(request, roll_id):
    result_list = RollDetail.objects.filter(roll_id=roll_id)
    roll = Roll.objects.get(id=roll_id)

    template = loader.get_template('lycee/calls/call_detail.html')
    context = {
        'liste': result_list,
        'roll': roll,
    }
    return HttpResponse(template.render(context, request))


def roll_specific_detail(request):
    result_list = RollDetail.objects.filter(roll_id__isnull=True)
    template = loader.get_template('lycee/calls/call_student_list.html')
    context = {
        'liste': result_list,
    }
    return HttpResponse(template.render(context, request))


### Call of roll ###
def call_of_roll(request, cursus_id):
    if request.method == 'POST':
        result_list = Student.objects.filter(cursus_id=cursus_id)
        result_cursus = Cursus.objects.get(id=cursus_id)
        roll = Roll(date=request.POST.get('date'), cursus=result_cursus,
                    debut=request.POST.get('debut'), fin=request.POST.get('fin'))
        roll.save()

        # Liste des absents
        for student in result_list:
            stu = request.POST.get(str(student.id))

            if stu == 'on':
                rollDetail = RollDetail(roll=roll, date=request.POST.get('date'), student=student, absent=True)
            else:
                rollDetail = RollDetail(roll=roll, date=request.POST.get('date'), student=student, absent=False,
                                        debut=request.POST.get('debut'), fin=request.POST.get('fin'))

            rollDetail.save()

        template = loader.get_template('lycee/cursus/call_of_roll.html')
        context = {
            'liste': result_list,
        }
        return HttpResponse(template.render(context, request))
    else:
        result_list = Student.objects.filter(cursus_id=cursus_id)
        # Changer l'URL en cursusCall
        template = loader.get_template('lycee/cursus/call_of_roll.html')
        context = {
            'liste': result_list,
        }
        return HttpResponse(template.render(context, request))

class CallOfRollStudent(CreateView):
    model = Cursus
    form_class = RollForm
    template_name = "lycee/student/call_of_roll_student.html"

    def get_success_url(self):
        return reverse("roll_specific_detail")

### Student ###
def detail_student(request, student_id):
    result_list = Student.objects.get(pk=student_id)
    result_absences = RollDetail.objects.filter(student_id=student_id, absent=1)
    context = {
        'liste': result_list,
        'absences': result_absences,
    }
    return render(request, 'lycee/student/detail_student.html', context)


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "lycee/student/create.html"

    def get_success_url(self):
        return reverse("detail_student", args=(self.object.pk,))


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "lycee/student/create.html"

    def get_success_url(self):
        return reverse("detail_student", args=(self.object.pk,))


### Cursus ###
def detail(request, cursus_id):
    result_list = Student.objects.filter(cursus_id=cursus_id)
    result_cursus = Cursus.objects.get(id=cursus_id)
    template = loader.get_template('lycee/cursus/detail_cursus.html')
    context = {
        'liste': result_list,
        'cursus': result_cursus,
    }
    return HttpResponse(template.render(context, request))


class CursusCreateView(CreateView):
    model = Cursus
    form_class = CursusForm
    template_name = "lycee/cursus/create.html"

    def get_success_url(self):
        return reverse("index")
