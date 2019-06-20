from django.shortcuts import render
from .models import Marker
from django.http import HttpResponseRedirect
import urllib.request, json


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def squadup(request):
    all_marker_items = Marker.objects.all()
    marker_nums = []
    for marker in all_marker_items:
        search_string = marker.marker_coord.replace(" ", "+")
        with urllib.request.urlopen(f"https://maps.googleapis.com/maps/api/geocode/json?address={search_string}&key=") as url:
            data = json.loads(url.read().decode())
        marker_nums.append([data["results"][0]["geometry"]["location"]["lat"], data["results"][0]["geometry"]["location"]["lng"]])

    return render(request, 'squadup.html',
                  {'marker_nums': marker_nums, 'all_items': all_marker_items})

def addMarker(request):
    new_item = Marker(marker_coord=request.POST['marker_coord'])
    new_item.save()
    return HttpResponseRedirect('../squadup')

def deleteMarker(request, Marker_id):
    item_to_delete = Marker.objects.get(id=Marker_id)
    item_to_delete.delete()
    return HttpResponseRedirect('../../squadup')
