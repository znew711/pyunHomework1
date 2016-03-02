from django import forms
from django.forms import ModelForm
############### django imports
from .models import blog

class BlogPost(ModelForm):
	class Meta:
		model = blog
		#fields = ['title', 'context', 'after', 'initial']
		exclude = [""]
