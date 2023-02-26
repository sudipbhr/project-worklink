from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('edit/', views.user_profile_edit, name="edit-user-profile"),
    path('detail/', views.user_profile, name="user-profile"),
    path('manage-users/', views.manage_users, name='manage-users'),
    path('disqualify-document/<int:id>/', views.disqualify_document, name='disqualify-document'),
    path('verify-document/<int:id>/', views.verify_document, name='verify-document'),
]