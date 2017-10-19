from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from core.models import BaseModel


class Category(BaseModel, MPTTModel):
    """
        Category Model
    """
    channel = models.ForeignKey(
        'channels.Channel',
        verbose_name=_('Channel'),
        related_name='categories',
        on_delete=models.CASCADE
    )

    parent = TreeForeignKey(
        'self',
        verbose_name=_('Parent'),
        related_name='children',
        on_delete=models.CASCADE,
        db_index=True,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):

        if self.parent:
            slug = slugify(f'{self.channel.slug}-{self.parent.name}-{self.name}')
        else:
            slug = slugify(f'{self.channel.slug}-{self.name}')
        self.slug = slug

        super(Category, self).save()

    class MPTTMeta:
        order_insertion_by = ['name']
