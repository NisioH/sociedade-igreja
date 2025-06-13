from rest_framework import serializers
from .models import Sociedade, Membro

class SociedadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sociedade
        fields = '__all__'

class MembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membro
        fields = '__all__'