from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Count
from django.utils import timezone
from .models import Post, Comment, Company, Role, ExtendedUserProfile
from .forms import AddNewPostForm


def index(request):
	args = {'user' : request.user}
	return render(request, 'supportsystem/index.html', args)

def viewposts(request):
	posts = Post.objects.filter(poststatus=True).order_by('-date_added')
	# Not Functioning Comment Counter - comments = Post.objects.filter(comment__post='').count()
	context = {'posts' : posts}
	return render(request, 'supportsystem/viewposts.html', context)

def addpost(request):
	if request.method == 'POST':
		form=AddNewPostForm(request.POST)

		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.user = request.user
			new_post.save()
			return redirect('viewposts')

	else:
		form=AddNewPostForm()
	form = {'form' : AddNewPostForm()}
	return render(request, 'supportsystem/addpost.html', form)

