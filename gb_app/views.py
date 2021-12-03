from django.shortcuts import render, HttpResponse

def index_view(request):
    return HttpResponse('Welcome to FOE GB Calculator!')