from django.urls import path
from .views import ArticleListCreateView, ArticleRetrieveUpdateDeleteView

app_name="api"
urlpatterns = [
    path('', ArticleListCreateView.as_view(), name="api_list_create"),
    path('<int:pk>', ArticleRetrieveUpdateDeleteView.as_view(), name="api_detail"),
]