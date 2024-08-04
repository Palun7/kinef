from django.shortcuts import render
from .forms import GastosForm
from .models import Gastos
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView
from django.db.models import Q
from django.urls import reverse_lazy
from django.db.models import Sum


def index(request):
    return render(request,'gastos/index.html')

class GastosList(LoginRequiredMixin, ListView):
    model = Gastos
    context_object_name = 'gastos'

    def get_queryset(self):
        queryset = Gastos.objects.all()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = queryset.filter(
                Q(usuario__usuarios__user__username__icontains=busqueda) |
                Q(monto__icontains=busqueda) |
                Q(concepto__icontains=busqueda) |
                Q(mes__icontains=busqueda) |
                Q(fijo_variable__icontains=busqueda)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calcular el total de los gastos
        total_gastos = self.get_queryset().aggregate(Sum('monto'))['monto__sum'] or 0
        context['total_gastos'] = total_gastos
        return context

class GastosCreate(CreateView):
    model = Gastos
    form_class= GastosForm
    success_url = reverse_lazy('gastos:gastos_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class GastosUpdate(UpdateView):
    model = Gastos
    form_class= GastosForm
    success_url = reverse_lazy('gastos:gastos_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

