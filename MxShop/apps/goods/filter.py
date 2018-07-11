# -*- coding:utf-8 -*-
__author__ = 'Tony.Yang'

from rest_framework import generics
import django_filters
from .models import Goods
from django.db.models import Q


class GoodsFilter(django_filters.rest_framework.FilterSet):
    pricemin = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    name = django_filters.CharFilter(name = 'name',lookup_expr='icontains')
    top_category = django_filters.NumberFilter(method='top_category_flter')

    def top_category_flter(self,queryset,name,value):
        return  queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin','pricemax','is_hot']