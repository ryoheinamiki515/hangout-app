from django.shortcuts import render
from django.http import HttpResponse


def myView(request):
    return render(request, 'example.html')

