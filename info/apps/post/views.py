from django.shortcuts import render
from .models import Post
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

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

class DetallePosts(DetailView):
	model=Post
	template_name="post_detail.html"