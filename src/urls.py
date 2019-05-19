from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]