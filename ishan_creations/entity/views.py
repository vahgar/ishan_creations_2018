from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import City, Business_Entity, Category
from django.core import serializers
from .forms import SearchForm
from functools import reduce
import operator

from django.db.models import Q

# Create your views here.
def list_city(request):

    Categories = Category.objects.all()
    Entity = Business_Entity.objects.all()
    form = SearchForm()
    context = {
      "category_list": Categories,
      "entity_list": Entity,
      "form": form,
    }
    return render(request, "categories.html", context)


def category_search(request):

    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['search']
            query_list = query.split()
            result = Business_Entity.objects.filter(
            reduce(operator.or_,
                       ( Q(name__icontains=q) for q in query_list)) |
            reduce(operator.or_,
                       ( Q(category__name__icontains=q) for q in query_list)) |
            reduce(operator.or_,
                       ( Q(services__icontains=q) for q in query_list)))
            print(result)
            context = {
              "Entities":result,
              "query": query
            }
        else:
            Categories = Category.objects.all()
            Entity = Business_Entity.objects.all()
            form = SearchForm()
            context = {
              "category_list": Categories,
              "entity_list": Entity,
              "form": form,
            }
            return render(request, "categories.html", context)


    return render(request, "results.html", context)


def category_wise(request, id):

    category = Category.objects.get(id=id)
    result = Business_Entity.objects.all().filter(category=category)
    context = {
      "Entities":result,
      "query": category,
    }
    return render(request, "results.html", context)

def entity_full(request, id):

    entity = Business_Entity.objects.get(id=id)
    context = {
        "Entity": entity,
    }
    return render(request, "entity_full.html", context)
