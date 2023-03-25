from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

# Local
from .serializers import ProfileSerializer


class ProfileAPIView(APIView):
    def get(self, request):
        profile = User.objects.all()
        return Response({"profile": ProfileSerializer(profile, many=True).data,})

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"profile": serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.pk("pk", None)
        if not pk:
            return Response({"error": "Method delete not allowed"})
        try:
            instance = User.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"error": "Object does not exist"})
        return Response({"profile": "Successfulpy delete" + str(pk)})

    def put(self, request, *args, **kwargs):
        pk =kwargs.pk("pk", None)
        if not pk:
            return Response({"error": "Method put not allowed"})
        try:
            instance = User.objects.get(pk=pk)
        except:
            return Response({"error": "Method put not allowed"})
        
        serializer = ProfileSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"profile": serializer.data})
    