from django import forms

from .models import Post

class AddPostForm(forms.Form):
	posttitle = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Please enter a title'}))
	postbody = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Please describe the issue you are experiencing in detail.'}))
	#postmedia = forms.ImageField(upload_to = 'uploadedimages/', default = 'uploadedimages/None/no.img.jpg')

class AddNewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['posttitle', 'postbody']
		widgets = {
			'posttitle' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Please enter a title'}),
			'postbody' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Please describe the issue you are experiencing in detail.'})
		}