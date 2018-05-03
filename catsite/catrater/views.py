from django.shortcuts import render

# Create your views here. ("logic" of the application, passed to the template)
def home_page(request):
	return render(request, 'catrater/home_page.html', {})
	

