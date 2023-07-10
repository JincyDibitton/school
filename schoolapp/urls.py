from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
app_name='schoolapp'


urlpatterns = [
    path("", views.index,name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add/', views.student_create_view, name='student_add'),
    path('<int:pk>/', views.student_update_view, name='student_change'),
    path('load_courses/', views.load_courses, name='load_courses'),
    path('confirm/',views.confirm, name='confirm'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)