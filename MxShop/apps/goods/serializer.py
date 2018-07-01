# -*- coding:utf-8 -*-
__author__ = 'Tony.Yang'

from rest_framework import  serializers
from .models import Goods

class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=100)
    click_num = serializers.IntegerField(required=False,default=0)

