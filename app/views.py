from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response
from models import *
from django.shortcuts import get_object_or_404
#from forms import *

# Create your views here.
def home(request):
	clientes = cliente.objects.all()
	productos = producto.objects.all()
	template = "index.html"
	return render_to_response(template, locals())