from django.urls import path
from blog import views

urlpatterns = [
    path("post-new/", views.PostNewestListAPIView.as_view()),
    path("post-create/", views.PostCreateAPIView.as_view()),
    path("posts/", views.PostListAPIView.as_view()),
    path("posts-most-viewed/", views.MostViewedPostsAPIView.as_view()),
    path("posts-week-viewed/", views.MostViewedOnOneWeekPostsAPIView.as_view()),
    path("posts-month-viewed/", views.MostViewedOnOneMonthPostsAPIView.as_view()),
    path("posts-detail/<int:pk>/", views.PostDetailAPIView.as_view()),
    
    
    path("comments/<int:pk>/", views.PostCommentListView.as_view()),
    path("comments/create/<int:pk>/", views.PostCommentCreateView.as_view()),
]
