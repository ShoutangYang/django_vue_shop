# -*- coding:utf-8 -*-
__author__ = 'Tony.Yang'
from goods.models import Goods
from django.views.generic.base import  View
from django .views.generic import  ListView,TemplateView
from django.http import  HttpResponse,JsonResponse
import json
from  django.forms.models import model_to_dict
from django.core.serializers import  serialize
class GoodsListView(View):
    def get(self,request):
        """
        通过django 实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict={}
        #     json_dict["name"] = good.name
        #     json_dict["category"] = good.category.name
        #     json_dict["market_price"]= good.market_price

        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        json_list =serialize('json',goods)
        json_list = json.loads(json_list)
        return  JsonResponse(json_list,safe=False)
        # return HttpResponse(json.dumps(json_list),content_type='application/json')