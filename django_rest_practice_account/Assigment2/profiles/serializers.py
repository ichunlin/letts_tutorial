from rest_framework import serializers
from profiles.models import loginModel, ProfileModel, LANGUAGE_CHOICES, STYLE_CHOICES

class LoginModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = loginModel
        fields = ('id', 'email', 'password')

class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'first_name', 'last_name','phoneNo','email')