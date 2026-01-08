from django.urls import path
from blog import views as blog_views


urlpatterns = [
    path('', blog_views.blog, name='blog.home'),
    path('comentarios/', blog_views.comentarios, name='blog.comentarios'),
]
