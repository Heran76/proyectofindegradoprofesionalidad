from django.http import HttpResponse
from django.template import loader
from .models import Persona
from django.http import Http404
from django.shortcuts import render

def index(request):
    personas_list = Persona.objects.order_by("-pub_date")[:5]
    template = loader.get_template("cvs/index.html")
    context = {
        "personas_list": personas_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, persona_id):
    try:
        persona = Persona.objects.get(pk=persona_id)
    except Persona.DoesNotExist:
        raise Http404("La persona no existe")
    return render(request, "cvs/detail.html", {"persona": persona})
# Create your views here.
