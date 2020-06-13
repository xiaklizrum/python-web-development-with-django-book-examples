from django.urls import path
from django.views.generic import DetailView, ListView, CreateView
from pastebin.pastebin.models import Paste

urlpatterns = [
    path('', ListView.as_view(queryset=Paste.objects.all()), name='index'),
    path('<int:pk>/', DetailView.as_view(queryset=Paste.objects.all())),
    path(
        'add/',
        CreateView.as_view(
            model=Paste,
            fields=['content', 'title', 'syntax', 'poster']
        )
    ),
]
