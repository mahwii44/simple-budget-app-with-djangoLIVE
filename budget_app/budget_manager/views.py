from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Transaction

class TransactionListView(ListView):
    model = Transaction
    template_name = 'budget/transaction_list.html'

class TransactionCreateView(CreateView):
    model = Transaction
    template_name = 'budget/transaction_form.html'
    fields = ['date', 'description', 'amount']
    success_url = reverse_lazy('transactions')

class TransactionUpdateView(UpdateView):
    model = Transaction
    template_name = 'budget/transaction_form.html'
    fields = ['date', 'description', 'amount']
    success_url = reverse_lazy('transactions')

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'budget/transaction_confirm_delete.html'
    success_url = reverse_lazy('transactions')
