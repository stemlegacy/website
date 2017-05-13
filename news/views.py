from django.shortcuts import get_object_or_404,render
from news.models import event, speaker, memberss, images

# Create your views here.
all_members = memberss.objects.all()
galleryy = images.objects.all()

def members(request):
    context={"all_members":all_members}
    return render(request, "news/members.html",context)
def Open(request):
    return render(request,"news/index.html",{"all_members": all_members})
def about(request):
    return render(request,"news/about.html",{"all_members": all_members})
def activity(request):
    return render(request,"news/activities.html",{"all_members": all_members})
def gallery(request):
    return render(request,"news/gallery.html",{"galleryy": galleryy})
def final(request,member_id):
    spmember = memberss.objects.get(pk=member_id)
    return render(request, "news/sp_member.html",{"spmember":spmember,})

