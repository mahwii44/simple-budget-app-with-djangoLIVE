from django.urls import path
from . import views
from .views import (
    TransactionListView,
    TransactionCreateView,
    TransactionUpdateView,
    TransactionDeleteView,
)

urlpatterns = [
    path('', TransactionListView.as_view(), name='transactions'),
    path('new/', TransactionCreateView.as_view(), name='transaction_create'),
    path('<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
]
