from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from . import firebase_Auth
from rest_framework import permissions, viewsets
from .permissions import IsOwnerorReadOnly

firebase_Auth.login_firebase()


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request.data["owner"] = request.user.username

        if request.POST.get("name", False) is False:
            request.data["name"] = request.FILES["file"].name

        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        apis = File.objects.filter(owner=request.user)
        serializer = FileSerializer(apis, many=True)
        return Response(serializer.data)

