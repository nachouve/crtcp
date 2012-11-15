# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from upais.models import upai

def upai_list(request):
    upais_qs = upai.objects
    return render(request, 'upais/list.html', {'upai_list': upais_qs})

def upai_card(request, upai_id):
    upai_qs = upai.objects.filter(id__exact=upai_id)
    upai_qs = upai_qs[0]
    return render(request, 'upais/card.html', {'upai': upai_qs})
