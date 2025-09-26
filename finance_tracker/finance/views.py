from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm

# Home page - shows all transactions
def home(request):
    transactions = Transaction.objects.all()
    return render(request, 'finance/home.html', {'transactions': transactions})

# Summary page - shows totals
def summary(request):
    transactions = Transaction.objects.all()
    total_income = sum(t.amount for t in transactions if t.type == 'Income')
    total_expense = sum(t.amount for t in transactions if t.type == 'Expense')
    balance = total_income - total_expense
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }
    return render(request, 'finance/summary.html', context)

# Add new transaction
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TransactionForm()
    return render(request, 'finance/add_transaction.html', {'form': form})
