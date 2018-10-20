from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from products.models import Product


def product_list(request):
    query = get_list_or_404(Product)
    data = map(lambda itm: {
        'title': itm.title,
        'category': itm.category.title,
        'image': itm.image.value.url,
        'snippet': itm.snippet,
        'cost': itm.cost,
        'modified': itm.modified,
        'created': itm.created

    }, query)
    return JsonResponse({'results': list(data), 'count': len(query)})