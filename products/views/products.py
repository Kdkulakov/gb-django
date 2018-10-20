from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from django.template import Template, Context

from django.template.loader import get_template, render_to_string

from django.urls import reverse_lazy

from django.http import HttpResponse

from products.models import Product

from products.forms import ProductModelForm

from django.views import View

from django.views.generic import (FormView, CreateView, UpdateView, DeleteView, DetailView, ListView)



class ProductList(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'results'

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'instance'
    slug_field = 'title'

    # def get_object(self, *args, **kwargs):
    #     # get_object_or_404(self.model, pk=kwargs['pk'], title__startswith='S')
    #     get_object_or_404(self.model, pk=kwargs['pk'], is_active=True)


class ProductGenericCreate(CreateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:list')


class ProductGenericUpdate(UpdateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:list')
    slug_field = 'title'

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')
    template_name = 'products/delete.html'
    slug_field = 'title'

class ProductCreate(View):
    def get(self, request):
        form = ProductModelForm(
        )
        return render(request, 'products/create.html', {'form': form})

    def post(self, request):
        success_url = reverse_lazy('products:list')
        form = ProductModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(success_url)

        return render(request, 'products/create.html', {'form': form})


class ProductUpdate(FormView):
    form_class = ProductModelForm
    success_url = reverse_lazy('products:list')
    template_name = 'products/create.html'

    def post(self, request, title):
        obj = get_object_or_404(Product, title=title)
        form = self.form_class(
            request.POST,
            instance=obj
        )

        if form.is_valid():
            form.save()

            return redirect(self.success_url)

        return render(request, 'products/create.html', {'form': form})


def product_list(request):

    query = get_list_or_404(Product)

    return render(request, 'products/list.html', {'results': query})


def product_detail(request, title):

    obj = get_object_or_404(Product, title=title)

    return render(request, 'products/detail.html', {'instance': obj})


def product_create(request):

    success_url = reverse_lazy('products:list')

    form = ProductModelForm(request.POST)

    if form.is_valid():

        form.save()

        return redirect(success_url)

    return render(request, 'products/create.html', {'form': form})


def product_update(request, title):

    success_url = reverse_lazy('products:list')

    obj = get_object_or_404(Product, title=title)

    form = ProductModelForm(instance=obj)

    if request.method == 'POST':

        form = ProductModelForm(
            request.POST,
            instance=obj
        )

        if form.is_valid():

            form.save()

            return redirect(success_url)

    return render(request, 'products/create.html', {'form': form})
