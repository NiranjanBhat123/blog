from django.contrib import admin
from django.urls import path,re_path
from .import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.article_list)
    
    
]