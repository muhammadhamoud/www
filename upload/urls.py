from django.urls import path
from upload import views

urlpatterns = [
    # path('file/upload/', views.future, name='upload'),
    path('file/list/', views.upload_show_list, name='file_list'),
    path('file/<int:pk>/', views.delete_file, name='delete_file'),
    path('file/sample_report/', views.sample_report, name='sample_report'),
    path('file/import_files/', views.import_files_view, name='import_files'),
]
