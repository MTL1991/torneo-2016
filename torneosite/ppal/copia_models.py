from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class School(models.Model):
    user = models.OneToOneField(User, editable=False)
    name = models.CharField(max_length=30)
    numberp = models.IntegerField()
    numberm = models.IntegerField()
    superuser = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % (self.name)

class Team(models.Model):

    school = models.ForeignKey('School')
    name = models.CharField(max_length=30)

    PRIMERO_TERCERO = 1
    TERCERO_SEXTO = 2

    TYPES = (
        (PRIMERO_TERCERO, 'sub-9'),
        (TERCERO_SEXTO, 'sub-12'),
    )


    years = models.IntegerField(choices=TYPES)
    matchs = models.IntegerField(default=0,blank=True, null=True);
    wins = models.IntegerField(default=0,blank=True, null=True);
    draw = models.IntegerField(default=0,blank=True, null=True);
    lose = models.IntegerField(default=0,blank=True, null=True); 
    goalf = models.IntegerField(default=0,blank=True, null=True);
    goalc = models.IntegerField(default=0,blank=True, null=True); 
    point = models.IntegerField(default=0,blank=True, null=True);                
    last_editing_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s | Categoria: %s' % (self.name, self.years)

class Group(models.Model):

    team1 = models.ForeignKey('Team',related_name='team1')
    team2 = models.ForeignKey('Team',related_name='team2')
    team3 = models.ForeignKey('Team',related_name='team3')

    PRIMERO_TERCERO = 1
    TERCERO_SEXTO = 2

    TYPES = (
        (PRIMERO_TERCERO, 'sub-9'),
        (TERCERO_SEXTO, 'sub-12'),
    )

    years = models.IntegerField(choices=TYPES)


class Match(models.Model):

    local = models.ForeignKey('Team',related_name='local')
    away = models.ForeignKey('Team',related_name='away')

    PRIMERO_TERCERO = 1
    TERCERO_SEXTO = 2

    TYPES = (
        (PRIMERO_TERCERO, 'sub-9'),
        (TERCERO_SEXTO, 'sub-12'),
    )


    PLACE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
    )

    GRUPO = 1
    OCTAVOS = 2
    CUARTOS = 3
    SEMIFINALES = 4
    FINAL = 5

    FASE = (
        (GRUPO, 'GRUPO'),
        (OCTAVOS, 'OCTAVOS'),
        (CUARTOS, 'CUARTOS'),
        (SEMIFINALES, 'SEMIFINALES'),
        (FINAL, 'FINAL'),
    )


    years = models.IntegerField(choices=TYPES)
    place = models.IntegerField(choices=PLACE)
    fase = models.IntegerField(choices=FASE)
    hora = models.IntegerField()
    minutes = models.IntegerField()
    team1Score = models.IntegerField(blank=True, null=True)
    team2Score = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s vs  %s' % (self.local.name, self.away.name)


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
    surname2 = models.CharField(max_length=30, blank=True, null=True)
    birthday = models.DateField()
    email = models.CharField(max_length=30, blank=True, null=True)
    movil = models.CharField(max_length=30, blank=True, null=True)
    def __unicode__(self):
        return u'Nombre: %s | Apellido: %s | Categoria: %s' % (self.name, self.surname1, self.team.years)
