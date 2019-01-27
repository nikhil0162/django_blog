from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
import zerosms
from background_task import background


def sending_sms_template(request):
	if 'username' in request.POST and 'password' in request.POST and 'send_to' in request.POST and 'message' in request.POST:
		username = request.POST["username"]
		password = request.POST["password"]
		sendto = request.POST["send_to"]
		msg = request.POST["message"]
		zerosms.sms(phno=8950776471, passwd='@nikhil@1', receivernum=7206759092, message="hellooooo")
		return HttpResponse("send")
	return HttpResponse(render(request, 'blog/sending_sms.html',{}))

def home(request):

	context={
		'posts':Post.objects.all()
	}
	return render(request,'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5



class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	paginate_by = 5
	context_object_name = 'posts'

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin ,CreateView):
	model = Post
	fields = ['title', 'content', 'send_via']
	template_name = 'blog/post_form.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


@background(schedule=15)
def hello():
	print('hello project')

def about(request):
<<<<<<< HEAD
	hello()
	print('running')
	return render(request,'blog/about.html', {'title':'About'})

def deom():
	pass


def demo_ui():
	pass

def game_program():
	pass


def ui_2():
	pass

def game_program_2():
	pass

def ui_3():
	pass

def game_program_3():
	pass
<<<<<<< HEAD

def ui_repo():
	pass
=======
 
 def repo_norm():
 	pass
>>>>>>> 71d3672fa5ff4d63444f04ec94f2a2543128af5f
