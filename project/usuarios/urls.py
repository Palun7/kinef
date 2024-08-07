from django.urls import path
from .views import (
    index,
    signup,
    login,
    UsuariosDelete,
    UsuariosDetail,
    UsuariosList,
    UsuariosUpdate,
    perfil,
)
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('perfil/<int:pk>/', perfil, name='perfil')
]

urlpatterns += [
    path('lista/', UsuariosList.as_view(),name='usuarios_list'),
    path('detalle/<int:pk>/', UsuariosDetail.as_view(),name='usuarios_detail'),
    path('editar/<int:pk>/', UsuariosUpdate.as_view(),name='usuarios_update'),
    path('borrar/<int:pk>/', UsuariosDelete.as_view(),name='usuarios_delete'),
]