from django.contrib.auth.models import User
from .models import Product
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    price = serializers.IntegerField()
    description = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=50)
    image = serializers.CharField(max_length=1000)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category', 'image']

    def create(self, validated_data):
        '''
        Create and return a new `Product` instance, given the validated data.
        '''
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        '''
        Update and return an existing `Product` instance, given the validated data.
        '''
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
