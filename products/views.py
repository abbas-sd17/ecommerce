from django.http import HttpResponse

from django.shortcuts import render

from products.models import Products


# Create your views here.
def hello(request):
    data= Products.objects.all()
    d=data[0]
    print(data[0].name)
    d.name="Apple"
    d.save()
    data=Products.objects.all()
    print( d.name)

    return HttpResponse("hello world")
