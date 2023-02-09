from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('', views.home, name="home-page"),
    path('services/', views.services_search, name="service-search"),
    path('services/<str:id>/service-detail/', views.services_detail, name="service-detail"),
    path('service-search-map/',views.service_search_map, name="service-search-map"),
    path('candidates/candidate-detail/<int:id>', views.candidate_detail, name="candidate-detail"),
    path('error-page/', views.error_page, name="404-page"),
    path('dashboard/', views.user_dashboard, name="dashboard"),
    path('about-us/', views.about_us, name="about-us"),
    path('contact-us/', views.contact_us, name="contact-us"),
    path('categories/', views.categories, name="categories"),
    path('post-job/', views.post_job, name="post-job"),
    path('post-job/<int:job_id>', views.post_job, name="post-job"),
    path('delete-job/<int:id>', views.delete_job, name="delete-job"),
    path('manage-job/', views.manage_job, name="manage-job"),
    path('manage-applicants/<int:id>', views.manage_applicant, name="manage-applicant"),
    path('my-profile/', views.my_profile, name="my-profile"),
    path('change-password/', views.change_password, name="change-password"),
    path('add-category/', views.add_category, name="add-category"),
    path('job-skill/', views.job_skill, name = "job-skill"),
    path('review/', views.review, name="review"),
    path('transactions/', views.transactions, name = "transaction"),
]