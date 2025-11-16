from django.shortcuts import render

from notes.models import Notes

# Create your views here.
def SubmitNotes(request):
    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        Notes.objects.create(title=title,content=content)
    return render(request,'forms.html')
def ShowNotes(request):
    data=Notes.objects.all()
    return render(request,'show.html',{'data':data})