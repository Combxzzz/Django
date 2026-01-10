from django.urls import path
from blog import views as blog_views

# blog/
urlpatterns = [
    path('', blog_views.blog, name='blog.home'),
    path('post/<int:post_id>/', blog_views.post, name='blog.post'),
    path('comentarios/', blog_views.comentarios, name='blog.comentarios'),
]
