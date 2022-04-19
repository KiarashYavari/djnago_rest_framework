# from django.shortcuts import render
from .serializers import ArticleSerializer, UserSerializer
from blog.models import Article
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAuthorOrReadonly, SuperUserOrReadonly
# Create your views here.
# add a custom permission for all views list of articles for staff to manipulate for users to read
# list of users for superuser to manipulate, for staff to read, users no access

class ArticleListCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthorOrReadonly,)


class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (SuperUserOrReadonly,)


class UserRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (SuperUserOrReadonly,)