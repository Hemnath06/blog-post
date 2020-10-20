from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry, Comment
from .forms import CommentForm
from django.urls import reverse_lazy

# Create your views here.

class HomeView(LoginRequiredMixin, ListView):
	model = Entry
	template_name = 'index.html'
	context_object_name = "blog_entries"
	ordering = ['-entry_date']
	paginate_by = 3

class EntryView(LoginRequiredMixin, DetailView):
	model = Entry
	template_name = 'entry_detail.html'

class CreateEntryView(LoginRequiredMixin, CreateView):
	model = Entry
	template_name = 'create_entry.html'
	fields = ['entry_title', 'entry_text']

	def form_valid(self,form):
		form.instance.entry_author = self.request.user
		return super().form_valid(form)

class AddCommentView(CreateView):
	model = Comment 
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = '__all__'
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

	success_url = reverse_lazy('blog-home')

