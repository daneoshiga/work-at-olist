import pytest
import json

from core.models import Channel, Category


@pytest.fixture
def initial_data():
    data = {}
    data['channel'] = Channel.objects.create(name='testchannel')
    data['category'] = Category.objects.create(channel=data['channel'],
                                               name='Category 1')
    return data


@pytest.mark.django_db
class TestModel:
    def test_create_categories_from_list(self):
        categories = ['Books', 'National Literature', 'Science Fiction']
        created = Category.create_channel_categories(channel='testchannel',
                                                     categories=categories)
        assert created == len(categories)


@pytest.mark.django_db
class TestAPI:
    def test_get_channels_is_up(self, client, initial_data):
        response = client.get('/api/1/channels/')
        assert response.status_code == 200

    def test_get_channels_content(self, client, initial_data):
        content = [{
            'id': str(initial_data['channel'].pk),
            'channel': 'testchannel'
        }]
        response = client.get('/api/1/channels/')

        assert b'testchannel' in response.content
        assert content == json.loads(response.content.decode())

    def test_get_channels_categories_is_up(self, client, initial_data):
        categories = ['Books', 'National Literature', 'Science Fiction']
        Category.create_channel_categories(channel='testchannel',
                                           categories=categories)

        url = '/api/1/channel/{}/'.format(initial_data['channel'].pk)
        response = client.get(url)
        assert response.status_code == 200

    def test_get_channels_categories_content(self, client, initial_data):
        url = '/api/1/channel/{}/'.format(initial_data['channel'].pk)
        response = client.get(url)
        assert b'Category 1' in response.content

    def test_get_category_family_is_up(self, client, initial_data):
        url = '/api/1/category/{}/'.format(initial_data['category'].pk)
        response = client.get(url)
        assert response.status_code == 200

    def test_get_category_family_content(self, client, initial_data):
        category = initial_data['category']
        category_2 = Category.objects.create(channel=category.channel,
                                             parent=category,
                                             name='Category 2')
        Category.objects.create(channel=category.channel, name='Other Tree')

        content = [{'id': str(category.pk), 'category': category.name},
                   {'id': str(category_2.pk), 'category': category_2.name}]

        url = '/api/1/category/{}/'.format(category.pk)
        response = client.get(url)
        print(response.content)
        assert b'Category 2' in response.content
        assert b'Other Tree' not in response.content
        assert content == json.loads(response.content.decode())
