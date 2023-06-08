from rest_framework import serializers
# from fdo_app.models import FDO, PID_metadata, profiles, PID_records, artifact_prop

from fdo_app.models import Thing, Organisation, CreativeWork, Service, WebAPI, SoftwareApplication, Person


class thingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = '__all__'


class organizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'


class creativeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreativeWork
        fields = '__all__'
        depth = 2


class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        depth = 2

    # # validation for the type input, for either a person or an organization
    # def validate(self, data):
    #     if data['provider_type'] == 'person' and not data.get('person'):
    #         raise serializers.ValidationError("Person field is required when provider_type is 'person'.")
    #     elif data['provider_type'] == 'organisation' and not data.get('organisation'):
    #         raise serializers.ValidationError("Organization field is required when provider_type is 'organisation'.")
    #     return data


class webapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebAPI
        fields = '__all__'


class softwareapplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareApplication
        fields = '__all__'


class personSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        depth = 2






