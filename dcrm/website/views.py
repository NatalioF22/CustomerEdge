from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
from django.db.models import Q
from .forms import AddRecordForm
# Create your views here.
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            messages.success(request, "You have been logged in")
            return render(request, 'home.html', {})
        else:
            messages.error(request,"There was an error logging in. Please try again...")
            return redirect('home')
    else: 
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and log it
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password= password)
            login(request, user)
            messages.success(request, "You have successfully created an account!!!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def custumer_record(request, pk):
    if request.user.is_authenticated:
        #look up record
        customer_record = Record.objects.get(id=pk)
        
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.info(request, "You must be logged in to view this page")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record deleted successfully!!")
        return redirect('home')
    else:
        messages.info(request, "You must be logged in!!")
        return redirect('home')
    
def add_record(request):
    form =  AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
           if form.is_valid():
            add_record = form.save()
            messages.success(request, "Record Added")
            return redirect('home')
        return render(request, 'add_record.html', {'form':form})

    else:
        messages.info(request, "You must be logged in!!")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form =  AddRecordForm(request.POST or None, instance = current_record)
        
        if form.is_valid():
            form.save()
            messages.info(request, "Record has been updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.info(request, "You must be logged in to view this page")
        return redirect('home')

        
def search_records(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            searched = request.POST['searched']
            records = Record.objects.filter(
                Q(first_name__contains=searched)| 
                Q(last_name__contains=searched) |  
                Q(email__contains=searched) | 
                Q(address__contains=searched) | 
                Q(city__contains=searched)| 
                Q(state__contains=searched) |  
                Q(phone__contains=searched) |  
                
                Q(zip_code__contains=searched) )
                
            return render(request, 'search_records.html', {'searched': searched, 'records': records})
        else:
            return render(request, 'search_records.html', {})
    else:
        
        messages.info(request, "You must be logged in to view this page")
        return redirect('home')
