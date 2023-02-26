from rest_framework import serializers
from fdo_app.models import FDO, PID_metadata, profiles, PID_records


class fdoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FDO
        fields = '__all__'


class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profiles
        fields = '__all__'


class recordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PID_records
        fields = '__all__'


class metadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PID_metadata
        fields = '__all__'