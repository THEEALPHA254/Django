from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def create_Fee_balance(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_template')
    else:
        form = StudentForm()
    return render(request, 'form_template.html', {'form':form})

def update_Fee_balance(request, pk):
    Fee_balance = get_object_or_404(Fee_balance, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=Fee_balance)
        if form.is_valid():
            form.save()
            return redirect('form_template')
    else:
        form = StudentForm(instance=Fee_balance)
    return render(request, 'form_template.html', {'form': form})

    def delete_Fee_balance(request, pk):
        Fee_balance = get_object_or_404(Fee_balance, pk=pk)
        if request.method =='POST':
            Fee_balance.delete()
            return redirect('form_template')
        return render(request, 'form_confirm_delete.html', {'Fee_balance': Fee_balance})
