from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogForm

# Create your views here.

def index(request):
	""" The home page for blogs. """
	return render(request, 'blogs/index.html')


def check_blog_owner(blogpost, request):
	""" check if the blogpost belongs to the owner """
	if blogpost.owner != request.user:
		raise Http404

def blogposts(request):
	""" Show all posts. """
	blogpost = BlogPost.objects.order_by('-date_added')
	context = {'blogpost': blogpost}
	return render(request, 'blogs/blogposts.html', context)

@login_required
def new_blog(request):
	""" Add a new blog """
	if request.method != 'POST':
		# No data submitted, create a blank form
		form = BlogForm()
	else:
		# POST data submitted; process data.
		form = BlogForm(data=request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.owner = request.user
			new_post.save()
			form.save()
			return redirect('blogs:blogposts')

	# Display blank or invalid form.
	context = {'form': form}
	return render(request, 'blogs/new_blog.html', context)

@login_required
def edit_blogpost(request, blogpost_id):
	"""Edit an existing blogpost"""
	blogpost = BlogPost.objects.get(id=blogpost_id) # blog id number
	blog = blogpost # blog data which includes the title. text etc.

	check_blog_owner(blogpost, request)

	if request.method != 'POST':
		# Intial request; pre-fill form with current blog post.
		form = BlogForm(instance=blogpost)
	else:
		# POST data submitted, process data.
		form = BlogForm(instance=blogpost, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('blogs:blogposts')

	context = {'blogpost': blogpost, 'blog': blog, 'form': form}
	return render(request, 'blogs/edit_blogpost.html', context)

