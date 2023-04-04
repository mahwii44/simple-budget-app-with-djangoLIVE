from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'amount')

admin.site.register(Transaction, TransactionAdmin)
