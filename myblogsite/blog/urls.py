from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('new/', views.CreatePostView.as_view(), name='post_new'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),

    path('<pk>/publish/', views.post_publish, name='post_publish'),
    path('<pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<pk>/remove/', views.comment_remove, name='comment_remove'),
]