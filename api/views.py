# from django.shortcuts import render
from .serializers import ArticleListSerializer
from blog.models import Article
from rest_framework.generics import ListCreateAPIView

# Create your views here.
class ArticleListCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    