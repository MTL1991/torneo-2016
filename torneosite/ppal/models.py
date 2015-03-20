from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from simple_email_confirmation import SimpleEmailConfirmationUserMixin


class User(AbstractUser):
    pass

class School(models.Model):
    user = models.OneToOneField(User, editable=False)
    name = models.CharField(max_length=30)
    number = models.IntegerField()

    def __unicode__(self):
        return u'%s' % (self.name)

class Team(models.Model):

    school = models.ForeignKey('School')
    name = models.CharField(max_length=30)

    PRIMERO_TERCERO = 1
    TERCERO_SEXTO = 2

    TYPES = (
        (PRIMERO_TERCERO, '1 a 3'),
        (TERCERO_SEXTO, '3 a 6'),
    )

    years = models.IntegerField(choices=TYPES)

    last_editing_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s | Categoria: %s' % (self.school.name, self.years)


class Player(models.Model):

    school = models.ForeignKey('School')
    team = models.ForeignKey('Team')
    JUGADORA = 1
    DELEGADO = 2

    TYPES = (
        (JUGADORA, 'Jugadora'),
        (DELEGADO, 'Delegado/a'),
    )


    member = models.IntegerField(choices=TYPES)
    name = models.CharField(max_length=30)
    surname1 = models.CharField(max_length=30)
    surname2 = models.CharField(max_length=30)
    birthday = models.DateField()
    email = models.CharField(max_length=30, blank=True, null=True)
    movil = models.CharField(max_length=30, blank=True, null=True)
    def __unicode__(self):
        return u'Nombre: %s | Apellido: %s | Categoria: %s' % (self.name, self.surname1, self.team.years)
