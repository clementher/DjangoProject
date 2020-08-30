from django.conf.urls import url

from . import views
from .views import StudentCreateView, StudentUpdateView, CursusCreateView, CallOfRollStudent

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail'),

    url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),

    url(r'^cursus/create/$', CursusCreateView.as_view(), name='create_cursus'),

    url(r'^student/create/$', StudentCreateView.as_view(), name='create_student'),
    url(r'^student/edit/(?P<pk>[0-9]+)$', StudentUpdateView.as_view(), name='update_student'),


    url(r'^call_of_roll/(?P<cursus_id>[0-9]+)$', views.call_of_roll, name='call_of_roll'),
    url(r'^call/', CallOfRollStudent.as_view(), name='call_of_roll particular'),

    url(r'^rolls/list/', views.rolls, name='rolls'),
    url(r'^rolls_student/list/', views.roll_specific_detail, name='roll_specific_detail'),
    url(r'^rolls/details/(?P<roll_id>[0-9]+)$', views.roll_detail, name='roll_detail'),
]

