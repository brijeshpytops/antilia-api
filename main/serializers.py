from rest_framework import serializers
from .models import member, news

class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = member
        fields = "__all__"

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = "__all__"

