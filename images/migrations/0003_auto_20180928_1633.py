# Generated by Django 2.0.3 on 2018-09-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20180928_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
