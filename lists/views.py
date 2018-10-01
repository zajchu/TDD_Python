from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from lists.models import Item


# Create your views here.


def home_page(request: HttpRequest):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
