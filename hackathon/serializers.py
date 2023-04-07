from rest_framework import serializers
from .models import User,Hackathon, Submission

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["id","username","email","password"]
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(email=validated_data['email'],
                                        username=validated_data['username']
                                            )
        if password:
            user.set_password(password)
            user.save()
        return user

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ["id","title","description","hackathonImage","participants","typeofSubmission","start","end","reward"]

class getHackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ["id","title","description","hackathonImage"]


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ["name","summary","participant","hackathon","urlSubmission","fileSubmission","imageSubmission" ]

        

