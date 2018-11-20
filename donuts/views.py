from django.shortcuts import render, get_object_or_404
from donuts.models import Donut
from django.db.models import Q
from django.http import HttpResponse
from itertools import chain

def site_mainPage(request):
    firstDonuts=Donut.objects.filter(isSpecial=True).order_by('price')[:4]
    if len(firstDonuts)<4:
        firstDonuts = list(chain(firstDonuts,Donut.objects.filter(onSale=True).order_by('price')[:4-len(firstDonuts)]))
        if len(firstDonuts)<4:
            firstDonuts = chain(firstDonuts,Donut.objects.filter(Q(onSale=False) & Q(isSpecial=False)).order_by('price')[:4-len(firstDonuts)])
    return render(request, 'site_mainPage.html', {'firstDonuts':firstDonuts})

def site_allPage(request):
    return render(request, 'site_allPage.html', {})

def site_donutPage(request, nameID):
    donut=get_object_or_404(Donut,pk=nameID)
    return render(request, 'site_donutPage.html', {'donut':donut})
