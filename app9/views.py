from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def jan(request):
    return HttpResponse ('<marquee><h1>MOEM CHESTUNAV MAAAA (VALLI)<h1/><marquee/>')
