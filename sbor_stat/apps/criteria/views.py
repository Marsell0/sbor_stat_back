from django.shortcuts import render
# from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from .models import Criteria
from .serializers import CriteriaSerializer

class CriteriaViewSet(viewsets.ModelViewSet):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer
    # permission_classes = [IsAdminUser]  # Только администратор может
