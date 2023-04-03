from django.urls import path
from .views import TransactionListView, TransactionCreateView, TransactionUpdateView, TransactionDeleteView

urlpatterns = [
    path('', TransactionListView.as_view(), name='transactions'),
    path('create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
]