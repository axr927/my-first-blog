from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new',views.post_new, name='post_new'),
    path('post/<int:pk>/edit',views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete',views.post_delete, name='post_delete'),
    path('cv_page',views.cv_page,name='cv_page'),
    path('cv_edit', views.cv_edit, name='cv_edit'),
]
