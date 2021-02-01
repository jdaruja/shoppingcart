from django.urls import path

# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
# ]

from .views import (DashBoardView, ShoppingListUpdate, ShoppingListDelete,
                    DetailsView, ShoppingItemUpdate, ShoppingItemDelete)


app_name = "shopping_proj"
urlpatterns = [
    path('dashboard/list_update/<int:pk>/', ShoppingListUpdate.as_view(), name='update_list'),
    path('dashboard/list_delete/<int:pk>/', ShoppingListDelete.as_view(), name='delete_list'),
    path('dashboard', DashBoardView.as_view(), name='dashboard'),
    path('details/<int:pk>/', DetailsView.as_view(), name='details'),
    path('details/<int:pk>/update/', ShoppingItemUpdate.as_view(), name='update_item'),
    path('details/<int:pk>/delete/', ShoppingItemDelete.as_view(), name='delete_item'),
]