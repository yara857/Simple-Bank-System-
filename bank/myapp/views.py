from django.shortcuts import render , redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    acc = account.objects.all()
    context = {
        'acc' : acc
    }
    return render(request , 'inner-page.html' , context)

def transfer(request):
    form = TransferForm(request.POST or None)
    if form.is_valid():
        sender = form.cleaned_data['sender']
        receiver = form.cleaned_data['receiver']
        amount = form.cleaned_data['amount']
        if sender.current_balance >= amount:
            sender.current_balance -= amount
            receiver.current_balance += amount
            sender.save()
            receiver.save()
            transfer = form.save()
            return redirect('thanks')
        else:
            return render(request, 'inner-page.html', {'form': form, 'error': 'Insufficient funds.'})
    return render(request, 'transfer.html', {'form': form})

def transactions(request):
    trans = Transaction.objects.all()
    context = {
        'trans' : trans
    }
    return render(request , "transactions.html" , context)

def thanks(request):
    return render(request , 'thanks.html')

def index(request):
    return render(request , "index.html")