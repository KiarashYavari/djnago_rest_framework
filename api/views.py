from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticleSerializer, UserSerializer
from blog.models import Article
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthorOrReadonly, SuperUserOrReadonly, IsStaffOrReadonly
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
# Create your views here.
# add a custom permission for all views list of articles for staff to manipulate for users to read
# list of users for superuser to manipulate, for staff to read, users no access

class ArticleViewSet(ModelViewSet):
    queryset =  Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ["status", "author__username", "author"]


    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadonly]
        else:
            permission_classes = [IsStaffOrReadonly, IsAuthorOrReadonly]
        
        return[permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (SuperUserOrReadonly,)


class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/api/'
    client_class = OAuth2Client


class EmailConfirmView(APIView):
    
    def get(self, request, key):
        return Response({'detail':"youre registerd successfully."}, status=201)