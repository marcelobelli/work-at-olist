from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


class Channel(BaseModel):
    """
    Channel Model
    """
    name = models.CharField(_('Name'), max_length=50, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Channel, self).save()
