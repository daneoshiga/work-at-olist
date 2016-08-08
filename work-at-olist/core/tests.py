import json

import pytest
from django.core.urlresolvers import reverse

from core.models import Category, Channel


@pytest.fixture
def initial_data():
    channel = Channel.objects.create(name='testchannel')
    category = Category.objects.create(channel=channel,
                                       name='Category 1')
    category_2 = Category.objects.create(channel=category.channel,
                                         parent=category, name='Category 2')

    return {'channel': channel, 'category': category, 'category_2': category_2}


@pytest.mark.django_db
class TestModel:
    def test_create_categories_from_list(self, initial_data):
        channel = initial_data['channel']
        categories = ['Books', 'National Literature', 'Science Fiction']
        created = Category.create_channel_categories(channel=channel,
                                                     categories=categories)
        assert created == len(categories)


@pytest.mark.django_db
class TestAPI:
    def test_get_channels_is_up(self, client, initial_data):
        url = reverse('core:channel_list')
        response = client.get(url)
        assert response.status_code == 200

    def test_get_channels_content(self, client, initial_data):
        url = reverse('core:channel_list')
        content = [{
            'id': str(initial_data['channel'].pk),
            'channel': 'testchannel'
        }]
        response = client.get(url)

        assert b'testchannel' in response.content
        assert content == json.loads(response.content.decode())

    def test_get_channels_categories_is_up(self, client, initial_data):
        channel = initial_data['channel']
        categories = ['Books', 'National Literature', 'Science Fiction']
        Category.create_channel_categories(channel=channel,
                                           categories=categories)

        url = reverse('core:category_list',
                      kwargs={'channel': initial_data['channel'].pk})

        response = client.get(url)
        assert response.status_code == 200

    def test_get_channels_categories_content(self, client, initial_data):
        channel = initial_data['channel']
        category = initial_data['category']
        category_2 = initial_data['category_2']

        url = reverse('core:category_list',
                      kwargs={'channel': channel.pk})

        response = client.get(url)

        content = [{'id': str(category.pk), 'category': category.name,
                    'children': [{
                        'id': str(category_2.pk), 'category': category_2.name,
                        'children': []
                    }]}]
        assert content == json.loads(response.content.decode())

    def test_get_category_family_is_up(self, client, initial_data):
        category = initial_data['category']

        url = reverse('core:category_family',
                      kwargs={'category_id': category.pk})

        response = client.get(url)
        assert response.status_code == 200

    def test_get_category_family_content(self, client, initial_data):
        category = initial_data['category']
        category_2 = initial_data['category_2']
        Category.objects.create(channel=category.channel, name='Other Tree')

        content = [{'id': str(category.pk), 'category': category.name},
                   {'id': str(category_2.pk), 'category': category_2.name}]

        url = reverse('core:category_family',
                      kwargs={'category_id': category.pk})
        response = client.get(url)
        assert b'Category 2' in response.content
        assert b'Other Tree' not in response.content
        assert content == json.loads(response.content.decode())
