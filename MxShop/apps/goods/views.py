from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import GoodsSerializer

from .models import Goods
# Create your views here.
class GoodsListView(APIView):
    """
    List all goods
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        serializer = GoodsSerializer(goods, many=True)
        return Response(serializer.data)