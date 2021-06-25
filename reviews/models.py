from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):
    """
    A review model that allows users to perform
    CRUD operations on product reviews
    """

    RATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.IntegerField(choices=RATING)
    would_recommend = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
