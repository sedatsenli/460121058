from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def contact(request):
    return render(request,  'blog/contact.html')
    
def menu(request):
    return render(request, 'blog/menu.html')

def today_special(request):
    return render(request, 'blog/today-special.html')

#def base(request):
 #   return render(request, 'base.html')