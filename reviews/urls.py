from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('review/<int:id>/<str:s_id>', views.review, name="review"),
]
