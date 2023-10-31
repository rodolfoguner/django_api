from rest_framework import status
from rest_framework.test import APITestCase
from category.models import Category
from django.urls import reverse


class CategoryTesteCase(APITestCase):
    
    def setUp(self) -> None:
        self.list_url = reverse('category-list')
        self.category = Category.objects.create(name='Controle acesso')
        self.category = Category.objects.create(name='CFTV')
        
    def test_request_get_category(self):
        """Test to validate GET of category"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_request_post_create_category(self):
        """Test to validate POST to create category"""
        data = {
            'name': 'Seguranca'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_request_put_category_deny(self):
        """Test to validate PUT request denied"""
        data = {
            'name': 'Teste'
        }
        response = self.client.put('/category/1/', data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_request_delete_category(self):
        """Test to validate DELETE category"""
        response = self.client.delete('/category/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    