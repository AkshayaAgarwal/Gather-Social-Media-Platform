from django.urls import path
from . import views

urlpatterns = [
    path('Users/', views.Users,name='Users'),
    path('',views.Login,name='Login'),
    path('post/',views.Add_post,name='Add_post'),
    path('friends/',views.Search_friend,name='Search_friend'),
    path('friend2/',views.Add_friend,name='Add_friend'),
    path('comments/',views.Add_comment,name='Add_comment'),
    path('likes/',views.Add_like,name='Add_like')
]


