from rest_framework import serializers

from .models import Shawarma

class ShawarmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shawarma
        fields = '__all__'