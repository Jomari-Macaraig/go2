from rest_framework import serializers

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
            "url"
        )
        read_only_fields = (
            "sku",
        )