from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from django.template import Template, Context

from django.template.loader import get_template, render_to_string

from django.urls import reverse_lazy

from django.http import HttpResponse

from products.models import Product

from products.forms import ProductModelForm


def product_list(request):

    query = get_list_or_404(Product)

    return render(request, 'products/list.html', {'results': query})


def product_detail(request, title):

    obj = get_object_or_404(Product, title=title)

    return render(request, 'products/detail.html', {'instance': obj})


def product_create(request):

    success_url = reverse_lazy('products:list')

    form = ProductModelForm(request.POST)

    if request.method == 'POST':

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
