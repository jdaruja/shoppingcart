import datetime
from django.db import models
from django.utils import timezone
from accounts.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class ShoppingList(models.Model):
    """This is the model for a single shopping list"""
    name = models.CharField(_('list_name'), max_length=20, null=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='shopping_lists')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def was_published_recently(self):
            return self.date_updated >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        ordering = ('-date_created',)

class ShoppingItem(models.Model):
    """This is the model for a single shopping item in a list"""
    name = models.CharField(_('item_name'), max_length=20, null=False)
    price = models.DecimalField(_('purchase_price(KES'),max_digits=7, decimal_places=2, default=0.00)
    quantity = models.DecimalField(_('item_quantity'),max_digits=7, decimal_places=2, default=0.00)
    list = models.ForeignKey(
        ShoppingList, on_delete=models.CASCADE, related_name='shopping_items')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)


# class Choice(models.Model):
#     item = models.ForeignKey(ShoppingItem, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.choice_text
