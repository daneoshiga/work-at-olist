import pytest

from core.models import Channel, Category


@pytest.mark.django_db
def test_create_categories_from_list():
    Channel.objects.create(name='testchannel')
    categories = ['Books', 'National Literature', 'Science Fiction']
    created = Category.create_channel_categories(channel='testchannel',
                                                 categories=categories)
    assert created == len(categories)
