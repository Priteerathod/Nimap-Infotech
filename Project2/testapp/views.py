from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
@api_view(['GET'])
def get_client(request):
    client_list=Client.objects.all()
    serializer=ClientSerializer(client_list,many=True)
    return Response({'data':serializer.data})

@api_view(['GET'])
def get_project(request):
    client_list=Project.objects.all()
    serializer=ProjectSerializer(client_list,many=True)
    return Response({'data':serializer.data})


@api_view(['POST'])
def create_client(request):
    data=request.data
    serializer=ClientSerializer(data=request.data)
    if serializer.is_valid():
        print("Success")
        serializer.save()
        return Response({'data':serializer.data})
    
@api_view(['PUT'])
def put_client(request,id):
    try:
        client_list=Client.objects.get(id=id)
        serializer=ClientSerializer(client_list,data=request.data)
        if serializer.is_valid():
            print("Success")
            serializer.save()
            return Response({'data':serializer.data})
    except Exception as e:
        print(e)
        return Response({"message":"Invalid id"})

@api_view(['PATCH'])
def patch_client(request,id):
    try:
        client_list=Client.objects.get(id=id)
        serializer=ClientSerializer(client_list,data=request.data, partial=True)
        if serializer.is_valid():
            print("Success")
            serializer.save()
            return Response({'data':serializer.data})
    except Exception as e:
        print(e)
        return Response({"message":"Invalid id"})

@api_view(['DELETE'])
def delete_client(request,id):
    try:
        client_list=Client.objects.get(id=id)
        client_list.delete()
        return Response({'status':204})
    except Exception as e:
        print(e)
        return Response({'status':"Invalid id"})