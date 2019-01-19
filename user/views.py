from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import product_form,signup_form
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def user_login(request):
	if(request.method == "POST"):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,('You have been logged in..'))
			return redirect("user_home")

		else:
			messages.success(request,('Error loggin in.Please try again..'))
			return redirect('user_login')
	else:
			return render(request,'user/user_login.html')

def user_logout(request):
	logout(request)
	messages.success(request,('You have been logged out..'))
	return redirect('home')

def user_register(request):
	if request.method == 'POST':
		form = signup_form(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request,('You have successfully registered...'))
			return redirect("user_home")
	else:
		form = signup_form()

	return render(request,'user/user_register.html',{'form':form})


def user_home(request):
	if request.method == 'POST':
		form = product_form(request.POST)
		if form.is_valid():
			product = form.save(commit=False)
			product.save()
			messages.success(request,('Your post is successfully added..'))
			return redirect("user_home")
		
				
	else:
		form = product_form()	
		return render(request,'user/user-home.html',{'form':form})