from django.urls import path
from .views import *
urlpatterns = [
    path("register/",SignUpView.as_view(),name="signup"),
    path("login/",SignInView.as_view(),name="signin"),
    path("index/",IndexView.as_view(),name="index"),
    path("posts/<int:id>/comment/add",add_comments,name="add-comments"),
    path("post/<int:id>/like/add",like_post_view,name="add-like"),
    path("logout",signout_view,name="logout")
]
