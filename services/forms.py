from django import forms
from services.models import Services,JobSkills


class PostJobForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = ['title', 'description', 'amount', 'duration', 'status', 'category', 'skills', 'vacancy', 'location', 'image']

    def __init__(self, *args, **kwargs):
        super(PostJobForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs=({
                'required': 'true',
                'class': 'form-control',
            })
# class JobSkillsForm(forms.ModelForm):

#     class Meta:
#         model = JobSkills
#         field = ('name',)
#     def __init__(self, *args, **kwargs):
#         super(JobSkillsForm, self).__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs=({
#                 'required': 'true',
#                 'class': 'form-control',
#             })



