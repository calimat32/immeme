# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from creator.models import Meme

def create(request, meme_id):
    context = RequestContext(request,{})
    template = loader.get_template('creator/root.html')
    return HttpResponse(template.render(context))

def home(request):
    context = RequestContext(request,{'memes': Meme.objects.all() })
    template = loader.get_template('creator/home.html')
    return HttpResponse(template.render(context))
