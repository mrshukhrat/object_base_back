# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer
from .serializers import RegionsSerializer
from .serializers import Objects_contractSerializer
from .serializers import Object_mainSerializer
from .models import Regions
from .models import Objects_contract
from .serializers import DistrictSerializer
from .models import District
from .models import Objects_main
from rest_framework import generics
from rest_framework import  permissions
from .permissions import IsProductOwner
from .permissions import IsObjectOwner
from .permissions import IsObjectContractOwner
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Objects_main.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsProductOwner]

class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Objects_main.objects.all()
    serializer_class = Object_mainSerializer
    permission_classes = [permissions.IsAuthenticated, IsObjectOwner]
    def get_queryset(self):
            queryset = Objects_main.objects.all()

            # Filter products based on query parameters
            name = self.request.query_params.get('name', None)
            category = self.request.query_params.get('category', None)
            # Add more filters as needed

            if name:
                queryset = queryset.filter(name__icontains=name)
            if category:
                queryset = queryset.filter(category__icontains=category)
            # Add more filters as needed

            return queryset

class ObjectContractViewSet(viewsets.ModelViewSet):
    queryset = Objects_contract.objects.all()
    serializer_class = Objects_contractSerializer
    permission_classes = [permissions.IsAuthenticated, IsObjectContractOwner]

class RegionsAPIView(generics.ListAPIView):
    queryset=Regions.objects.all()
    serializer_class=RegionsSerializer


class DistrictAPIView(generics.ListAPIView):
    queryset=District.objects.all()
    serializer_class=DistrictSerializer





class CustomerDetailAPIView(generics.RetrieveAPIView):
    """
    get all
    """
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    lookup_field = 'pk'



class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
