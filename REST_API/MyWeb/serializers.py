from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    roll_no = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    college = serializers.CharField(max_length=100)



    def create(self, validated_data):
        return Student.objects.create(validated_data)




    def update(self, instance, validated_data):
        instance.roll_no = validated_data.get('name',instance.roll_no)
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('name', instance.city)
        instance.college = validated_data.get('name', instance.college)
        instance.save()
        return instance
