# Generated by Django 2.0.3 on 2018-09-28 16:24

from django.db import migrations


def create_detault_image(apps, schema_editor):
    Image = apps.get_model('images', 'Image')
    Image.objects.create(
        name='default',
        value='default.png'
    )

class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_detault_image,
            lambda x, y: (x, y)
        )
    ]