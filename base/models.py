from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Grocery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item_name = models.CharField(max_length=200)
    item_quantity = models.CharField(max_length=100)

    PENDING = 'PENDING'
    BOUGHT = 'BOUGHT'
    NOT_AVAILABLE = 'NOT AVAILABLE'

    status = [
        (PENDING, 'PENDING'),
        (BOUGHT, 'BOUGHT'),
        (NOT_AVAILABLE, 'NOT AVAILABLE'),
    ]

    choose = models.CharField(
        max_length=20,
        choices=status,
        default=BOUGHT,
    )

    date = models.DateField(auto_now=False, auto_now_add=False, blank=True)

    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name

    class Meta:
        ordering = ['date']    

