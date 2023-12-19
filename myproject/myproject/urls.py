# urls.py in myproject

from django.contrib import admin
# urls.py

from django.urls import path,include
from myapp.views import LoginView, UserMeView
from myapp.views import RegionsAPIView
from myapp.views import DistrictAPIView
from myapp.views import CustomerDetailAPIView

from rest_framework.routers import DefaultRouter
from myapp.views import ProductViewSet
from myapp.views import ObjectViewSet
from myapp.views import ObjectContractViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'objects', ObjectViewSet, basename='objects')
router.register(r'objects_contract', ObjectContractViewSet, basename='objects_contract')

urlpatterns = [
    path('api/v1/login/', LoginView.as_view(), name='login'),
    path('api/v1/user-me/', UserMeView.as_view(), name='user-me'),


    path('admin/', admin.site.urls),

    path('api/v1/', include(router.urls))
]
