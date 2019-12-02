from django.http import HttpResponse
from . models import  Album,Song
from django.shortcuts import Http404,render,get_object_or_404
from django.template import loader
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.
def index(request):
    albums=Album.objects.all()
    template=loader.get_template("music/index.html")
    context={
        'albums':albums,
    }
    return HttpResponse(template.render(context,request))

#generic views can also bu used and functions are replaced by classes
#from django.views import generic
# class Index(generic.listview):
# template_name= template loc

# def get_queryset():
#return Album.objects.all()

def details(request,album_id):

    try:
        album=Album.objects.get(pk=album_id)

    except Album.DoesNotExist:
        raise Http404("something is wrong")
    return render(request,"music/details.html",{'album':album})

def favourite(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    try:
        selectedsong=album.song_set.get(pk=request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request, "music/details.html", {'album': album},
                      {'error_message':"something wrong"},)
    else:
        selectedsong.isfavourite=True
        selectedsong.save()
        return render(request, "music/details.html", {'album': album})

class AlbumView(CreateView):
        model=Album
        fields=['albumname','artist','genre','albumlogo']