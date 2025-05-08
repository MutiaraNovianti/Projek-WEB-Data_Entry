from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


app_name = 'data_entry'

urlpatterns = [
    path('', views.set_pengguna, name='set_pengguna'),
    path('data_entry/', views.set_data_entry, name='set_data_entry'),
    path('content/', views.set_content, name='set_content'),
    path('pengguna/view/<id>/', views.view_pengguna, name='view_pengguna'),
    path('api/pengguna/<int:user_id>/', views.get_pengguna_detail_api, name='get_pengguna_detail_api'),
    path('pengguna/<int:id>/delete/', views.delete_pengguna, name='delete_pengguna'),
    path('pengguna/<int:id>/edit/', views.update_pengguna, name='update_pengguna'),
    path('content/<int:id>/view/', views.view_content, name='view_content'),
    path('content/<int:id>/edit/', views.edit_content, name='edit_content'),
    path('content/<int:id>/delete/', views.delete_content, name='delete_content'),
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)