from django.urls import path
from . import views
app_name = 'api'


urlpatterns = [
    path('', views.WatchlistList.as_view()),
   # path('<int:pk>/', views.WatchlistDetail.as_view()),
    path('<int:pk>/', views.WatchlistList.as_view(), name='watchlist_list_create'),
    # path('<int:pk>/', views.Watchlistdetail),
    path('<int:pk>/crud/', views.WatchlistRetrieveUpdateDestroyApiView.as_view(), name='watchlist_detail'),
    path('platform/', views.StreamPlatformListCreateApiView.as_view(), name='stream_list_create'),
    path('platform/<int:pk>/', views.StreamPlatformRetriveUpdateDeleteApiView.as_view(), name='stream_detail'),
    path('review/', views.ReviewListCreateApiView.as_view(), name='review_list_create'),
    path('review/<int:pk>/', views.ReviewRetriveUpdateDeleteApiView.as_view(), name='review_detail'),
]