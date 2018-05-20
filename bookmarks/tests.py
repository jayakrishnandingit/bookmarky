import json

from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_auth.utils import jwt_encode

from bookmarks.models import Bookmark
# Create your tests here.
User = get_user_model()


class BookmarkAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'jaytest', 'jaytest@example.com', 'password123.'
        )
        self.token = jwt_encode(self.user)

        self.user2 = User.objects.create_user(
            'jaytest2', 'jaytest2@example.com', 'password123.'
        )
        self.token2 = jwt_encode(self.user2)

    def test_api_access_without_credentials_fails(self):
        url = reverse('mybookmarks')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_saving_without_credentails_fails(self):
        data = {
            'title': 'Google for all search!',
            'link': 'https://google.co.in',
            'tags': ['google', 'search', 'www']
        }
        url = reverse('mybookmarks')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_saving_with_invalid_link_fails(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            'title': 'Google for all search!',
            'link': 'google.co.in',
            'tags': ['google', 'search', 'www']
        }
        url = reverse('mybookmarks')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_saving_with_existing_title_fails(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            'title': 'Google for all search!',
            'link': 'https://google.co.in',
            'tags': []
        }
        url = reverse('mybookmarks')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data.update({'link': 'https://google.com'})
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), {'title': ['Title already exists.']})

    def test_saving_with_existing_link_by_same_user_fails(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            'title': 'Google for all search!',
            'link': 'https://google.co.in',
            'tags': []
        }
        url = reverse('mybookmarks')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data.update({'title': 'Google'})
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), {'link': ['Link already exists.']})

    def test_saving_with_empty_required_values_fails(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            'title': '',
            'link': '',
            'tags': ['google', 'search', 'www']
        }
        url = reverse('mybookmarks')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_saving_with_invalid_data_fails(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            'iam_not_permitted': 'I am not permitted.',
            'link': 'https://google.co.in',
        }
        url = reverse('mybookmarks')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_saving_with_empty_tags_is_success(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            'title': 'Google for all search!',
            'link': 'https://google.co.in',
            'tags': []
        }
        url = reverse('mybookmarks')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_saving_existing_link_by_distinct_users_is_success(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            'title': 'Google for all search!',
            'link': 'https://google.co.in',
            'tags': []
        }
        url = reverse('mybookmarks')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # make sure the bookmark is saved under first user.
        bookmark = Bookmark.objects.get(pk=response.data['id'])
        self.assertEqual(bookmark.user.email, self.user.email)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token2)
        data = {
            'title': 'Google.',
            'link': 'https://google.co.in',
            'tags': ["search engine", "web"]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # make sure the bookmark is saved under second user.
        bookmark = Bookmark.objects.get(pk=response.data['id'])
        self.assertEqual(bookmark.user.email, self.user2.email)

    def test_saving_with_valid_values_is_success(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token)
        data = {
            'title': 'Google for all search!',
            'link': 'https://google.co.in',
            'tags': ['google', 'search', 'www']
        }
        url = reverse('mybookmarks')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # make sure the bookmark is saved under logged in user.
        bookmark = Bookmark.objects.get(pk=response.data['id'])
        self.assertEqual(bookmark.user.email, self.user.email)
