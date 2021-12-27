from django.shortcuts import render
from django.http import HttpResponse
from alla.models import EpData

# Create your views here.

def home(req,num):
    epd = EpData.objects.get(epnum=num)
    context = {
        'epd': epd
    }
    return render(req, 'alla/alla.html', context)

def api(req,num):
    epd = EpData.objects.get(epnum=num)
    html = f'<div class="card text-center text-white bg-dark m-2"><div class="card-header py-1">Episode - {epd.epnum}</div><div class="card-body py-2"><h5 class="card-title">{epd.name}</h5><p class="card-text">{epd.details}</p></div><div class="card-footer text-muted py-1">{epd.date}</div></div>'
    return HttpResponse(html)