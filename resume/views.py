from django.shortcuts import render

# Create your views here.
def resume(request):
    template_name = 'resume/resume.html'
    context={}
    return render(request, template_name, context)