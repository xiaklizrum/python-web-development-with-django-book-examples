from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
import os


def _add_thumb(s):
    parts = s.split('.')
    parts.insert(-1, 'thumbs')
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return '.'.join(parts)


class ThumbnailImageFieldFile(ImageFieldFile):
    @property
    def thumb_path(self):
        return _add_thumb(self.path)

    @property
    def thumb_url(self):
        return _add_thumb(self.url)

    def save(self, name, content, save=True):
        super().save(name, content, save)
        img = Image.open(self.path)
        img.thumbnail(
            (self.field.thumb_width, self.field.thumb_height),
            Image.ANTIALIAS
        )
        img.save(self.thumb_path, 'JPEG')

    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)


class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super().__init__(*args, **kwargs)
