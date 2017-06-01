from django.shortcuts import render
from django.http import HttpResponse
from rango2.models import Category
def about(request):
    return HttpResponse("Rango says here is the about page.<br/> <a href='/rango2/'> Click Here </a> .")
# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
