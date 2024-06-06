from django.urls import path

from blog import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article_list'),
    # blog/2
    path('<int:pk>', views.article_detail, name='article_detail'),
]