from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction
from django.urls import reverse_lazy
from django.contrib import messages

def transaction_list(request):
    transactions = Transaction.objects.all()
    context = {
        'transactions': transactions,
    }
    return render(request, 'index.html', context)

def transaction_create(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        Transaction.objects.create(date=date, description=description, amount=amount)
        messages.success(request, 'Transaction created successfully.')
        return redirect('transactions')

    return render(request, 'newbudget.html')

def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    if request.method == 'POST':
        transaction.date = request.POST.get('date')
        transaction.description = request.POST.get('description')
        transaction.amount = request.POST.get('amount')
        transaction.save()
        messages.success(request, 'Transaction updated successfully.')
        return redirect('transactions')

    context = {
        'transaction': transaction,
    }
    return render(request, 'edit.html', context)

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    if request.method == 'POST':
        transaction.delete()
        messages.success(request, 'Transaction deleted successfully.')
        return redirect('transactions')

    context = {
        'transaction': transaction,
    }
    return render(request, 'delete.html', context)
