from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id', 'owner', 'post',
            'created_at',
        ]

    def create(self, validate_data):
        try:
            return super().create(validate_data)
        except IntegrityError:
            serializers.ValidationError({
                'detail': 'Possible duplicate'
            })
