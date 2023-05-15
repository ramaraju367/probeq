from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# register user

class CreateUserForm(UserCreationForm):

    class meta:

        model = User
        fields = ['username', 'password1', 'passpword2']


#login user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Create a Record

class CreateRecordForm(forms.ModelForm):
    
        class meta:

            model = Record
            fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']



# update a Record

class UpdateRecordForm(forms.ModelForm):
    
        class meta:

            model = Record
            fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']
