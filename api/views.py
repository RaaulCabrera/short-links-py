from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseBadRequest

def create(request):
    if request.method == 'POST':
        if not request.body:
            return HttpResponseBadRequest("Bad request")
        
    else:
        return HttpResponseBadRequest("Bad request")
