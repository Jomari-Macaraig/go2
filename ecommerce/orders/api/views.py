from typing import Tuple

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommerce.products.api.serializers import SimpleProductSerializer
from .serializers import OrderSerializer


class CreateOrder(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        response, order = self._validate_order(request=request)

        if response:
            return response

        response = self._validate_products(request=request)

        if response:
            return response

        order.save()

        return Response(order.data)

    def _validate_order(self, request) -> Tuple:
        order_number = request.data["order_number"]
        data = {
            "order_number": order_number,
            "meta": request.data
        }
        serializer = OrderSerializer(data=data)

        if serializer.is_valid():
            return None, serializer

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST), serializer

    def _validate_products(self, request):
        for item in request.data.get("items", []):
            product = SimpleProductSerializer(data=item)
            if not product.is_valid():
                return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)
        return None
