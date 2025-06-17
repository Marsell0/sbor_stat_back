from rest_framework import serializers
from apps.criteria.serializers import CriteriaSerializer
from .models import Report
from ..criteria.models import Criteria

class ReportSerializer(serializers.ModelSerializer):
    criteria = CriteriaSerializer(many=True, read_only=True)


    def create(self, validated_data):
        criteria_data = self.initial_data.get('criteria', [])
        report = Report.objects.create(**validated_data)
        report.criteria.set(criteria_data) 
        return report
    

    def update(self, instance, validated_data):
        criteria_data = self.initial_data.get('criteria', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if criteria_data is not None:
            instance.criteria.set(criteria_data)

        return instance


    class Meta:
        model = Report
        fields = [
            'id', 'event_name', 'about_event', 'date', 'members', 'user_id',
            'result', 'proofs', 'criteria', 'checked_by_head', 'date_created'
        ]
        read_only_fields = ['checked_by_head', 'date_created']

    
