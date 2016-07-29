from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Channel(models.Model):
    """Channels (eg. marketplaces)"""
    name = models.CharField('Name', max_length=255)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    """Categories Tree Structure of each channel"""
    name = models.CharField('Name', max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True)
    channel = models.ForeignKey(Channel)

    def __str__(self):
        return self.name
