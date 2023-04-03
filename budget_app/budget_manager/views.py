from django.shortcuts import render
from .models import Transaction


# Create your views here.
def index(request):
    transactions = Transaction.objects.all()
    return render(request, 'index.html', {'transactions': transactions})



