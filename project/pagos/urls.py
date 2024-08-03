from django.urls import path
from .views import index, PagosList, PagosCreate, PagosUpdate

app_name = 'pagos'

urlpatterns = [
    path('', index, name='index'),
    path('lista/', PagosList.as_view(), name='pagos_list'),
    path('cargar_pago/', PagosCreate.as_view(), name='pagos_create'),
    path('editar_pago/<int:pk>', PagosUpdate.as_view(), name='pagos_update'),
]