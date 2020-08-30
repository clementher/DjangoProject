from django.db import models
import datetime

# Create your models here.
from django.forms import forms


class Cursus(models.Model):
    name = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        default='Nom'
    )

    year_from_bac = models.SmallIntegerField(
        help_text="year since le bac",
        verbose_name="year",
        blank=False,
        null=True,
        default=1
    )

    scholar_year = models.CharField(
        max_length=9,
        blank=False,
        null=True,
        default='2019-2020'
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )

    birth_date = models.DateField(
        verbose_name='date of birth',
        blank=False,
        null=False
    )

    last_name = models.CharField(
        verbose_name="lastname",
        blank=False,  # pas de champ vide
        null=False,  # pas de champ null (a conjuguer avec default
        default="???",
        max_length=255,  # taille maximale du champ
    )

    phone = models.CharField(
        verbose_name="phonenumber",
        help_text="Phone number of the student",
        blank=False,  # pas de champ vide
        null=False,  # pas de champ null (a conjuguer avec default
        default="0999999999",
        max_length=10,  # taille maximale du champ
    )

    email = models.EmailField(
        verbose_name="email",
        help_text="Email of the student",
        blank=False,  # pas de champ vide
        null=False,  # pas de champ null (a conjuguer avec default
        default="x@y.z",
        max_length=255,  # taille maximale du champ
    )

    comments = models.CharField(
        verbose_name="comments",
        help_text="Some comments about the student",
        blank=True,
        null=False,  # pas de champ null (a conjuguer avec default
        default="",
        max_length=255,  # taille maximale du champ
    )

    cursus = models.ForeignKey(
        Cursus,
        help_text="Cursus of the student",
        on_delete=models.CASCADE,  # necessaire selon la version de Django
        null=True
    )

    def __str__(self):
        return self.email


class Roll(models.Model):
    date = models.DateField(
        blank=False,
        null=False,
        default=datetime.date.today
    )

    cursus = models.ForeignKey(
        Cursus,
        on_delete=models.CASCADE,  # necessaire selon la version de Django
        null=False
    )

    debut = models.TimeField(
        max_length=100,
        blank=False,
        null=False,
        default='08:00'
    )

    fin = models.TimeField(
        max_length=100,
        blank=False,
        null=False,
        default='09:00'
    )


class RollDetail(models.Model):
    date = models.DateField(
        blank=False,
        null=False,
        default=datetime.date.today
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,  # necessaire selon la version de Django
        null=False
    )

    absent = models.BooleanField(
        default=False
    )

    cause = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        default=''
    )

    roll = models.ForeignKey(
        Roll,
        on_delete=models.CASCADE,  # necessaire selon la version de Django
        null=True
    )

    debut = models.TimeField(
        max_length=100,
        blank=False,
        null=False,
        default='08:00'
    )

    fin = models.TimeField(
        max_length=100,
        blank=False,
        null=False,
        default='09:00'
    )

