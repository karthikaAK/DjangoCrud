from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404

class StudentView(APIView):
     def get(self, request, id=None): 
        if id: 
            result = Students.objects.get(id = id)  
            serializers = StudentSerializer(result)  
            return Response({"students":serializers.data}, status=200)  
  
        result = Students.objects.all()  
        serializers = StudentSerializer(result, many=True)  
        return Response({"students":serializers.data}, status=200)
     
     def post(self, request):  
        serializer = StudentSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"message": "Student data created successfully"}, status=201)  
        else:  
            return Response({"message": serializer.errors}, status=400)
          
    
     def patch(self, request, id=None):
        student = get_object_or_404(Students, id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": " Student data updated successfully"}, status=200)
        else:
            return Response({"message": serializer.errors}, status=400)
        
     def delete(self,request,id=None):
        student = get_object_or_404(Students, id=id)
        student.delete()
        return Response({"message":" Student data deleted successfully"})