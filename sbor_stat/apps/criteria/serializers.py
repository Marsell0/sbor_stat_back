from rest_framework import serializers
from .models import Criteria
from ..reports.models import Report

class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = ['id', 'name', 'point']



