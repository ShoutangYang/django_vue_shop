# -*- coding:utf-8 -*-
__author__ = 'Tony.Yang'

from rest_framework import serializers
from .models import UserFav
import re
from rest_framework import  serializers
from rest_framework.validators import  UniqueTogetherValidator

class UserFavSerilaizer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model= UserFav
        validators = [
            UniqueTogetherValidator(
                queryset= UserFav.objects.all(),
                fields=("user","goods"),
                message="已经收藏"
            )
        ]
        fields = ("user","goods","id")