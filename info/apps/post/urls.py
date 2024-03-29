from django.urls import path
from . import views


urlpatterns = [
	path('', views.ListarPosts.as_view(), name= 'lista'),
	path('<slug:pk>/detalle', views.DetallePosts.as_view(), name= 'detalle'),
	path('<slug:pk>/update', views.UpdatePost.as_view(), name='update'),
	path('<slug:pk>/delete', views.DeletePost.as_view(), name='delete'),
	path('crear/', views.CrearPost.as_view(), name='crear'),
]