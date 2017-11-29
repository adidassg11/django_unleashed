#from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import Context, loader

from .models import Tag


def homepage(request):
    tag_list = Tag.objects.all()
    #output = ",".join([tag.name for tag in tag_list])

    context = {'tag_list': tag_list}
    #context = Context({'tag_list': tag_list})  # Book wants this, but it's borked
    template = loader.get_template('organizer/tag_list.html')

    output = template.render(context)

    return HttpResponse(output)


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    template = loader.get_template(
        'organizer/tag_detail.html')

    context = Context({'tag': tag})

    return HttpResponse(template.render(context))