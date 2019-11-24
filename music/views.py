from django.http import HttpResponse
from . models import  Album
from django.shortcuts import Http404,render
from django.template import loader
# Create your views here.
def index(request):
    albums=Album.objects.all()
    template=loader.get_template("music/index.html")
    context={
        'albums':albums,
    }
    return HttpResponse(template.render(context,request))

def details(request,album_id):

    try:
        album=Album.objects.get(pk=album_id)

    except Album.DoesNotExist:
        raise Http404("something is wrong")
    return render(request,"music/details.html",{'album':album})