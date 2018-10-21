from django.contrib import admin
from django.utils.safestring import mark_safe

from django.template.loader import render_to_string


from products.models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'picture',
        'title',
        'category',
        'cost',
        'created',
        'modified'
    ]

    list_filter = [
        'category',
        'image',
        'created',
        'modified'

    ]

    search_fields = [
        'title',
        'snippet'
    ]


    def picture(self, obj):
        return render_to_string('products/componets/picture.html', {'image': obj.image.value.url})

    def name(self, obj):
        return obj.title.title()

    fieldsets = (           # разбиение на секции в админке и скрытия полей
        (
            'Data', {
                'fields': ('title', 'image', 'category')
            },
        ),
        (
            'Content', {
                'fields': ('image', 'snippet', 'cost')
            }
        )
    )


class ProductInline(admin.TabularInline):
    model = Product
    fk_name = 'category'

#admin.site.register(models.Product, ProductAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created',
        'modified'
    ]

    list_filter = [
        'created',
        'modified'

    ]

    search_fields = [
        'title',
        'snippet'
    ]

    inlines = [
        ProductInline           # выведение продуктов редактируемым списком в категории
    ]
