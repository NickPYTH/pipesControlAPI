from validate_email import validate_email
from rest_framework import serializers
from .models import userProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password


class userProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    def validate(self, attrs):
        username = str(self.context.get('request').data.get('username'))
        password = str(self.context.get('request').data.get('password'))
        email = str(self.context.get('request').data.get('email'))
        if len(username.strip()) < 3:
            raise serializers.ValidationError("Username too short")
        else:
            if len(User.objects.filter(username=username)) != 0:
                raise serializers.ValidationError("Username exists")
        if len(password.strip()) < 7:
            raise serializers.ValidationError("Password too short")
        if not validate_email(email):
            raise serializers.ValidationError("Bad email")
        return {'attrs': {'username': username, 'password': password, 'email': email}}

    def create(self, validated_data):
        print('here')
        attrs = validated_data.get('attrs')
        user = User.objects.create(
            username=attrs.get('username'),
            email=attrs.get('password'),
            password=make_password(attrs.get('password')))
        user.save()
        user_profile = userProfile.objects.create(user=user)
        user_profile.save()
        return user_profile

    class Meta:
        model = userProfile
        fields = '__all__'
