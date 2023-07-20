from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add'),
    path('edit/<int:id>/',views.update_movie,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete')
]
