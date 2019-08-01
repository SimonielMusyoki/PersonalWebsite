from django.shortcuts import render, get_object_or_404, redirect
from .models import Messages,Post, Projects
from .forms import ContactForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title','content','url']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title','content','url']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model =  Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def home(request):
    context = {
    'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html', {'title': 'About'})

def contact(request):
    form = ContactForm()
    if form.is_valid():
        message = "message send successfully. Please wait for response on your email"
        form.save()
        return redirect('blog-home')

    return render(request,'blog/contact.html', {'form':form,'title': 'Contact'})

class Contact(CreateView):
    model = Messages
    template_name = 'blog/contact.html'
    fields = ['name','email','message']

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Projects
    template_name = 'blog/project_create.html'
    fields = ['title', 'idea','technologies','git_link', 'project_link','status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ProjectDetailView(DetailView):
    model = Projects
    template_name = 'blog/project-detail.html'
    context_object_name = 'posts'

class ProjectListView(ListView):
    model = Projects
    template_name = 'blog/projects.html'
    context_object_name = 'posts'
    ordering = ['-date_started']
    paginate_by = 5

class MessagesListView(ListView):
    model = Messages
    template_name = 'blog/message.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Projects
    template_name = 'blog/project_create.html'
    fields = ['title', 'idea','git_link', 'project_link','status']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ProjectDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model =  Projects
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
