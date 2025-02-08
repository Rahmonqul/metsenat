from django.urls import path
from .views import StudentListCreateView, StudentDetailView

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),  # GET / PUT / PATCH / DELETE
]
