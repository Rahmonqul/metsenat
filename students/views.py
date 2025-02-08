from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer
from .filters import StudentFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from sponsor.views import Pagination

class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.prefetch_related("sponsors").select_related("otm")
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StudentFilter
    pagination_class = Pagination
    search_fields = ['full_name', 'phone']

class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.prefetch_related("sponsors").select_related("otm")
    serializer_class = StudentSerializer