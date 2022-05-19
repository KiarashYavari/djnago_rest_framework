from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model

class ArticleSerializer(serializers.ModelSerializer):
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
