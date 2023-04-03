from django.shortcuts import render
from .models import Transaction


# Create your views here.
def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'index.html', {'transactions': transactions})



