from django.urls import path
from blog import views

urlpatterns=[
    path('blog/',views.blogView.as_view(),name='blog'),
    path('toiawase/',views.toiawaseView.as_view(),name='toiawase'),
    path('post/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new',views.CreatePostView.as_view(),name='post_new'),
]