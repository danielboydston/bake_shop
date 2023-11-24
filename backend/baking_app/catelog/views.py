from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Product


class IndexView(generic.ListView):
    template_name = "catelog/index.html"
    context_object_name = "product_list"

    def get_queryset(self):
        return Product.objects


class DetailView(generic.DetailView):
    model = Product
    template_name = "catelog/detail.html"

