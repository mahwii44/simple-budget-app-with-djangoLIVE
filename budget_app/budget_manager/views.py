from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm


class TransactionListView(ListView):
     model = Transaction
     template_name = 'index.html'
     context_object_name = 'transaction'

class TransactionCreateView(CreateView):
    model = Transaction
    template_name = 'newbudget.html'
    fields = ['date', 'description', 'amount']
    success_url = reverse_lazy('transaction')

class TransactionUpdateView(UpdateView):
    model = Transaction
    template_name = 'index.html'
    fields = ['date', 'description', 'amount']
    success_url = reverse_lazy('transaction')

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'delete.html'
    success_url = reverse_lazy('transaction')
