from django.urls import path
from .views import index, HorasCreate, HorasList, HorasUpdate, HorasDetail

app_name = 'horas'

urlpatterns = [
    path('', index, name='index'),
    path('list/', HorasList.as_view(), name='horas_list'),
    path('create/', HorasCreate.as_view(), name='horas_create'),
    path('update/<int:pk>', HorasUpdate.as_view(), name='horas_update'),
    path('detail/<int:pk>', HorasDetail.as_view(), name='horas_detail'),
]