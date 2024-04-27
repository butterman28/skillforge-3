from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog import views
from .views import *

#router.register(r'comments', CommentViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path("post/", views.postview.as_view(),name="posts"),
    path("post/<int:post_id>/", views.postupdatedelete.as_view(),name="post_update_delete"),
    path("comment/<int:post_id>/", views.CommentView.as_view(),name="comment"),
    path("commentadjust/<int:comment_id>/", views.commentupdatedelete.as_view(),name="comment_update_delete"),
    path("search/", views.searchview.as_view(),name="search"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('searchpost/', BlogPostSearch.as_view(), name='blog-post-search'),
]
