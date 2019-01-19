from django.forms import ModelForm
from product.models import UserProduct
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms

class product_form(ModelForm):
	class Meta:
		model = UserProduct
		fields = '__all__'
	def __init__(self, *args, **kwargs):

		super(product_form,self).__init__(*args, **kwargs)

		self.fields['product_title'].widget.attrs.update({'class': 'form-control'})
		self.fields['product_description'].widget.attrs.update({'class': 'form-control'})
		self.fields['product_price'].widget.attrs.update({'class': 'form-control'})
		self.fields['price_negotiable'].widget.attrs.update({'class': 'form-control'})
		self.fields['product_usage_age'].widget.attrs.update({'class': 'form-control'})
		self.fields['product_warranty'].widget.attrs.update({'class': 'form-control'})

		self.fields['seller_name'].widget.attrs.update({'class': 'form-control'})
		self.fields['seller_location'].widget.attrs.update({'class': 'form-control'})
		self.fields['seller_email'].widget.attrs.update({'class': 'form-control'})
		self.fields['seller_phone'].widget.attrs.update({'class': 'form-control'})
		self.fields['seller_city'].widget.attrs.update({'class': 'form-control'})
		
	

class signup_form(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name','last_name','email','password1','password2',)
			
	def __init__(self, *args, **kwargs):

		super(signup_form,self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs.update({'class': 'form-control'})
		self.fields['password1'].widget.attrs.update({'class': 'form-control'})
		self.fields['password2'].widget.attrs.update({'class': 'form-control'})