from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Topic, Post
from .forms import PostForm


class TopicListView(ListView):
    model = Topic
    template_name = 'forum/topic_list.html'
    context_object_name = 'topics'


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'forum/topic_detail.html'
    context_object_name = 'topic'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        context['posts'] = self.object.posts.all()[:self.paginate_by]
        return context