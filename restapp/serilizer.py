from rest_framework import serializers
from restapp.models import Userdata


class Userdataseriliazer(serializers.ModelSerializer):
    name=serializers.CharField()
    password=serializers.IntegerField()
    mobile=serializers.CharField()


    class Meta:
        model=Userdata
        fields=("__all__")