"""
shareblood.account.serializers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from rest_framework import serializers
from account.models import CustomAccount


class CustomAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomAccount
        fields = ('name', 'email', 'gender', 'role', 'birth_date', 'site',
                  'image', 'about', 'blood_type', 'location')
        write_only_fields = ('password',)

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'), instance.password)
        return instance

    def create(self, validated_data):
        return CustomAccount.objects.create(**validated_data)
