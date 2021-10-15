from rest_framework import fields, serializers
from .models import student

class studentserializer(serializers.ModelSerializer):
  class Meta:
      model = student
      fields = ['id','name', 'address','number']