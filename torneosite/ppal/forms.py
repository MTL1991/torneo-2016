from django.forms import *

from django.contrib.admin import widgets
from ppal.models import *

class TeamForm(ModelForm):
    class Meta:
        model = Team
        exclude = ['school','name']

class SchoolForm(ModelForm):
    password = CharField(widget=PasswordInput())
    password2 = CharField(widget=PasswordInput(), label="Password confirmation")

    class Meta:
        model = School

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError('Passwords do not match')

        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserForm(ModelForm):
    password = CharField(widget=PasswordInput())
    password2 = CharField(widget=PasswordInput(), label="Password confirmation")

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError('Passwords do not match')

        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# class FavEditForm(ModelForm):
#     class Meta:
#         model = Fav

class PlayerEditForm(ModelForm):
    class Meta:
        model = Player
        exclude = ['school','team']

class AdvancedSearchForm(forms.Form):


    school = CharField(max_length=60, required=False)

    title = CharField(max_length=60, required=False)

    description = CharField(max_length=100, required=False)

    
    def clean(self):
        cleaned_data = super(AdvancedSearchForm, self).clean()

    def __init__(self, *args, **kwargs):
        super(AdvancedSearchForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Titulo"
        self.fields['description'].label = "Descripcion"

        self.fields['title'].help_text = 'Nombre de un equipo'
        self.fields['description'].help_text = 'Texto contenido en la descripcion de un Tubo'
       # self.fields['school'].help_text = 'Nombre completo o parcial de un Tuber'
