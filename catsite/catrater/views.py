from django.shortcuts import render
from django.utils import timezone
from .models import Cat
# Connects models and templates
# Create your views here. ("logic" of the application, passed to the template)
def home_page(request):
	cats = Cat.objects.filter(upload_date__lte=timezone.now()).order_by('upload_date')
	return render(request, 'catrater/home_page.html', {'cats': cats})
	

