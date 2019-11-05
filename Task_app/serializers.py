from rest_framework import serializers
from Task_app.models import Data,File
class Dataserializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields='__all__'
#
# class Fileviewserializer(serializers.ModelSerializer):
#     class Meta:
#         model=File
#         fields='__all__'