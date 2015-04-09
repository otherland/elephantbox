from django.shortcuts import render, render_to_response, redirect
from django.views import generic
from . import models
from endless_pagination.decorators import page_template
from django.template import RequestContext

@page_template('blog/blog_entries.html')
def BlogIndex(
        request, template='blog/blog_index.html', extra_context=None):

    context = {
        'entries': models.Entry.objects.published().order_by('-created'),
        'request':request,
        'popular' : models.Entry.objects.published().order_by('-created')[:5],
        'title':'Elephant Box | Blog',
    }

    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(
        template, context, context_instance=RequestContext(request))


def BlogDetail(
        request, slug, template='blog/post.html', extra_context=None):

    context = {
        'object': models.Entry.objects.get(slug=slug),
        'request':request,
        'popular' : models.Entry.objects.published().order_by('-created')[:5],
        'current_path': request.build_absolute_uri(request.get_full_path()),
    }

    context['title'] = "Elephant Box | {}".format(context['object'].title)

    return render_to_response(
        template, context, context_instance=RequestContext(request))
