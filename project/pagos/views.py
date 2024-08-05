from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView
from .models import Pagos
from django.db.models import Q
from .forms import PagosForm
from django.urls import reverse_lazy




def index(request):
    return render(request, 'pagos/index.html')

class PagosList(LoginRequiredMixin, ListView):
    model = Pagos
    context_object_name = 'pagos'

    def get_queryset(self):
        queryset = Pagos.objects.all()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = queryset.filter(
                Q(usuario__user__username__icontains=busqueda) |
                Q(monto__icontains=busqueda) |
                Q(modo_pago__icontains=busqueda) |
                Q(pase__icontains=busqueda) |
                Q(actividad__icontains=busqueda)
            )
        return queryset

class PagosCreate(CreateView):
    model = Pagos
    form_class= PagosForm
    success_url = reverse_lazy('pagos:pagos_list')

class PagosUpdate(LoginRequiredMixin, UpdateView):
    model = Pagos
    form_class= PagosForm
    success_url = reverse_lazy('pagos:pagos_list')