from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from jobsApi.api.serializers import *
from jobsApi.models import *


class JobsListCreateAPIView(APIView):
    def get(self, request):
        jobs = JobOffers.objects.filter(available=True)
        serializer = JobsSerializer(jobs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status.HTTP_400_BAD_REQUEST)
    

class JobsDetailAPIView(APIView):
    def get_object(self, pk):
        job = get_object_or_404(JobOffers, pk=pk)
        return job
    
    def get(self, request, pk):
        job = self.get_object(pk)
        serializer = JobsSerializer(job)
        return Response(serializer.data)
    
    def put(self, request, pk):
        job = self.get_object(pk)
        serializer = JobsSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        job = self.get_object(pk=pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
