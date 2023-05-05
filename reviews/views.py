from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from .models import JobReviews
from account.models import User
from services.models import Services


# Create your views here.
@login_required(login_url = '/auth/login/')
def review(request, id, s_id):
    user = User.objects.get(id=id)
    service = Services.objects.get(id=s_id)
    if request.method == 'POST':
        rating = request.POST.get('f_rate')
        review = request.POST.get('review')
        # get prev rating
        prev_rating = JobReviews.objects.filter(reviewer=request.user, doer=user, service=service)
        if prev_rating:
            prev_rating.delete()
            review = JobReviews.objects.create(
                reviewer = request.user,
                doer = user,
                service = service,
                review = review,
                rating = rating
            )
            review.save()
            messages.success(request, "Review added successfully")
            return redirect('manage-applicant', id=service.id)
        elif rating or review:
            review = JobReviews.objects.create(
                reviewer = request.user,
                doer = user,
                service = service,
                review = review,
                rating = rating
            )
            review.save()
            messages.success(request, "Review added successfully")
            return redirect('manage-applicant', id=service.id)
    template_name='reviews/review.html'
    context={
        'user': user,
        'service': service,
    }
    return render(request, template_name, context)