from django.urls import path
from django.views.generic import ListView, DetailView
from cmsproject.cms.models import Story
from cmsproject.cms.views import category, search

urlpatterns = [
    path('category/<slug:slug>', category, name='cms-category'),
    path('search/', search, name='cms-search'),
    path(
        '',
        ListView.as_view(
            queryset=Story.objects.all(), context_object_name='story_list'
        ),
        name='cms-home'
    ),
    path(
        '<slug:slug>/',
        DetailView.as_view(
            queryset=Story.objects.all(), context_object_name='story'
        ),
        name='cms-story'
    ),
]
