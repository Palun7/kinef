from django.urls import path
from .views import index, GastosCreate, GastosList, GastosUpdate

app_name = 'gastos'

urlpatterns = [
    path('', index, name='index'),
    path('create/', GastosCreate.as_view(), name='gastos_create'),
    path('update/<int:pk>', GastosUpdate.as_view(), name='gastos_update'),
    path('lista/', GastosList.as_view(), name='gastos_list'),
    path('lista/<int:pk>', GastosList.as_view(), name='gastos_list_mes'),
]