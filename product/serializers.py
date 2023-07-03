from product.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
          "id",
          "name", 
          "quantity", 
          "price", 
          "category", 
          "isAvailable",
          "user"
        ]
        extra_kwargs = {
          "user": {"read_only": True},
          "isAvailable":{"default": True}
        }
    def validate(self, attrs):
      quantity = attrs.get("quantity")
      attrs["isAvailable"] = quantity != 0
      return attrs