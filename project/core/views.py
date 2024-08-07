from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    usuario = User.objects.all()
    return render(request, 'core/index.html', {'usuario': usuario})