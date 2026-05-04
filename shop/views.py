from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Artist
from .serializers import ProductSerializer, TopArtistSerializer, CustomTokenObtainPairSerializer  # ✅ CustomTokenObtainPairSerializer bhi import kar

# ✅ Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['GET'])
def topartist(request):
    artists = Artist.objects.filter(is_top=True)[:6]
    serializer = TopArtistSerializer(artists, many=True)
    return Response(serializer.data)