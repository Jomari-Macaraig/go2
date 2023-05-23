from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductSerializer
from ..models import Product


class ProductListAPIView(ListAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        status = self.request.query_params.get("status", "")

        if status:
            status = status.lower()

        if status == "true":
            queryset = queryset.filter(quantity__gt=0)
        elif status == "false":
            queryset = queryset.filter(quantity=0)

        return queryset


class ProductRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    lookup_field = "sku"
