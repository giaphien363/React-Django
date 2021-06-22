from django.contrib import admin
from django.urls import path, include
# from api.views import index
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    # path('', index)
    path('auth/', obtain_auth_token)
]
