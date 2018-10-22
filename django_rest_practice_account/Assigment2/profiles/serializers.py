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
        
    #def validate_first_name(self, value):
        """
        Check that the blog post is about Django.
        """
        #print("!!")
        #print(value)
        #if 'django' not in value.lower():
            #raise serializers.ValidationError("Blog post is not about Django")
        #if not value.strip() :
            #print("!!!!!!")
            #raise serializers.ValidationError("first_name is empty")
        #return value