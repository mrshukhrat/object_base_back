# serializers.py

from rest_framework import serializers
from .models import Regions
from .models import District
from .models import Product
from .models import Objects_main

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']


class Object_mainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objects_main
        fields = [
                'id',
                'name',
                'object_type_id',
                'object_goal_id',
                'object_desk_id',
                'object_desk1_id',
                'images',
                'contracts_file',
                'object_age',
                'regions',
                'district',
                'address',
                'k_number',
                'author',
                'lat',
                'lng',
                'surface',
                'area',
                'gas',
                'water',
                'electricity',
                'Rented',
                'contracts',
                'marked',
                'district_name',
                'regions_name'
        ]

class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Regions
        fields = ['id','title']

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id','title','regions_id']


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','first_name','last_name')
