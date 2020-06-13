from django.core import serializers
from django.http import HttpResponse
from liveproject.liveupdate.models import Update


# Create your views here.


def updates_after(request, id):
    response = HttpResponse()
    response['Content-Type'] = 'text/javascript'
    response.write(serializers.serialize('json', Update.objects.filter(pk__gt=id)))
    return response
