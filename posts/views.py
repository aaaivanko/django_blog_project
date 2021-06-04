from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.core.mail import send_mail
from django.contrib import messages

from .models import Post
from .forms import ContactForm


class PostListView(ListView):
    '''View for listing all posts'''
    model = Post
    ordering = ['-date_created']
    paginate_by = 2


class PostDetailView(DetailView):
    '''View for post detail '''
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    '''View for creating Posts'''
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        ''' Setting the author of the Post to the current Log In User '''
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''View for updating Posts'''
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        ''' Setting the author of the Post to the current Log In User '''
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ''' Checking whether or not the current Log In User is the author of the post '''
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''View for Post delete '''
    model = Post
    success_url = '/'

    def test_func(self):
        ''' Checking whether or not the current Log In User is the author of the post '''
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def contact(request):
    '''Logic for sending email to the site admin'''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipient = ['ivan.chvartatskyy@gmail.com']

            send_mail(subject, message, sender, recipient)
            messages.success(request, f"Your message has been successfully sent to: {recipient[0]}")

            return redirect('posts:home')
    else:
        form = ContactForm()

    context = {
        'title': 'Contact Form',
        'form': form
    }

    return render(request, 'posts/contact.html', context)



