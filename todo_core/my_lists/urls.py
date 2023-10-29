from django.urls import path, include
from .views import home, items_list

urlpatterns = [
    path('', home),
    path('<int:pk>/', items_list, name="items_list")
]
