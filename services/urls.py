from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('', views.home, name="home-page"),
    path('services/', views.services_search, name="service-search"),
    path('services/<str:id>/service-detail/', views.services_detail, name="service-detail"),
    path('service-search-map/',views.service_search_map, name="service-search-map"),
    path('candidates/candidate-detail/', views.candidate_detail, name="candidate-detail"),
    path('error-page/', views.error_page, name="404-page"),
    path('dashboard/', views.user_dashboard, name="dashboard"),
    path('about-us/', views.about_us, name="about-us"),
    path('contact-us/', views.contact_us, name="contact-us"),
    path('categories/', views.categories, name="categories"),
    path('post-job/', views.post_job, name="post-job"),
    path('manage-job/', views.manage_job, name="manage-job"),
    path('manage-seeker/', views.manage_seeker, name="manage-applicant"),
    path('my-profile/', views.my_profile, name="my-profile"),
    path('change-password/', views.change_password, name="change-password"),
    
]