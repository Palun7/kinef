from django.urls import path
from .views import index, contacto

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contacto/', contacto, name='contacto'),
]