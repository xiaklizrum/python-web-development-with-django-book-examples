import datetime

from django.contrib.auth.models import User
from django.db import models
from markdown import markdown

VIEWABLE_STATUS = [3, 4]


class ViewbleManager(models.Manager):
    def get_queryset(self):
        default_queryset = super().get_queryset()
        return default_queryset.filter(status__in=VIEWABLE_STATUS)


# Create your models here.


class Story(models.Model):
    STATUS_CHOICES = (
        (1, 'Need Edit'),
        (2, 'Need Approval'),
        (3, 'Published'),
        (4, 'Archived'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.SET_NULL)
    markdown_content = models.TextField()
    html_content = models.TextField(editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ['modified']
        verbose_name_plural = 'stories'

    def get_absolute_url(self):
        return '/cms/{}'.format(self.slug)

    def __str__(self):
        return self.title

    admin_objects = models.Manager()
    objects = ViewbleManager()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.html_content = markdown(self.markdown_content)
        self.modified = datetime.datetime.now()
        super().save(force_insert, force_update, using, update_fields)


class Category(models.Model):
    label = models.CharField(blank=True, max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.label
