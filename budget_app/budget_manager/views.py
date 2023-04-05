from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm


def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'index.html', {'transactions': transactions})

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'newbudget.html', {'form': form})



class TransactionUpdateView(UpdateView):
    model = Transaction
    template_name = 'index.html'
    fields = ['date', 'description', 'amount']
    success_url = reverse_lazy('transaction')

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'delete.html'
    success_url = reverse_lazy('transaction')
