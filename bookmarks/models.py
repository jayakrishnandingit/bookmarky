from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager


# Create your models here.
User = get_user_model()


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Bookmark(TimestampModel):
    title = models.CharField(_('Title'), max_length=200, null=False, blank=False)
    link = models.URLField(_('Link to site'), null=False, blank=False)
    user = models.ForeignKey(
        User,
        verbose_name=_('Bookmarked by'),
        related_name='bookmarks',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    tags = TaggableManager()
