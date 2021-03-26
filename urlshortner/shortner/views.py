from django.shortcuts import render, HttpResponse , redirect
import uuid
from .models import Link
# Create your views here.

def index(request) :
    return render(request, 'index.html') 


def create(request) : 
    if request.method == 'POST' :
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5] 
        new_url = Link(url = url , uuid = uid)
        new_url.save() 
        return HttpResponse(uid)

def go(request, pk) :
    url_detail = Link.objects.get(uuid=pk)
    return redirect(url_detail.url)