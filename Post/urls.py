from django.urls import path
from django.urls import include
from .views import (ArticleListView,detail_view,ArticleCreateView,ArticleUpdateView,ArticleDeleteView)
app_name='posts'
urlpatterns = [
    path('all/',ArticleListView.as_view(), name='list'),
    path('post/<int:id>/', detail_view.as_view(), name='post-details'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('post/<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('post/<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]