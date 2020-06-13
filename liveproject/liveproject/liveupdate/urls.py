from django.urls import path
from django.views.generic import ListView
from liveproject.liveupdate.views import updates_after
from liveproject.liveupdate.models import Update

urlpatterns = [
    path('', ListView.as_view(queryset=Update.objects.all())),
    path('updates-after/<int:id>/', updates_after),
]
