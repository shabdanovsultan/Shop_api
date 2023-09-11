from .models import Like, Dislike, Comment, Rating
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommentSerializer, RatingSerializer, FavoiteListSerializer, FavoriteCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAuthorOrReadOnly
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated]

        elif self.action in ('update', 'partial_update', 'destroy'):
            permissions = [IsAuthorOrReadOnly]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]


class CommentView(PermissionMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RatingView(PermissionMixin, ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class FavoriteListView(ListAPIView):
    serializer_class = FavoiteListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.favoites.all()
    
class FavoriteCreateView(CreateAPIView):
    serializer_class = FavoriteCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FavoriteDeleteView(DestroyAPIView):
    lookup_url_kwarg = 'pk'
    permission_classes = (IsAuthenticated)
    
    def get_queryset(self):
        return self.request.user.favorites.all()