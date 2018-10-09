from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from django.template import Template, Context

from django.template.loader import get_template, render_to_string

from django.urls import reverse_lazy

from django.http import HttpResponse

from . import models

from . import forms


def product_list(request):

    query = get_list_or_404(models.Product)

    return render(request, 'products/list.html', {'results': query})


def product_detail(request, title):

    obj = get_object_or_404(models.Product, title=title)

    return render(request, 'products/detail.html', {'instance': obj})


def category_create(request):

    form = forms.CategoryForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():

            title = form.cleaned_data.get('title')
            snippet = form.cleaned_data.get('snippet')

            models.Category.objects.create(
                title=title,
                snippet=snippet
            )
    
    return render(request, 'products/create.html', {'form': form})


def product_create(request):

    success_url = reverse_lazy('products:list')

    form = forms.ProductModelForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():

            form.save()

            return redirect(success_url)

    return render(request, 'products/create.html', {'form': form})


def product_update(request, title):

    success_url = reverse_lazy('products:list')

    obj = get_object_or_404(models.Product, title=title)

    form = forms.ProductModelForm(instance=obj)

    if request.method == 'POST':

        form = forms.ProductModelForm(
            request.POST,
            instance=obj
        )

        if form.is_valid():

            form.save()

            return redirect(success_url)

    return render(request, 'products/create.html', {'form': form})


def native(request):

    template = Template('Hello {{ name }}')

    context = Context({'name': 'Anton'})

    response_string = template.render(context)

    return HttpResponse(response_string)


def get_list_template(request):

    context = {
        'results': [
            'apple',
            'banana',
            'apricot'
        ]
    }

    template = get_template('products/list.html')

    return HttpResponse(template.render(context))


def render_list_to_string(request):

    context = {
        'results': [
            'apple',
            'banana',
            'apricot'
        ]
    }

    return HttpResponse(render_to_string('products/list.html', context))

