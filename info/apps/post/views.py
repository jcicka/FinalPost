from django.shortcuts import render
from .models import Post
from django.views.generic.list import ListView
from django.http import HttpResponse
from .forms import PostForm
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ListarPosts(LoginRequiredMixin, ListView):
	#login_url = 'login'
	model= Post
	template_name = "postsList.html"
	context_object_name = "post"
	#def get_queryset(self):
		#noticias = Noticia.objects.all().order_by('-fecha_creacion')
		#return noticias
# Create your views here.
#def inicio(request):
#	return render(request, 'index.html')

class DetallePosts(LoginRequiredMixin, DetailView):
	model=Post
	template_name="post_detail.html"

class CrearPost(CreateView):
	model= Post
	success_url='/lista'
	form_class = PostForm

class UpdatePost(UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'post_update_form.html'
	success_url='/post'

#class DeletePost(DeleteView):
	#model = Noticia
	#success_url = reverse_lazy('lista')