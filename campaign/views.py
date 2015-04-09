from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext, loader
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse

def contact(request):
    payload = {
        'errors' : [],
        'success' : False,
    }
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            payload['errors'].append('Please enter your email address.')
        if not request.POST.get('message', ''):
            payload['errors'].append('Please enter your message.')
        #if request.POST.get('email') and '@' not in request.POST['email']:
            #payload['errors'].append('Enter a valid e-mail address.')
        if not payload['errors']:
          try:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'support@test.com'),
                ['twittomyates@gmail.com'],
            )
            payload['success'] = True
          except Exception, err:
            raise
    print payload
    return render(request, 'campaign/contact.html', payload)

def index(request):
    template = loader.get_template('campaign/index.html')
    context = {'title':'Elephant Box | Home'}
    return HttpResponse(template.render(context))

def about(request):
    template = loader.get_template('campaign/about.html')
    context = {'title':'Elephant Box | About'}
    return HttpResponse(template.render(context))

def care(request):
    template = loader.get_template('campaign/care.html')
    context = {'title':'Elephant Box | Customer Care'}
    return HttpResponse(template.render(context))

def giving(request):
    template = loader.get_template('campaign/giving.html')
    context = {'title':'Elephant Box | Giving Back'}
    return HttpResponse(template.render(context))

def faq(request):
    template = loader.get_template('campaign/faq.html')
    context = {'title':'Elephant Box | FAQs'}
    return HttpResponse(template.render(context))

def shop(request):
    template = loader.get_template('campaign/shop.html')
    context = {'title':'Elephant Box | Shop'}
    return HttpResponse(template.render(context))
