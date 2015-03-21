from django.shortcuts import render

from django.http import *

from django.core.urlresolvers import reverse,reverse_lazy


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView



from braces.views import LoginRequiredMixin # sudo pip install django-braces
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver


from ppal.models import *
from ppal.forms import *

import simplejson as json


import urllib

from django.utils.http import *
from django.db.models import Q

def index(request):
    school_list1 = Team.objects.filter(years=1).order_by('-last_editing_date')[:5]
    school_list2 = Team.objects.filter(years=2).order_by('-last_editing_date')[:5]
    return render(request, 'index.html', {
        'school_list_p': school_list1,
        'school_list_m': school_list2,

    })

def index_all(request):
    school_list1 = Team.objects.filter(years=1).order_by('-last_editing_date')
    school_list2 = Team.objects.filter(years=2).order_by('-last_editing_date')
    return render(request, 'index_all.html', {
        'school_list_p': school_list1,
        'school_list_m': school_list2,

    })

def us(request):
    return render(request, 'us.html')

def school_login(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect(reverse(index))
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                dest = request.GET.get('next') if request.GET.get('next') != None else reverse(index)
                return HttpResponseRedirect(dest)
            else:
                return HttpResponse('not valid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login')
def school_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))

def school_view(request, num):
    try:
        user = User.objects.get(id=num)
    except User.DoesNotExist:
        raise Http404()
    if request.user.is_anonymous():
        return HttpResponseRedirect(reverse(index))
    else:
        team_list = Team.objects.filter(school=user.school)
        player_list = Player.objects.filter(school=user.school,)
        return render(request, 'school_view.html', {
            'school': user.school,
            'user': request.user, # footer
            'school_list': team_list,
            'player_list': player_list,
            })


def create_school(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            school = School(user=user)
            school.name = user.username
            school.number = 1
            school.save()
            u = authenticate(username=request.POST['username'],
                             password=request.POST['password'])
            login(request, u)
            return HttpResponseRedirect(reverse(index))
        else:
            return HttpResponse('user not valid')
    else:
        form = UserForm()
    return render(request, 'school_form.html', {'form': form})

def team_view(request, pk):
    try:
        user = request.user
    except User.DoesNotExist:
        raise Http404()
    if request.user.is_anonymous():
        return HttpResponseRedirect(reverse(index))
    else:
        team_list = Team.objects.filter(school=user.school)
        team = Team.objects.get(id=pk)
        player_list = Player.objects.filter(team= team,)
        return render(request, 'team_view.html', {
            'school': user.school,
            'user': request.user, # footer
            'team': team,
            'school_list': team_list,
            'player_list': player_list,
            })


class TeamDefinitiveView(DetailView):
    template_name = 'team_view.html'

    def get_context_data(self, **kwargs):
        context = super(TeamDefinitiveView, self).get_context_data(**kwargs)
        player_list = Player.objects.filter(school=self.request.user.school,)
        context['player_list']= player_list
        return context


class TeamView(LoginRequiredMixin, TeamDefinitiveView):
    model = Team

@login_required(login_url='/login')
def create_team(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect(reverse(index))
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if "cancel" in request.POST:
                return HttpResponseRedirect(reverse(index))
        if form.is_valid():
           team = form.save(commit = False)
           team.school = request.user.school
           team.name = request.user.school.name +" '"+str(request.user.school.number)+"'"
           team.save()
           number = request.user.school.number +1 
           school = School.objects.filter(name=request.user.school.name).update(number=number)
           return HttpResponseRedirect(reverse(index))
    else:
        form = TeamForm()
    return render(request, 'team_form.html', {'form': form})

class TeamDefinitiveDelete(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('index') # in the future, this will redirect to the user profile
    template_name = 'confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super(TeamDefinitiveDelete, self).get_object()
        if not obj.school == self.request.user.school:
            raise Http404
        return obj

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.success_url
            return HttpResponseRedirect(url)
        else:
            return super(TeamDefinitiveDelete, self).post(request, *args, **kwargs)



class TeamDelete(TeamDefinitiveDelete):
    model = Team

# @login_required(login_url='/login')
# def create_fav(request, pk):
#     if request.method == 'POST':
#         form = FavEditForm(request.POST)
#         if "cancel" in request.POST:
#             return HttpResponseRedirect(reverse('view_team', kwargs={'pk':pk}))
#         if form.is_valid():
#             fav = Fav(creator=request.user.school,
#                                       status = Fav.STATUS_FAV,
#                                       video = Tubo.objects.get(id=pk),
#                                       )
#             fav.save()
#             return HttpResponseRedirect(reverse('view_team', kwargs={'pk':pk}))
#     else:
#         form = FavEditForm()

#     return render(request, 'fav_form.html', {'form': form})

@login_required(login_url='/login')
def create_player(request, pk):
    if request.user.is_anonymous():
        return HttpResponseRedirect(reverse(index))
    if request.user.school == Team.objects.get(id=pk).school:
        if request.method == 'POST':
            form = PlayerEditForm(request.POST)
            if "cancel" in request.POST:
                    return HttpResponseRedirect(reverse(index))
            if form.is_valid():
                player = form.save(commit = False)
                player.school = request.user.school
                player.team = Team.objects.get(id=pk)
                player.save()
                return HttpResponseRedirect(reverse(index))
        else:
            form = PlayerEditForm()
        return render(request, 'player_form.html', {'form': form})
    else:
        raise Http404


def player_view(request, pk):
    if request.user.is_anonymous():
        return HttpResponseRedirect(reverse(index))
    player = Player.objects.get(id=pk)
    return render(request, 'player_view.html', {
        'player': player,
        })


class PlayerDefinitiveDelete(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('index') # in the future, this will redirect to the user profile
    template_name = 'confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super(PlayerDefinitiveDelete, self).get_object()
        if not obj.school == self.request.user.school:
            raise Http404
        return obj

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.success_url
            return HttpResponseRedirect(url)
        else:
            return super(PlayerDefinitiveDelete, self).post(request, *args, **kwargs)



class PlayerDelete(PlayerDefinitiveDelete):
    model = Player

# class FavView(DetailView):
#     template_name = 'fav_form.html'
#     model = Fav

# class FavDelete(LoginRequiredMixin, DeleteView):
#     template_name = 'fav_confirm_delete.html'
#     model = Fav

#     def get_object(self, queryset=None):
#         obj = super(FavDelete, self).get_object()
#         if not obj.creator == self.request.user.school:
#             raise Http404
#         return obj

#     def post(self, request, *args, **kwargs):
#         if "cancel" in request.POST:
#             url = self.get_success_url()
#             return HttpResponseRedirect(url)
#         else:
#             return super(FavDelete, self).post(request, *args, **kwargs)

#     def get_success_url(self):
#         return reverse_lazy(index)

