from .models import Notes
from rest_framework import serializers
from django.contrib.auth.models import User



class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields =['id','username','email','password']
        extra_kwargs = {"password": {"write_only": True}}
         
         
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


#creaate a file 


from rest_framework import serializers
from .models import Notes

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'first_name', 'last_name', 'department', 'grade', 'cgpa', 'sslc_percentage', 'plus_two_percentage', 'phone_number', 'address', 'image']
        extra_kwargs = {"user": {"read_only": True}}
  # Set user__username field as read-only
    
