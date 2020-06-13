from django.db import models


# Create your models here.


class Update(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '[{}] {}'.format(
            self.timestamp.strftime('%Y-%m-%d %H:%M:%S'), self.text
        )
