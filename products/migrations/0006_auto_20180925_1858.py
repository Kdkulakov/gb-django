# Generated by Django 2.0.3 on 2018-09-25 18:58

from django.db import migrations

CATEGORIES_DATA = [
    {'title': 'vegetable'},
    {'title': 'fruit'}
]

def create_detault_categories(apps, schema_editor):
    Category = apps.get_model('products', 'Category')

    for data in CATEGORIES_DATA:
        Category.objects.get_or_create(**data)

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_category'),
    ]

    operations = [
        migrations.RunPython(
            create_detault_categories,
            lambda x, y: (x, y)
        )
    ]
