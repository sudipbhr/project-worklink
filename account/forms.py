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
        fields = ('first_name', 'last_name', 'gender', 'avatar', 'experience', 'address', 
                  'phone_number','profession', 'description', 'email')

    def __init__(self, *args, **kwargs):
         super(UserProfileForm, self).__init__(*args, **kwargs)
         for field in self.fields:
            self.fields[field].widget.attrs=({
                'class': 'form-control',
            })
            if field == 'description':
                self.fields[field].widget.attrs=({
                    'class': 'form-control tinymce',
                    'rows': '30',
                })
class UserEducationForm(forms.ModelForm):

    class Meta:
        model = UserEducation
        fields = ['level', 'degree', 'edu_description', 'college_university_name', 'end_date']
        
    def __init__(self, *args, **kwargs):
         super(UserEducationForm, self).__init__(*args, **kwargs)
         for field in self.fields:
            self.fields[field].widget.attrs=({
                'class': 'form-control',
            })
            if field == 'end_date':
                self.fields[field].widget= forms.DateInput(attrs={
                    'class': 'form-control datepicker',
                    'placeholder': 'Select date',
                    'type': 'date',
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
            if field == 'name':
                self.fields[field].widget.attrs=({
                    'class': 'form-control select2',
                    'placeholder': 'Enter your skills',
                })
