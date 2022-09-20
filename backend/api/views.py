""" 
Using function Based view
"""



# from django.shortcuts import render
# from .serializer import WatchlistSerializer
# from apps_watchlist.models import Watchlist
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# # Create your views here.

# @api_view(['GET', 'POST'])
# def Watchlistlist(request):
#     if request.method =='GET':
#         Watchlist = Watchlist.objects.all()
#         serializer = WatchlistSerializer(Watchlist, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = WatchlistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT','DELETE'])
# def Watchlistdetail(request, pk):
#     if request.method == 'GET':
#         Watchlist = Watchlist.objects.get(pk=pk)
#         serializer = WatchlistSerializer(Watchlist)
#         return Response(serializer.data)

#     if request.method =="PUT":
#         Watchlist = Watchlist.objects.get(pk=pk)
#         serializer = WatchlistSerializer(Watchlist, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
    
#     if request.method == "DELETE":
#         Watchlist = Watchlist.objects.get(pk=pk)
#         Watchlist.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# """
# Using Mixins. one of the class based views
# """
# from rest_framework import mixins
# from rest_framework import generics
# from .serializer import WatchlistSerializer
# from apps_watchlist.models import Watchlist


# class WatchlistList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     serializer_class = WatchlistSerializer

#     def get_queryset(self):
#         return Watchlist.objects.all()
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class WatchlistDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     serializer_class = WatchlistSerializer
    
#     queryset = Watchlist.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args,**kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)


from .serializer import WatchlistSerializer, StreamPlatformSerializer
from rest_framework import generics
from apps_watchlist.models import Watchlist, StreamPlatform


class WatchlistList(generics.ListCreateAPIView):
    serializer_class = WatchlistSerializer

    def get_queryset(self):
        return Watchlist.objects.all()

class WatchlistRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WatchlistSerializer

    def get_queryset(self):
        return Watchlist.objects.all()


class StreamPlatformListCreateApiView(generics.ListCreateAPIView):
    serializer_class = StreamPlatformSerializer
    queryset = StreamPlatform.objects.all()


class StreamPlatformRetriveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StreamPlatformSerializer
    queryset = StreamPlatform.objects.all()