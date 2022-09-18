from django.urls import path
from . import views
app_name = 'api'


urlpatterns = [
    path('', views.movielist),
    path('<int:pk>/', views.moviedetail),
]