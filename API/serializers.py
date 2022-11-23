from rest_framework import serializers
from .models import ComplainRecord

class ComplainRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplainRecord
        fields = ['complain_number', 'name', 'location', 'mobile_number', 'Description', 'date_time', 'Resolved']