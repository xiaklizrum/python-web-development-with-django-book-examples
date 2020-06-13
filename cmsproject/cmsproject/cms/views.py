from django.db.models import Q

from cmsproject.cms.models import Category, Story
from django.shortcuts import render, get_object_or_404


# Create your views here.


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    story_list = Story.objects.filter(category=category)
    heading = 'Category: {}'.format(category.label)
    return render(request, 'cms/story_list.html', locals())


def search(request):
    if 'q' in request.GET:
        term = request.GET['q']
        story_list = Story.objects.filter(Q(title__contains=term) |
                                          Q(markdown_content__contains=term))
        heading = 'Search results'
    return render(request, 'cms/story_list.html', locals())
