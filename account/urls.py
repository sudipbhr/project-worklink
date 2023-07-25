from . import api_views as views
from rest_framework import routers
from django.urls import include, path
from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('edit/', views.user_profile_edit, name='edit-user-profile'),
    path('detail/', views.user_profile, name='profile'),
    path('manage-users/', views.manage_users, name='manage-users'),
    path('disqualify-document/<int:id>/',
         views.disqualify_document, name='disqualify-document'),
    path('verify-document/<int:id>/',
         views.verify_document, name='verify-document'),
    path('education/<str:id>/', views.del_education, name='del_education'),
]


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     # path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
