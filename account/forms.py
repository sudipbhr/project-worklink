from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms
from account.models import UserEducation, UserSkills

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'last_name')
        # fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'gender', 'avatar', 'experience', 'address', 
                  'phone_number')

    def __init__(self, *args, **kwargs):
         super(UserProfileForm, self).__init__(*args, **kwargs)
         for field in self.fields:
            self.fields[field].widget.attrs=({
                'class': 'form-control',
            })
class UserEducationForm(forms.ModelForm):

    class Meta:
        model = UserEducation
        fields = ['level', 'degree', 'add_degree']
        
    def __init__(self, *args, **kwargs):
         super(UserEducationForm, self).__init__(*args, **kwargs)
         for field in self.fields:
            self.fields[field].widget.attrs=({
                'class': 'form-control',
            })
class UserSkillsForm(forms.ModelForm):

    class Meta:
        model = UserSkills
        fields = ('name',)

    def __init__(self, *args, **kwargs):
         super(UserSkillsForm, self).__init__(*args, **kwargs)
         for field in self.fields:
            self.fields[field].widget.attrs=({
                'class': 'form-control',
            })
