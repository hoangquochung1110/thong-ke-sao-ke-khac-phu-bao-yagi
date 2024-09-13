from django.shortcuts import render
from .models import Transaction
from django.db.models import Q


def transaction_list(request):
    transactions = Transaction.objects.all()

    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        transactions = transactions.filter(
            Q(order__icontains=search_query) | 
            Q(comment__icontains=search_query)
        )

    # Filtering functionality
    min_amount = request.GET.get('min_amount')
    max_amount = request.GET.get('max_amount')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if min_amount:
        transactions = transactions.filter(amount__gte=min_amount)
    if max_amount:
        transactions = transactions.filter(amount__lte=max_amount)
    if start_date:
        transactions = transactions.filter(transaction_datetime__gte=start_date)
    if end_date:
        transactions = transactions.filter(transaction_datetime__lte=end_date)

    context = {
        'transactions': transactions,
    }
    return render(request, 'transaction_list.html', context)
