from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import DeleteView, DetailView, ListView, UpdateView
from .models import Usuarios
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
    return render(request, 'usuarios/index.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('usuarios:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/signup.html', {'form': form})

class login(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "usuarios/login.html"

class UsuariosDetail(DetailView):
    model = Usuarios

class UsuariosDelete(LoginRequiredMixin, DeleteView):
    model = Usuarios
    success_url = reverse_lazy('usuarios:usuarios_list')

class UsuariosList(LoginRequiredMixin, ListView):
    model = Usuarios
    context_object_name = 'usuarios'

    def get_queryset(self):
        queryset = Usuarios.objects.filter(user=self.request.user)
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda) |
                Q(apellido__icontains=busqueda) |
                Q(dni__icontains=busqueda) |
                Q(instagram__icontains=busqueda) |
                Q(telefono__icontains=busqueda) |
                Q(user__username__icontains=busqueda) |
                Q(domicilio__icontains=busqueda)
            )
        return queryset

class UsuariosUpdate(LoginRequiredMixin, UpdateView):
    model = Usuarios
    form_class= CustomUserCreationForm
    success_url = reverse_lazy('usuarios:usuarios_list')