from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import DeleteView, DetailView, ListView, UpdateView
from .models import Usuarios
from pagos.models import Pagos
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
            return redirect('core:index')
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
        queryset = Usuarios.objects.all()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = queryset.filter(
                Q(user__first_name__icontains=busqueda) |
                Q(user__last_name__icontains=busqueda) |
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

def perfil(request, pk):
    usuarios = get_object_or_404(Usuarios, id=pk)
    pagos = Pagos.objects.filter(usuario=usuarios)
    contexto = {
        'usuarios': usuarios,
        'proximo_vencimiento': usuarios.proximo_vencimiento,
        'pagos': pagos,
    }
    return render(request, 'usuarios/perfil.html', contexto)