from django.urls import path
from gallery.items.models import Item, Photo
from django.views.generic import TemplateView, ListView, DetailView

urlpatterns = [
    path(
        '',
        TemplateView.as_view(
            template_name='index.html',
            extra_context={'item_list': Item.objects.all()}
        ),
        name='index'
    ),
    path(
        'items/',
        ListView.as_view(
            template_name='items_list.html',
            queryset=Item.objects.all(),
            allow_empty=True
        ),
        name='item_list'
    ),
    path(
        'items/<int:pk>/',
        DetailView.as_view(
            template_name='items_detail.html',
            queryset=Item.objects.all(),
        ),
        name='item_detail'
    ),
    path(
        'photos/<int:pk>/',
        DetailView.as_view(
            template_name='photos_detail.html',
            queryset=Photo.objects.all(),
        ),
        name='photo_detail'
    )
]
