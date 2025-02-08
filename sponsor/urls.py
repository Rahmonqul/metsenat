from django.urls import  path
from .views import SponsorListCreateView, SponsorDetailView

urlpatterns=[
    path('sponsor/', SponsorListCreateView.as_view(), name='sponsor-list-create'),
    path('sponsor/<int:pk>/', SponsorDetailView.as_view(), name='sponsor-detail'),  # GET / PUT / PATCH / DELETE
]