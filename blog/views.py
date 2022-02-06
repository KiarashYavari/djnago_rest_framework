# from django.shortcuts import render
from django.views.generic import ListView
from .models import Article
# Create your views here.


class ArticleList(ListView):
    queryset=Article.objects.filter(status=True)