from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment
from posts.models import Post


class CommentListView(ListView):
    model = Comment
    template_name = 'comments/comment_list.html'
    context_object_name = 'comments'

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return context


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comments/comment_detail.html'


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']
    template_name = 'comments/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('comment_list', kwargs={'post_id': self.kwargs['post_id']})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['text']
    template_name = 'comments/comment_form.html'

    def get_success_url(self):
        return reverse_lazy('comment_detail', kwargs={'pk': self.object.pk})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comments/comment_list.html'

    def get_success_url(self):
        return reverse_lazy('comment_list', kwargs={'post_id': self.object.post.id})