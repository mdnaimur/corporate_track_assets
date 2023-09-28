from base import models
from rest_framework.serializers import ModelSerializer
from base.models import Product_Assets


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product_Assets
        fields = '__all__'
        # exclude = ['user_host']
