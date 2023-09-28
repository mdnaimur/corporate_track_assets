from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from base.models import Product_Assets

# ? Route declaration


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET/api',
        'GET/api/products',
        'GET/api/products/:id',
    ]
    return Response(routes)


# find all products
@api_view(['GET'])
def getProducts(request):
    product = Product_Assets.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

# get one product


@api_view(['GET'])
def getProduct(request, pk):
    product = Product_Assets.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
