import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from .models import Features

# Create your views here.
def index(request):

    features=Features.objects.all()
    return render(request, 'index.html', {'features':features})

def counter(request):
    words=request.POST['words'] #words, because the name of collactor is words in html file
    amount_of_words=len(words.split())
    return render(request, 'counter.html',{'amount':amount_of_words})
