# -*- coding:utf-8 -*-
__author__ = 'Tony.Yang'

from MxShop.settings import REGEX_MOBILE
import re

if __name__ == '__main__':
    num = 186
    if re.match(REGEX_MOBILE,'186'):
        print(re)
        print(True)
    else:
        print(False)