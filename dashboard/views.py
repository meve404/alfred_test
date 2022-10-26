from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.utils import timezone
import random
import json

def DashHome(request):
    now = timezone.now()
    with open("jobs/points/points.json", "r+") as jsonFile:
        data = json.load(jsonFile)
    return HttpResponse(f'''<h1>Hola Alfred! los datos de points.json se han actualizan cada minuto:</h1><br>
                            <h2>Última actualización: {now}</h2>
                            <p>datos: {data}</p>'''
                        )