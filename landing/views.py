from django.shortcuts import render, render_to_response, redirect
from django.http import Http404, HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('landing/index.html')
    context = {'title':'Welcome to Elephant Box'}
    return HttpResponse(template.render(context))
