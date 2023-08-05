from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from .models import Product
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, ProductSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def user_list(request):
        """
        List all code users, or create a new user.
        """
        if request.method == 'GET':
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return JsonResponse(serializer.data, safe=False)
    
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
    
    def user_detail(request, pk):
        """
        Retrieve, update or delete a code user.
        """
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse(status=404)
    
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)
    
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = UserSerializer(user, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
    
        elif request.method == 'DELETE':
            user.delete()
            return HttpResponse(status=204)

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be added,deleted or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]

    @csrf_exempt
    def product_list(request):
        """
        List all code products, or create a new product.
        """
        if request.method == 'GET':
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return JsonResponse(serializer.data, safe=False)
    
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        
    @csrf_exempt
    def product_detail(request, pk):
        """
        Retrieve, update or delete a code product.
        """
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return HttpResponse(status=404)
    
        if request.method == 'GET':
            serializer = ProductSerializer(product)
            return JsonResponse(serializer.data)
    
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ProductSerializer(product, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
    
        elif request.method == 'DELETE':
            product.delete()
            return HttpResponse(status=204)