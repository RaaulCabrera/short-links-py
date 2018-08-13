from django.shortcuts import render

import json

from django.http import JsonResponse
from django.http import HttpResponseBadRequest

from api.models import ShortLink

from os import urandom
from base64 import b32encode

def createShortURL(request):
    if request.method == 'POST':
        if not request.body:
            return HttpResponseBadRequest("Bad request")
        
        jsonRequest = None
        urllist = []
        try:
            jsonRequest = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return HttpResponseBadRequest("Bad request")
        
        if isinstance(jsonRequest, list):
            urllist = jsonRequest
        else:
            urllist.append(jsonRequest['url'])
        
        shortList = []
        for url in urllist:
            shortKey = b32encode(urandom(5)).decode('ascii')
            shortUrl =  'http://' + request.get_host() + '/' + shortKey
            shortLink = ShortLink(original=url, shortKey=shortKey)
            shortLink.save()
            shortList.append({
                'original': url,
                'short': shortUrl
            })
        return JsonResponse(shortList, safe=False)
    else:
        return HttpResponseBadRequest("Bad request")
