from django.urls import path
from basket_app import views as basket_app

app_name = 'basket_app'

urlpatterns = [
    path('', basket_app.basket, name='basket'),
    path('add/<int:pk>', basket_app.basket_add, name='basket_add'),
    path('remove/<int:pk>', basket_app.basket_remove, name='basket_remove')

]