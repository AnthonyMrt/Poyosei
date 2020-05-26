from django.shortcuts import render
# from django.views import View
# from poyosei.forms import *
# from django.views.decorators.csrf import csrf_exempt
# from poyosei.models import *
# from poyosei.ressources import PlanteurResource, mouvementResource
# from tablib import Dataset
# import json

# @csrf_exempt

def rapport(request):
    return render(request, 'rapport/index.html', {"active_tab": "rapport"})
