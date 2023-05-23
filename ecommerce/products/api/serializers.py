from rest_framework import serializers
from rest_framework.exceptions import NotFound, ValidationError

from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(read_only=True)
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Product
        fields = (
            "sku",
            "name",
            "price",
            "description",
            "quantity",
            "status",
            "url",
        )
        read_only_fields = (
            "sku",
        )


class SimpleProductSerializer(serializers.Serializer):
    sku = serializers.CharField(max_length=128)
    quantity = serializers.IntegerField(min_value=0)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        sku = data.get("sku")
        try:
            product = Product.objects.get(pk=sku)
        except Product.DoesNotExist:
            raise NotFound(detail=f"Product {sku} does not exists")

        if not product.status:
            raise ValidationError(detail=f"Product {product.sku} is out of stock")

        if not product.is_stock_sufficient(orders=data.get("quantity", 0)):
            raise ValidationError(detail=f"Product {product.sku} has insufficient stocks")
        return data
