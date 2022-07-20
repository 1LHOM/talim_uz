from django.urls import path
from auth_app import views as auth_app

app_name = 'auth_app'

urlpatterns = [
    path('login/', auth_app.login, name='login'),
    path('logout/', auth_app.logout, name='logout'),
    path('edit/', auth_app.edit, name='edit'),
    path('register/', auth_app.register, name='register'),

]