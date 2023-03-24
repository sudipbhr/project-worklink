from django import forms
from services.models import Services, JobSkills, Category


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
            self.fields[field].widget.attrs=({
                'class': 'form-control form-select select2',
                'multiple': 'multiple',

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
                'class': 'form-control form-select select2',
                'multiple': 'multiple',
            })

