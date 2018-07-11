from django.shortcuts import render
from rest_framework import mixins
from rest_framework  import  viewsets
from utils.permission import IsOwnerOrReadOnly
from rest_framework.permissions import  IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.
from .models import UserFav
from .serializer import  UserFavSerilaizer


class UserFavViewset(mixins.CreateModelMixin,mixins.ListModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet, mixins.DestroyModelMixin):


    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    serializer_class = UserFavSerilaizer
    authentication_classes = (JSONWebTokenAuthentication,)
    lookup_field = "goods_id"
    def get_queryset(self):
        return  UserFav.objects.filter(user=self.request.user)

