from django.urls import path
from app_autenticacao import views

urlpatterns = [
   path('',views.login, name='login'),
   path('register/',views.register, name='register')
]
