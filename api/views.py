from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from . import firebase_Auth
from rest_framework import permissions, viewsets
from django.conf import settings
import os
from .firebase_operations import upload_file, download_file, delete_file
from django.shortcuts import get_object_or_404


class FileUploadView(APIView):
    """Class for uploading file
    
    Arguments:
        APIView -- Default View for API
    """

    parser_class = (MultiPartParser,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """        
        Arguments:
            request -- Contains the parameters of the request sent
        """
        user_id = request.user.username
        request.data["owner"] = user_id
        files = request.FILES["file"]
        file_path = os.path.join(settings.MEDIA_ROOT, files.name)

        if os.path.exists(file_path) is True:  # Avoid adding duplicate entries
            print("Entry already exists")
            return Response(status=status.HTTP_205_RESET_CONTENT)
        if request.POST.get("name", False) is False:
            request.data["name"] = files.name  # Assigning name of the file to the model
        modelinstance = File(file=files)
        modelinstance.save()
        """Creating a model instance copies the file to MEDIA_ROOT/media directory. 
        Required since to upload a file the path of file is required. 
        So a model instance is created so file is saved, then uploaded to FIREEBASE and then deleted.
        The uploaded URL is then passed on to request to make a serializer        
        """
        request.data["file_url"] = upload_file(files.name, user_id)
        os.remove(file_path)
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(file_serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        apis = File.objects.filter(owner=request.user)
        serializer = FileSerializer(apis, many=True)
        return Response(serializer.data)


class DetailView(APIView):
    """Provides a detail view, showing individual records.
    Can be accessed by adding 'LOCALHOST_URL/<pk>' 
    pk is the primary key which corresponds to unique records    
    """

    def delete(self, request, pk):
        instances = get_object_or_404(File, pk=pk)
        serializer = FileSerializer(instances)
        delete_file(serializer.data["name"], serializer.data["owner"])
        instances.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk):
        instances = get_object_or_404(File, pk=pk)
        serializer = FileSerializer(instances)
        return Response(serializer.data)

    def post(self, request, pk):
        instances = get_object_or_404(File, pk=pk)
        serializer = FileSerializer(instances)
        file_name = serializer.data["name"]
        owner = serializer.data["owner"]
        download_file(file_name, owner)
