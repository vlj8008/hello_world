from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    countries = ["Iran", "Iraq", "India", "Australia", "USA", "England"]
    context = {
        'countries': countries,
    }
    return render(request, "home.html", context)