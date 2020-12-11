from django.urls import path

from .apiviews import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<pk>', ArticleDetailView.as_view())
]