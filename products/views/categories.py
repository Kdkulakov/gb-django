from django.shortcuts import render, redirect, get_object_or_404

from products.models import Category

from django.views.generic import (FormView, CreateView, UpdateView, DeleteView, DetailView, ListView)
from django.urls import reverse_lazy
from products.forms import CategoryModelForm


def index(request):
    return render(request, 'categories/list.html')


class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:list')


class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:list')
    slug_field = 'title'


class CategoryDelete(DeleteView):
    model = Category
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:list')
    slug_field = 'title'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'products/list.html'
    context_object_name = 'results'
    slug_field = 'title'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        instance = context.get('object')
        context[self.context_object_name] = instance.product_set.all()
        return context


# def category_create(request):
#
#     form = CategoryForm(request.POST)
#
#     if request.method == 'POST':
#
#         if form.is_valid():
#
#             title = form.cleaned_data.get('title')
#             snippet = form.cleaned_data.get('snippet')
#
#             Category.objects.create(
#                 title=title,
#                 snippet=snippet
#             )
#
#     return render(request, 'products/create.html', {'form': form})
