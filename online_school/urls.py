"""online_school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main_app import views as main_app

urlpatterns = [
    path('', main_app.index, name='home'),
    path('courses/', include('main_app.urls', namespace='courses')),
    # name=courses bu templateslarda ishlatilinadi, agarda birinchida turgan "courses" ni
    # nomini o'zgartirishga to'g'ri kelib qolsa bu silka nomini butun boshli saytda
    # o'zgartirib chiqish shart bo'lmaydi
    path('auth/', include('auth_app.urls', namespace='auth_app')),
    path('basket/', include('basket_app.urls', namespace='basket_app')),
    path('my-learnings/', main_app.my_learnings, name='my-learnings'),
    path('course/<int:pk>/<int:lesson_num>', main_app.example_course, name='example-course'),
    path('post/<int:pk>', main_app.view_post, name='view-post'),
    path('view_course/<int:pk>', main_app.view_course, name='view-course'),


    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
