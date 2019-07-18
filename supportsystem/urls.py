from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addpost', views.addpost, name='addpost'),
    path('viewposts', views.viewposts, name='viewposts'),
]
