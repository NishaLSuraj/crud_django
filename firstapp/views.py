from urllib import request
from django.shortcuts import redirect, render
from firstapp.form import todoform
from firstapp.models import todotable

# Create your views here.
def home(request):
    form=todoform()
    todos=todotable.objects.all()
    if request.method == 'POST':
        form=todoform(request.POST)
        if form.is_valid():
         form.save()
    return render(request,'home.html',{'form':form,'todo':todos})
def update(request,todo_id):  
    todo=todotable.objects.get(id=todo_id)
    form=todoform(instance=todo)
    if request.method == 'POST':
        form=todoform(request.POST,instance=todo)
        if form.is_valid():
         form.save()
         return redirect('/')
    return render(request,'update.html',{'form':form}) 



 





