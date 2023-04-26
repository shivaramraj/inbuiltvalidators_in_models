from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
from app.forms import *

def Topic_Insert(request):
    TO=TopicForm()
    d={'TO':TO}

    if request.method=='POST':
        TOD=TopicForm(request.POST)
        if TOD.is_valid():
            return HttpResponse('its a valid data')
        else:
            return HttpResponse('NOT VALID DATA')
    return render (request,'Topic_Insert.html',d)