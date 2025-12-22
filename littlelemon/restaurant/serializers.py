from rest_framework import serializers
from .models import MenuTable, BookingTable

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTable
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = '__all__'