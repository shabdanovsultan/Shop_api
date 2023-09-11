from django.urls import path, include
from .views import CommentView, RatingView, FavoriteCreateView, FavoriteListView, FavoriteDeleteView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('comments', CommentView)
router.register('ratings', RatingView)


urlpatterns = [
    path('', include(router.urls)),
    path('favorites/', FavoriteListView.as_view(), name='list'),
    path('favorite/', FavoriteCreateView.as_view(), name='create'),
    path('favorites/<int:pk>/', FavoriteDeleteView.as_view(), name='delete')
]