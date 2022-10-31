from django.shortcuts import render,HttpResponse

# Create your views here.
def layout(request):
  return render(request,"layout.html")
