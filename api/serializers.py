from rest_framework import serializers
from fdo_app.models import FDO


class fdoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FDO
        fields = '__all__'