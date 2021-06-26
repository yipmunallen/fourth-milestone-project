from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='posts'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('add_post', views.add_post, name='add_post'),
    path('edit_post/<slug:slug>/', views.edit_post, name='edit_post'),
]
