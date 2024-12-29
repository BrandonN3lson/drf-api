from rest_framework import serializers
from django.db import IntegrityError
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']

        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner',
        ]

    def create(self, validate_data):
        try:
            return super().create(validate_data)
        except IntegrityError:
            serializers.ValidationError({
                'detail': 'Possible duplicate'
            })