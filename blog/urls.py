from django.urls import path
from . import views
urlpatterns = [
    path("home/",views.home, name="home"),
    path("about/", views.about, name="about" ),
    path("blog/", views.blog, name="blog"),
    path("blog_detail/", views.blog_detail, name="blog_detail")
]
