from django.urls import path
from . import views

app_name="music"
urlpatterns = [
    path('', views.index,name="index"),
    path('<int:album_id>/',views.details,name="details"),
    path('album/add',views.AlbumView.as_view(),name="add")

]