from rest_framework import serializers
from RjSite.models import Parent,Teacher,Student
# todo: import specific models instead of the entier database,


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('email','name')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('email','name')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('email','name','colleges','studentTeacher', 'studentParent')

