from django.urls import path
from . import views, api
app_name = "posts"
urlpatterns = [
    path('', views.index, name="index"),
    path('api/posts/', api.PostViewset.as_view({"get":"list", "post": "create"})),
    path('api/posts/<int:pk>', api.PostViewset.as_view({"get":"retrieve", "post":"update"})),
    path('<int:id>/', views.postDetails, name="details"),
    # path('api/posts/create', api.createPost, name="create-post"),
    # path('api/posts/', api.listPosts, name="posts-list"),
    # path('api/posts/<int:id>', api.postDetail, name="post-detail"),
    # path('api/posts/<int:id>/update/', api.updatePost, name="update-post"),
    # path('api/posts/<int:id>/delete/', api.deletePost, name="delete-post"),
]