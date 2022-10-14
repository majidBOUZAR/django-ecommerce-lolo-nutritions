from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('category/<str:slug>', views.cat_blog, name='cat_blog'),
]
