from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from .forms import RegForm

def create_Students(request):
    submitted = False
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('form_register') + '?submitted=true')

    else:
        form = RegForm
        if 'submitted' in request.GET:
            submitted = True 

    return render(request, 'form_register.html', {'form':form, 'submitted':submitted})
