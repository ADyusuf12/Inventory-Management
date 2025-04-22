from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .models import Product
from django.contrib.auth.models import User

class ProductAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser2', password='password1234')
        self.client = APIClient()
        token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.product = Product.objects.create(
            name='Test Product 1',
            SKU='TP123',
            price=15.99,
            stock_quantity=36,
            description='Test product description',
            )
    
    def test_create_product(self):
        data = {
            'name': 'New Product 1',
            'SKU': 'NP124',
            'price': 20.99,
            'stock_quantity':50,
            'description': 'New product description',
        }
        response = self.client.post('/api/products/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_single_product(self):
        response = self.client.get(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)
        
    def test_update_product(self):
        data = {
            'name': self.product.name,
            'SKU': self.product.SKU,
            'price': 14,
            'stock_quantity': self.product.stock_quantity,
            'description': self.product.description,
            
            }
        response = self.client.put(f'/api/products/{self.product.id}/', data)  # Correct URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.price, 14)
        
        
    def test_delete_product(self):
        response = self.client.delete(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())
        
    def test_unauthenticated_access(self):
        self.client.logout()
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_invalid_product_creation(self):
        data = {
            'name': 'Invalid Product',
            'SKU': 'IP125',
            'price': -10.99,  # Invalid price
            'stock_quantity': -10, # Invalid stock quantity
            
        }
        response = self.client.post('/api/products/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)