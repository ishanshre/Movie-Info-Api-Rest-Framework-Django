from django.urls import path
from . import views
app_name = 'api'


urlpatterns = [
    path('', views.MovieList.as_view()),
    path('<int:pk>/', views.MovieDetail.as_view()),
    # path('<int:pk>/', views.moviedetail),
]