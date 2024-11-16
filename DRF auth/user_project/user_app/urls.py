
from django.urls import path,include
from .views import UserLogout,UserLogin,UserRegistration
from knox.views import LogoutView


urlpatterns = [
    path('api/register/', UserRegistration.as_view(), name='register'),
    path('api/login/', UserLogin.as_view(), name='login'),
    path('api/logout/', UserLogout.as_view(), name='logout'),
    path('auth/', include('rest_framework.urls', namespace='register')),

    
]
