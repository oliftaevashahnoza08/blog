from django.urls import path
from django.views.generic import RedirectView
from posts.views import PostListView,PostDetailView,UsersPostListview

urlpatterns = [
    path('posts/', PostListView.as_view(),name="post-list"),
    path('posts/<pk>/', PostDetailView.as_view(),name="post-detail"),
    path(
        "posts/author/<username>/", UsersPostListview.as_view(),name="user"
    )
    path("",RedirectView.as_view(url=reverse_lazy("post_list"),permenent=))
]

