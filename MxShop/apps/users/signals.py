# -*- coding:utf-8 -*-
__author__ = 'Tony.Yang'


from  django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from  django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


user = get_user_model()

@receiver(post_save,sender = user)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()