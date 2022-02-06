from .views import ArticleList
from django.urls import path

urlpatterns = [
    path('', ArticleList.as_view(), name="article_list"),   
]