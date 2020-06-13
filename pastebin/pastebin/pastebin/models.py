from django.db import models


# Create your models here.

class Paste(models.Model):
    SYNTAX_CHOICES = (
        (0, 'Plain'),
        (1, 'Python'),
        (2, 'HTML'),
        (3, 'SQL'),
        (4, 'Javascript'),
        (5, 'CSS'),
    )

    content = models.TextField()
    title = models.CharField(blank=True, max_length=30)
    syntax = models.IntegerField(choices=SYNTAX_CHOICES, default=0)
    poster = models.CharField(blank=True, max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return '{} ({})'.format(self.title or '#{}'.format(self.id),
                                self.get_syntax_display())

    def get_absolute_url(self):
        return '/paste/{}/'.format(self.id)
