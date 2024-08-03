from django.urls import path
from .views import (
    index,
    signup,
    login,
    UsuariosDelete,
    UsuariosDetail,
    UsuariosList,
    UsuariosUpdate
)
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('usuarios/index', index, name='index'),
    path('usuarios/signup', signup, name='signup'),
    path('usuarios/login', login.as_view(), name='login'),
    path('usuarios/logout', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
]

urlpatterns += [
    path('usuarios/lista', UsuariosList.as_view(),name='usuarios_list'),
    path('usuarios/detalle/<int:pk>', UsuariosDetail.as_view(),name='usuarios_detail'),
    path('usuarios/editar/<int:pk>', UsuariosUpdate.as_view(),name='usuarios_update'),
    path('usuarios/borrar/<int:pk>', UsuariosDelete.as_view(),name='usuarios_delete'),
]