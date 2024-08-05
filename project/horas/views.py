from django.shortcuts import render
from .models import Horas
from .forms import HorasForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.db.models import Q
from django.urls import reverse_lazy

def index(request):
    return render(request, 'horas/index.html')

class HorasList(LoginRequiredMixin, ListView):
    model = Horas
    context_object_name = 'horas'

    def get_queryset(self):
        queryset = Horas.objects.all()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = queryset.filter(
                Q(usuario__usuarios__user__username__icontains=busqueda) |
                Q(horas__icontains=busqueda) |
                Q(mes__icontains=busqueda) |
                Q(dia__icontains=busqueda)
            )
        return queryset

class HorasDetail(DetailView):
    model = Horas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dia'] = self.object.get_dia_str() # type: ignore
        return context

class HorasCreate(CreateView):
    model = Horas
    form_class= HorasForm
    success_url = reverse_lazy('horas:horas_list')

class HorasUpdate(UpdateView):
    model = Horas
    form_class= HorasForm
    success_url = reverse_lazy('horas:horas_list')