
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_queryset(self):
        post = Post.objects.all()
        return post



# @api_view(['GET'])
# def listPosts(request):
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def postDetail(request, id):
#     post = Post.objects.get(pk=id)
#     serializer = PostSerializer(post, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def createPost(request):
#     post = request.data
#     serializer = PostSerializer(data=post)
#     if(serializer.is_valid()):
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['POST'])
# def updatePost(request, id):
#     post = Post.objects.get(pk=id)
#     serializer = PostSerializer(instance=post, data=request.data)
#     if(serializer.is_valid()):
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['GET'])
# def deletePost(request, id):
#     post = Post.objects.get(pk=id)
#     post.delete()
#     return Response("post deleted")