from rest_framework import serializers

from ..models import Task


class TaskCreationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Task
        fields = ['name', 'is_done', 'space']