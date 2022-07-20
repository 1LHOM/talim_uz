from django.urls import path
from main_app import views as main_app

app_name = 'courses'

urlpatterns = [
    path('', main_app.courses, name='courses'),
    path('<int:pk>', main_app.courses, name='category')

]