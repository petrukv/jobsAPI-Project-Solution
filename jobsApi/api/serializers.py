from rest_framework import serializers

from jobsApi.models import *


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffers
        fields = "__all__"
