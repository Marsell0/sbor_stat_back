from rest_framework import serializers
from apps.criteria.serializers import CriteriaSerializer
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    criteria = CriteriaSerializer(many=True, read_only=True)

    class Meta:
        model = Report
        fields = ['id', 'user', 'event_name', 'criteria', 'checked_by_head', 'date_created']