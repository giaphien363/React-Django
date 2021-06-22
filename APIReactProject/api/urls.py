from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet, UserViewSet

# from .views import ArticleList, ArticleDetail
# from .views import index, article_detail

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('user', UserViewSet)


urlpatterns = [
    # path('', ArticleList.as_view()),
    # path('<int:id>/', ArticleDetail.as_view()),
    # path('', index),
    # path('<int:pk>/', article_detail),
    path('api/', include(router.urls))
]
