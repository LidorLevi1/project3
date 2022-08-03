from rest_framework import serializers
from .models import Category,Orders,Dish

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','imageUrl']


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id','name','price','description','imageUrl','isGlutenFree','isVegeterian','category']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category'] = CategorySerializer(instance.category).data
        return data

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
      

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['dishes'] = DishSerializer(instance.dishes,many=True).data
        return data   