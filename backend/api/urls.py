from django.urls import path
from . import views
app_name = 'api'


urlpatterns = [
    path('', views.WatchlistList.as_view()),
   # path('<int:pk>/', views.WatchlistDetail.as_view()),
    path('<int:pk>/', views.WatchlistList.as_view()),
    # path('<int:pk>/', views.Watchlistdetail),
    path('<int:pk>/crud/', views.WatchlistRetrieveUpdateDestroyApiView.as_view()),
    path('platform/', views.StreamPlatformListCreateApiView.as_view()),
    path('platform/<int:pk>/', views.StreamPlatformRetriveUpdateDeleteApiView.as_view()),
]