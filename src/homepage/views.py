from django.shortcuts import render
from homepage.models import blog

from .forms import BlogPost

# Create your views here.

from django.contrib.auth import authenticate,login,logout
from helloworld import settings
from django.contrib.auth.models import User

def home(request):
	all_objects = blog.objects.all()
	first_object = all_objects[0]
	title_first_object= first_object.title
	form = BlogPost(request.POST or None) ##this is our form
	###save code undernearth
	if form.is_valid():
		var = form.save(commit = 'false')
		var.save()
	##above is save code
	template="home.html"
	context={
		"form" : form,
		"variable1": all_objects,
		"variable2": first_object,
		"WOWTHISISAVARIABLE": title_first_object,
	}
	return render(request,template,context)
