from django.urls import path
from .views import ArticleListCreateView

app_name="api"
urlpatterns = [
    path('', ArticleListCreateView.as_view(), name="api_list_create")
]