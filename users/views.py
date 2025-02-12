from django.shortcuts import render, redirect
from django.contrib import messages
from .forms  import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def register (request):
    if request.method == 'POST':
        form =  UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Accout created for {username}!')
            return redirect('login')
        
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})

def Profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request, 'profile.html', context)
