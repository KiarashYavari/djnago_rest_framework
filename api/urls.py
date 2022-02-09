from django.urls import path
from .views import (ArticleListCreateView, ArticleRetrieveUpdateDeleteView,
 UserListCreateView, UserRetrieveUpdateDeleteView)

app_name="api"
urlpatterns = [
    path('', ArticleListCreateView.as_view(), name="api_list_create"),
    path('<int:pk>', ArticleRetrieveUpdateDeleteView.as_view(), name="api_detail"),
    path('users/', UserListCreateView.as_view(), name="api_user_list_create"),
    path('users/<int:pk>', UserRetrieveUpdateDeleteView.as_view(), name="api_user_detail"),
]