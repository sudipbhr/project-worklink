from django import forms
from services.models import Services, JobSkills, Category, Inquries


class PostJobForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = ['title', 'description', 'amount', 'duration', 'status', 'category', 'skills', 'vacancy', 'location', 'image']
        exclude = ['posted_by']

    def __init__(self, *args, **kwargs):
        super(PostJobForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs=({
                'class': 'form-control',
                'placeholder': 'Enter your ' + field,
            })
            if field == 'description':
                self.fields[field].widget.attrs=({
                    'class': 'form-control tinymce',
                    'rows': '30',
                })

            if field == 'skills':
                self.fields[field].widget.attrs=({
                    'class': 'form-control select2',
                    'placeholder': 'Enter your skills',
                    'multiple': 'multiple',
                })
            if field == 'category':
                self.fields[field].widget.attrs=({
                    'class': 'form-control form-select select2',
                    'placeholder': 'Enter your category',
                    'multiple': 'multiple',

                })
# category form

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'skills', 'image']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'skills':
                self.fields[field].widget.attrs=({
                    'class': 'form-control select2',
                    'multiple': 'multiple',
                })

            self.fields[field].widget.attrs=({
                'class': 'form-control',
            })

# Job skills form

class JobSkillForm(forms.ModelForm):

    class Meta:
        model = JobSkills
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(JobSkillForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs=({
                'class': 'form-control',
                'placeholder': 'Enter field name' ,
              
            })


class ContactUsForm(forms.ModelForm):

    def validate(self):
        cleaned_data = super(ContactUsForm, self).clean()
        email = cleaned_data.get('email')
        name = cleaned_data.get('name')
        message = cleaned_data.get('message')
        if not email:
            raise forms.ValidationError('Please enter your email')
        if not name:
            raise forms.ValidationError('Please enter your name')
        if not message:
            raise forms.ValidationError('Please enter your message')
        
    class Meta:
        model = Inquries
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs=({
                'class': 'form-control',
                'placeholder': 'Enter your ' + field,
            })

