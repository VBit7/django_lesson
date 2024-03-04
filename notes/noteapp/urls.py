from django.urls import path
from . import views


app_name = 'noteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('note/', views.note, name='note'),
    path('tag/', views.tag, name='tag'),
    path('detail/<int:note_id>', views.detail, name='detail'),
]
