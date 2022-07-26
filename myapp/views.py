from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from misc.Custom_Permission import IsOwner
from myapp.models import Student
from myapp.serializers import StudentSerializers
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import generics
from misc.custome_generic_view import PartialUpdateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


# @csrf_exempt
# @api_view
# def Student_list(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializers(students, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = StudentSerializers(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#
#         return JsonResponse(serializer.errors, status=400)

#
# class StudentView(APIView):
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializers(students, many=True)
#         return Response(serializer.data)


# class StudentView(generics.ListAPIView):
#     serializer_class = StudentSerializers
#     queryset = Student.objects.all()

# class StudentView(generics.CreateAPIView):
#     serializer_class = StudentSerializers
#     queryset = Student.objects.all()

class StudentView(generics.ListCreateAPIView):
    serializer_class = StudentSerializers
    queryset = Student.objects.all()
    permission_classes = (IsOwner,)


# class StudentView(generics.RetrieveAPIView):
#     serializer_class = StudentSerializers
#     queryset = Student.objects.all()

# class StudentView(generics.RetrieveUpdateAPIView):
#     serializer_class = StudentSerializers
#     queryset = Student.objects.all()
#     permission_classes = (IsOwner,)


# class StudentView(generics.RetrieveDestroyAPIView):
#     serializer_class = StudentSerializers
#     queryset = Student.objects.all()

class RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializers
    queryset = Student.objects.all()


class PartialUpdateView(PartialUpdateView):
    serializer_class = StudentSerializers
    queryset = Student.objects.all()
