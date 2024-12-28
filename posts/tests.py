# from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_post(self):
        adam = User.objects.get(username='adam')
        Post.objects.create(owner=adam, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test__logged_out_user_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTest(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        bob = User.objects.create_user(username='bob', password='pass')
        Post.objects.create(owner=adam, title='a title')
        Post.objects.create(owner=bob, title='another title')

    def test_user_can_retrieve_a_post_with_valid_id(self):
        response = self.client.get('/posts/1')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_retrieve_a_post_with_invalid_id(self):
        response = self.client.get('/posts/999')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_post_they_own(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/posts/1', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_post_they_dont_own(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/posts/2', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
