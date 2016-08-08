import uuid
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class OlistBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Channel(OlistBaseModel):
    """Channels (eg. marketplaces)"""
    name = models.CharField('Name', max_length=255, blank=False)

    def __str__(self):
        return self.name


class Category(OlistBaseModel, MPTTModel):
    """Categories Tree Structure of each channel"""
    name = models.CharField('Name', max_length=255, blank=False)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True)
    channel = models.ForeignKey(Channel)

    def __str__(self):
        return self.name

    @classmethod
    def create_channel_categories(self, channel, categories):
        """Create a Category tree given a channel name and category list
        """
        channel, _ = Channel.objects.get_or_create(name=channel)
        previous = None
        count = 0
        for category in categories:
            previous, created = (Category.objects
                                 .get_or_create(channel=channel, name=category,
                                                parent=previous))
            if created:
                count += 1
        return count
