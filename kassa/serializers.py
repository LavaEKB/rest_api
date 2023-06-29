from rest_framework import serializers
from .models import Sale
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class SaleSerializer(serializers.ModelSerializer):

    #author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Sale
        fields ='__all__'
        
        #lookup_field = 'ntab'
        #extra_kwargs = {
        #    'url': {'lookup_field': 'ntab'}
        #}
