# -*- coding:utf-8 -*-
__author__ = 'Tony.Yang'

from rest_framework import  serializers
from goods.models import Goods,GoodsCategory,GoodsImage


class CategorySerializer3(serializers.ModelSerializer):
    """
        商品分类 三级分类
    """
    class Meta:
        model = GoodsCategory
        # fields = fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"

class CategorySerializer2(serializers.ModelSerializer):
    """
        商品分类 二级分类
    """
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        # fields = fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
        商品一级分类
    """
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        # fields = fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodsSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(required=True,max_length=100)
    # click_num = serializers.IntegerField(required=False,default=0)
    # goods_front_image = serializers.ImageField()
    #
    # def create(self, validated_data):
    #     """
    #     ceate and return a new goods, given the validated data.
    #     :param validated_data:
    #     :return:
    #     """
    #     return Goods.objects.create(**validated_data)

    category = CategorySerializer()
    images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        # fields = fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"

