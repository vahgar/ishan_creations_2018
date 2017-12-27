from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return render(request,'index.html')


def icbc(request):
	return render(request,'icbc.html')

def categories(request):
	return render(request,'categories.html')
