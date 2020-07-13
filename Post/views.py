from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from Post.models import Post
from .forms import ArticleModelForm
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
class ArticleCreateView(CreateView):
    template_name = 'article_create.html'
    form_class = ArticleModelForm
    queryset = Post.objects.all() # <blog>/<modelname>_list.html
    #success_url = '/'

    def form_valid(self, form):
        print (form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:list')     

        
class ArticleListView(ListView):
    template_name = 'articlelist.html'
    queryset = Post.objects.all()

class detail_view(DetailView):
    template_name = 'article_detail.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

class ArticleUpdateView(UpdateView):
    template_name = 'article_create.html'
    form_class = ArticleModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def get_success_url(self):
        return reverse('posts:list')
 



