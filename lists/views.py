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


class Employee:
    def atributes(self):
        pass


def hire_candidate(candidate: Employee) -> str:
    if candidate.atributes in [
        "motivated",
        "creative",
        "funny"
    ]:
        return "".join("to US!")
