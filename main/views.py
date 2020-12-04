from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .filters import ProductFilter
from .models import Product
from .permissions import ProductPermission
from .serializers import ProductDetailsSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    filterset_class = ProductFilter



    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params  #дает список всех параметров
        print(params)
        # queryset = queryset.filter(**params)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        else:
            permissions = [ProductPermission, ]
        return [permission() for permission in permissions]



