from rest_framework import serializers
from users.models import TodoUser

class TodoUserCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = TodoUser
        fields = ('username', 'email', 'password')


    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(validated_data['password'])
        user.save()
        return user


class TodoUserManyDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoUser
        fields = ('username',)