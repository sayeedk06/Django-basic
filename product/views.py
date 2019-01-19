from django.shortcuts import render
from .models import UserProduct
from django.db.models import Min

# Create your views here.
def home(request):
	allpost = UserProduct.objects.values('seller_city').annotate(city = Min('seller_city'))
	return render(request,'home.html',{'posts':allpost})

def allpost(request,pk = None):
	if(pk):
		allpost = UserProduct.objects.filter(seller_city = pk)
		return render(request,'product/allpost.html',{'posts':allpost})
	else:
		allpost = UserProduct.objects.all()
		return render(request,'product/allpost.html',{'posts':allpost})




UserProduct.objects.values('seller_city').annotate(city=Min('seller_city'))
