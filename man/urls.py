from django.urls import path, include
from .views import  logout_view,login_view,register_view


urlpatterns = [
    path('register/', register_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
