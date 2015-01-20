from django.shortcuts import render_to_response
from equipo.models import Equipo
# Create your views here.

def home(request):
	entradas = Equipo.objects.all()[:10]
	return render_to_response('index.html', {'equipos':entradas})