import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    """
    Base model for Channel and Category
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('Name'), max_length=50)
    slug = models.SlugField(_('Slug'), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
