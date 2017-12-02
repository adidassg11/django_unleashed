#from django.shortcuts import render
from django.http.response import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, loader

from .models import Tag


def homepage(request):
    '''
    tag_list = Tag.objects.all()
    #output = ",".join([tag.name for tag in tag_list])
    context = {'tag_list': tag_list}
    #context = Context({'tag_list': tag_list})  # Book wants this, but it's borked
    template = loader.get_template('organizer/tag_list.html')
    output = template.render(context)
    return HttpResponse(output)
    '''
    return render_to_response('organizer/tag_list.html', {'tag_list': Tag.objects.all()})


def tag_detail(request, slug):
    '''
    try:
        tag = Tag.objects.get(slug__iexact=slug)
    except Tag.DoesNotExist:
        #return HttpResponseNotFound('<h1>Tag not found!</h1>')
        raise Http404
    '''
    # Shortcut for this ^^^
    tag = get_object_or_404(Tag, slug__iexact=slug)

    return render_to_response('organizer/tag_detail.html', {'tag': tag})

