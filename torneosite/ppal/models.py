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
    GROUP = (
        (1, 'G1'),
        (2, 'G2'),
        (3, 'G3'),
        (4, 'G4'),
        (5, 'G5'),
        (6, 'G6'),
        (7, 'G7'),
        (8, 'G8'),
        (9, 'G9'),
        (10, 'G10'),

    )

    OCTAVOS = (
        (1, 'O1'),
        (2, 'O2'),
        (3, 'O3'),
        (4, 'O4'),
        (5, 'O5'),
        (6, 'O6'),
        (7, 'O7'),
        (8, 'O8'),
    )

    CUARTOS = (
        (1, 'C1'),
        (2, 'C2'),
        (3, 'C3'),
        (4, 'C4'),
    )

    SEMIS = (
        (1, 'S1'),
        (2, 'S2'),
    )

    FINAL = (
        (1, 'F1'),
    )

    group = models.IntegerField(choices=GROUP,default=0,blank=True, null=True);
    octavos = models.IntegerField(choices=OCTAVOS,default=0,blank=True, null=True);
    cuartos = models.IntegerField(choices=CUARTOS,default=0,blank=True, null=True);
    semis = models.IntegerField(choices=SEMIS,default=0,blank=True, null=True);
    final = models.IntegerField(choices=FINAL,default=0,blank=True, null=True);

    years = models.IntegerField(choices=TYPES)
    matchs = models.IntegerField(default=0,blank=True, null=True);
    wins = models.IntegerField(default=0,blank=True, null=True);
    draw = models.IntegerField(default=0,blank=True, null=True);
    lose = models.IntegerField(default=0,blank=True, null=True); 
    goalf = models.IntegerField(default=0,blank=True, null=True);
    goalc = models.IntegerField(default=0,blank=True, null=True); 
    point = models.IntegerField(default=0,blank=True, null=True);  
    playersnumber = models.IntegerField();              
    last_editing_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s | Categoria: %s' % (self.name, self.years)

# class Group(models.Model):

#     team1 = models.ForeignKey('Team',related_name='team1')
#     team2 = models.ForeignKey('Team',related_name='team2')
#     team3 = models.ForeignKey('Team',related_name='team3')

#     PRIMERO_TERCERO = 1
#     TERCERO_SEXTO = 2

#     TYPES = (
#         (PRIMERO_TERCERO, 'sub-9'),
#         (TERCERO_SEXTO, 'sub-12'),
#     )

#     years = models.IntegerField(choices=TYPES)

class Match(models.Model):



    PRIMERO_TERCERO = 1
    TERCERO_SEXTO = 2

    TYPES = (
        (PRIMERO_TERCERO, 'sub-9'),
        (TERCERO_SEXTO, 'sub-12'),
    )


    PLACE = (
        (1, 'PISTA 1'),
        (2, 'PISTA 2'),
        (3, 'PISTA 3'),
        (4, 'PISTA 4'),
        (5, 'PISTA 5'),
        (6, 'PISTA 6'),
        (7, 'PISTA 7'),
        (8, 'PISTA 8'),
        (9, 'PISTA 9'),
    )

    GROUP = (
        (1, 'G1'),
        (2, 'G2'),
        (3, 'G3'),
        (4, 'G4'),
        (5, 'G5'),
        (6, 'G6'),
        (7, 'G7'),
        (8, 'G8'),
        (9, 'G9'),
        (10, 'G10'),

    )

    OCTAVOS = (
        (1, 'O1'),
        (2, 'O2'),
        (3, 'O3'),
        (4, 'O4'),
        (5, 'O5'),
        (6, 'O6'),
        (7, 'O7'),
        (8, 'O8'),
    )

    CUARTOS = (
        (1, 'C1'),
        (2, 'C2'),
        (3, 'C3'),
        (4, 'C4'),
    )

    SEMIS = (
        (1, 'S1'),
        (2, 'S2'),
    )

    FINAL = (
        (1, 'F1'),
    )


    years = models.IntegerField(choices=TYPES)
    local = models.ForeignKey('Team',related_name='local',blank=True, null=True)
    away = models.ForeignKey('Team',related_name='away',blank=True, null=True)
    team1Score = models.IntegerField(blank=True, null=True)
    team2Score = models.IntegerField(blank=True, null=True)
    group = models.IntegerField(choices=GROUP,default=0,blank=True, null=True);
    octavos = models.IntegerField(choices=OCTAVOS,default=0,blank=True, null=True);
    cuartos = models.IntegerField(choices=CUARTOS,default=0,blank=True, null=True);
    semis = models.IntegerField(choices=SEMIS,default=0,blank=True, null=True);
    final = models.IntegerField(choices=FINAL,default=0,blank=True, null=True);
    place = models.IntegerField(choices=PLACE)
    hora = models.IntegerField()
    minutes = models.IntegerField()


    def __unicode__(self):
        return u'%s vs  %s '   % (self.local.name, self.away.name,)


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
