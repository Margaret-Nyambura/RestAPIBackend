from django.urls import path
from .views import login, user_logout

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', user_logout, name='logout'),
]
