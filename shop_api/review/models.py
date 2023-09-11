from django.db import models
from product.models import Product
from django.contrib.auth import get_user_model
from typing import List, Tuple

User = get_user_model()

class Comment(models.Model):
    body = models.TextField(verbose_name='Содержимое')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} {self.body}'
    
class Rating(models.Model):
    rating = models.PositiveSmallIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return f'{self.author} {self.rating}'


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    is_liked = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.author} {self.product}'
    


class Dislike(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dislikes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='dislikes')


    def __str__(self):
        return f'{self.author} {self.product}'
    
class Favorite(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)
        constraints = [models.UniqueConstraint(fields=['author', 'product'], name='unique_author_product'),]

        indexes = [models.Index(fields=['author', 'product'], name='idx_author_product'),]
        # unique_together: List[Tuple(int, str)]

        # indexes: List[models.Index] = [models.Index(fields=('author', 'product'))]


