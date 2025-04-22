from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.exceptions import NotFound
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated to access this view
    
class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    
