""" 
Using function Based view
"""



# from django.shortcuts import render
# from .serializer import MovieSerializer
# from apps_watchlist.models import Movie
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# # Create your views here.

# @api_view(['GET', 'POST'])
# def movielist(request):
#     if request.method =='GET':
#         movie = Movie.objects.all()
#         serializer = MovieSerializer(movie, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT','DELETE'])
# def moviedetail(request, pk):
#     if request.method == 'GET':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method =="PUT":
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
    
#     if request.method == "DELETE":
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# """
# Using Mixins. one of the class based views
# """
# from rest_framework import mixins
# from rest_framework import generics
# from .serializer import MovieSerializer
# from apps_watchlist.models import Movie


# class MovieList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     serializer_class = MovieSerializer

#     def get_queryset(self):
#         return Movie.objects.all()
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class MovieDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     serializer_class = MovieSerializer
    
#     queryset = Movie.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args,**kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)


from .serializer import MovieSerializer
from rest_framework import generics
from apps_watchlist.models import Movie


class MovieList(generics.ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()

class MovieRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()