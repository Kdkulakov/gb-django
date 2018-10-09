from django.shortcuts import render, redirect

from products.models import Category

from products.forms import CategoryForm

def category_create(request):

    form = CategoryForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():

            title = form.cleaned_data.get('title')
            snippet = form.cleaned_data.get('snippet')

            Category.objects.create(
                title=title,
                snippet=snippet
            )

    return render(request, 'products/create.html', {'form': form})
