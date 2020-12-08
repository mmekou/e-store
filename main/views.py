from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.viewsets import ModelViewSet

from .filters import ProductFilter
from .models import Product, Comment
from .permissions import ProductPermission, IsCommentAuthor
from .serializers import ProductDetailsSerializer, CommentSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ["title", ]

    # queryset = Product.objects.all()
    # serializer_class = ProductDetailsSerializer
    # filterset_class = ProductFilter
    # search_fields = ['title']
    # filter_backends = (filters.SearchFilter,)
    # # filterset_fields = ['category', 'title', 'price']

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


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [ProductPermission, ]
    queryset = Comment.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        else:
            permissions = [IsCommentAuthor, ]
        return [permission() for permission in permissions]

# class CustomSearchFilter(filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         if request.query_params.get('title_only'):
#             return ['title']
#         return super(CustomSearchFilter, self).get_search_fields(view, request)
