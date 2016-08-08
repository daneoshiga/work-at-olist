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
        previous = None
        for count, category in enumerate(categories, 1):
            previous, created = (Category.objects
                                 .get_or_create(channel=channel, name=category,
                                                parent=previous))
        return count

    def serializable_tree(self):
        "Generate a serializable structure from current node and children"
        obj = {'id': str(self.pk), 'category': self.name, 'children': []}
        for child in self.get_children():
            obj['children'].append(child.serializable_tree())
        return obj
