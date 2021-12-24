from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse('This are the projects')

def project(request, pk):
    return HttpResponse('this is a single project' + ' ' + str(pk))
