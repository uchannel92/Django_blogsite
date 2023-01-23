"""Defines URL patterns for blogs."""

from django.urls import path

from .import views

app_name = 'blogs'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),

	# Page that shows all posts
	path('blogposts/', views.blogposts, name='blogposts'),

	# Page that will add a new blog
	path('new_blog/', views.new_blog, name='new_blog'),

	# Page for editing blog posts.
	path('edit_blogpost/<int:blogpost_id>', views.edit_blogpost, name='edit_blogpost'),
]