from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.consultorio, name='consultorio'),
    path('blog', views.blog, name='blog'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('blog/<str:title_slug>/', views.blog_detail, name='blog_detail'),
    path('blog/edit/<int:blog_id>/', views.edit_blog, name='edit_blog'), 
    path('blog/delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)