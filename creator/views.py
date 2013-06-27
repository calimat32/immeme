# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from creator.models import Meme
from django.shortcuts import get_object_or_404
from forms import MacroForm
import sys

sys.path.append('..')

from imgbackend import caption

def create(request, meme_id):
    meme = get_object_or_404(Meme, pk=meme_id)
    if request.method == 'POST':
        form = MacroForm(request.POST)
        if form.is_valid():
            top_text = form.cleaned_data['top_text'] 
            bottom_text = form.cleaned_data['bottom_text']
            image = caption.write_on_image64("../immeme/creator/static/images/%s" % meme.background_file, 
                               top_text, bottom_text)
            return HttpResponse('<img src="data:image/png;base64,' + image + '">')
    else:
        form = MacroForm()
    context = RequestContext(request,{"meme": meme, "form": form})
    template = loader.get_template('creator/create.html')
    return HttpResponse(template.render(context))

def home(request):
    context = RequestContext(request,{'memes': Meme.objects.all() })
    template = loader.get_template('creator/home.html')
    return HttpResponse(template.render(context))
