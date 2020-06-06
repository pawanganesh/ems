from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import  User, auth
from django.contrib.auth import  login
from .forms import CreateUserForm
from django.contrib import messages



# Create your views here.
def add_account(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            form = CreateUserForm()
        else:
            user = User.objects.get(pk = id)
            form = CreateUserForm(instance=user)
        context = {'form':form}
        return render(request, 'account/add_account.html',context)
    else:
        if id == 0:
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user +', Your Account Created Successfully')
                return redirect('login_account')
        else:
            user = User.objects.get(pk = id)
            form = CreateUserForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user +', Your Account Has Been Updated')
            return redirect('manage_user')
        context = {'form':form}
        return render(request, 'account/add_account.html', context)

def login_account(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html',{'form':form})

def logout_account(request):
    auth.logout(request)
    return redirect('/')

def user_list(request):
    userlist = User.objects.all()
    context = {'users':userlist}
    return render(request, 'account/manage_user.html',context)

def delete_user(request, id):
    user = User.objects.get(pk = id)
    user.delete()
    return redirect('manage_user')
