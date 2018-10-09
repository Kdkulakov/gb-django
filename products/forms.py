from django import forms

from products.models import Category, Product

from images.models import Image


class CategoryForm(forms.Form):

    title = forms.CharField(
        label='title',
        widget=forms.widgets.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    snippet = forms.CharField(
        label='snippet',
        required=False,
        widget=forms.widgets.Textarea(
            attrs={'class': 'form-control'}
        )
    )


class ProductForm(forms.Form):

    title = forms.CharField(
        label='title',
        widget=forms.widgets.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all()
    )

    image = forms.ModelChoiceField(
        queryset=Image.objects.all()
    )

    snippet = forms.CharField(
        label='snippet',
        required=False,
        widget=forms.widgets.Textarea(
            attrs={'class': 'form-control'}
        )
    )

    cost = forms.DecimalField(
        label='cost',
        required=False,
        widget=forms.widgets.NumberInput(
            attrs={'class': 'form-control'}
        )
    )


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'image', 'snippet', 'cost']
