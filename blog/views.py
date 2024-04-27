from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import filters,status,generics
from .models import Post, Comment
from rest_framework.decorators import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
#from django_filters.rest_framework import DjangoFilterBackend


class BlogPostSearch(APIView):
    @swagger_auto_schema(
        operation_summary="Search for entered string",
        operation_description="searchs both content and title field if the instances contain a pattern of the string entered",
    )
    def post(self, request):
        serializer = SearchFormSerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.validated_data['query']
            blog_posts = Post.objects.filter(title__icontains=query)
            blog_posts1 = Post.objects.filter(content__icontains=query)
            serializer1 = PostSerializer(blog_posts, many=True)
            serializer2 = PostSerializer(blog_posts1, many=True)
            combined_data = {
            'posts1': serializer1.data,
            'posts2': serializer2.data
            }
            return Response(data=combined_data,status=status.HTTP_202_ACCEPTED
                            )
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class postview(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    #serializer_class = PostSerializer
    @swagger_auto_schema(
        operation_summary="Display all post",
        operation_description="shows all post in the data base",
    )
    def get(self,request:Request,*args,**kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(instance=posts,many=True)
        return Response(data = serializer.data,status = status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_summary="Create a new post",
        operation_description="enter title and content",
    )
    def post(self,request:Request,*args,**kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"post created",
                "data":serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

class postupdatedelete(APIView):
    serializer_class = PostSerializer
    @swagger_auto_schema(
        operation_summary="Get a particular post",
        operation_description="fetch only one post by appending its id at the end of the url",
    )
    def get(self,request:Request,post_id:int):
        post = get_object_or_404(Post,id=post_id)
        serializer = self.serializer_class(instance=post)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_summary="Update a post",
        operation_description="update a particular post in the database by appending its id at the end of the url",
    )
    def put(self,request:Request,post_id:int):
        post = get_object_or_404(Post,id=post_id)
        data = request.data
        serializer = self.serializer_class(instance=post,data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"Post updated",
                "data":serializer.data
            }
            return Response(data=response,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)        
    @swagger_auto_schema(
        operation_summary="Delete a post",
        operation_description="delete a particular post in the database by appending its id at the end of the url",
    )
    def delete(self,request:Request,post_id:int):
        post = get_object_or_404(Post,id=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     
class CommentView(APIView):
    serializer_class = CommentSerializer
    @swagger_auto_schema(
        operation_summary="view all post",
        #operation_description="update a particular post in the database by appending its id at the end of the url",
    )
    def get(self,request:Request,*args,**kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(instance=posts,many=True)
        return Response(data = serializer.data,status = status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_summary="comment on a post",
        operation_description="comment on a particular post in the database by appending its id at the end of the url",
    )
    def post(self,request:Request,post_id:int):
        post = get_object_or_404(Post,id=post_id)
        data = request.data
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(post=post)
            response = {
                "message":"comment created",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class commentupdatedelete(APIView):
    serializer_class = CommentupdateSerializer
    @swagger_auto_schema(
        operation_summary="view all post with their comments",
        #operation_description="comment on a particular post in the database by appending its id at the end of the url",
    )
    def get(self,request:Request,*args,**kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(instance=posts,many=True)
        return Response(data = serializer.data,status = status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_summary="Update A comment",
        operation_description="update a particular comment on a particular post in the database by appending its id at the end of the url http://127.0.0.1:8000/blog/commentadjust/id",
    )
    def put(self,request:Request,comment_id:int):
        comment = get_object_or_404(Comment,id=comment_id)
        data = request.data
        serializer = CommentupdateSerializer(instance=comment, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"comment updated",
                "data":serializer.data
            }
            return Response(data=response,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
        operation_summary="delete a comment",
        operation_description="delete a comment on a particular post in the database by appending its id at the end of the url http://127.0.0.1:8000/blog/commentadjust/delete/id",
    )        
    def delete(self,request:Request,comment_id:int):
        comment = get_object_or_404(Comment,id=comment_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

@swagger_auto_schema(
        operation_summary="uses django filter method to implement a search",
        operation_description="you use it like so http://127.0.0.1:8000/blog/search/?search=russell",
    )
class searchview(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']           
        
        
        
            
# Create your views here.
