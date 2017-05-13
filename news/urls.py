__author__ = 'Ali Shosha'
from django.conf.urls import  url
from . import views
app_name = "news"

urlpatterns = [
    url(r'^$',views.Open,name="Open"),
    url(r'^about/', views.about,name="about"),
    url(r'^Home/', views.Open, name="Home"),
    url(r"^activity/", views.activity, name="activity"),
    url(r"^members/", views.members, name="members"),
    url(r"(?P<member_id>[0-9]+)/$", views.final, name="final"),
    url(r"^gallery/", views.gallery, name="gallery"),
]