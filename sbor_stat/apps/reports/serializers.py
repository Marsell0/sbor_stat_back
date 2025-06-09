from rest_framework import serializers
from apps.criteria.serializers import CriteriaSerializer
from .models import Report
from ..criteria.models import Criteria

class ReportSerializer(serializers.ModelSerializer):
    criteria = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Criteria.objects.all()
    )

    class Meta:
        model = Report
        fields = [
            'id', 'event_name', 'about_event', 'date', 'members',
            'result', 'proofs', 'criteria', 'checked_by_head', 'date_created'
        ]
        read_only_fields = ['checked_by_head', 'date_created']