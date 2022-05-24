from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin



class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):


    def get_author(self, obj):
        return {
            "username":obj.author.username,
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name
        }


    author = serializers.SerializerMethodField("get_author")
    class Meta:
        model = Article
        fields = '__all__'


    def validate_title(self, value):
        filter_words = ['politician', 'politics', 'Corruption']
        for word in filter_words:
            if word in value:
                raise serializers.ValidationError("don't use forbidden word : %s"%(word))
        return value



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
