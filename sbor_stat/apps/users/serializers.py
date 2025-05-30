from rest_framework import serializers
from .models import User

class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        request = self.context['request']
        # current_user = request.user

        teacher = User(
            username=validated_data['username'],
            role='teacher',
            pck='it'
            # pck=current_user.affiliation
        )
        teacher.set_password(validated_data['password'])
        teacher.save()
        return teacher