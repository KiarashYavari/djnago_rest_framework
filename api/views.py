# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticleSerializer, UserSerializer
from blog.models import Article
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadonly, SuperUserOrReadonly
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
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


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)

#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)


class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/api/'
    client_class = OAuth2Client


class EmailConfirmView(APIView):
    
    def get(self, request, key):
        return Response({'detail':"youre registerd successfully."}, status=201)