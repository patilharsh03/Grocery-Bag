from django.urls import path
from .views import GroceryList, GroceryDetail, GroceryCreate, GroceryUpdate, GroceryDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', GroceryList.as_view(), name='groceries'),
    path('grocery/<int:pk>/', GroceryDetail.as_view(), name='grocery'),
    path('create-grocery/', GroceryCreate.as_view(), name='create-grocery'),
    path('update-grocery/<int:pk>/', GroceryUpdate.as_view(), name='update-grocery'),
    path('delete-grocery/<int:pk>/', GroceryDelete.as_view(), name='delete-grocery'),

]
