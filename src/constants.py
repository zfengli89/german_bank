# -*- coding: utf-8 -*-

'''
Created on 2019/7/8

@author: lizhifeng

@requirement:

@description:
'''
# 日志模块
import logging.handlers
logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)
handler1 = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler1.setFormatter(formatter)
logger.addHandler(handler1)

# 离散、连续变量表头
DISCRETE_VARIABLE =  ['信用好坏', '帐户余额','之前的信贷的付款状态','贷款目的','存款/股票价值','当前就业的时间长度',
                   '分期付款','性别婚姻状况','担保人','在当前地址居住时间','提供最有价值的资产',
                   '其他信用卡情况','公寓类型','信用卡数','职业','有无家属','有无电话','是否国外工作者']
CONTIN_VARIABLE = ['信贷金额','年龄','信贷期限']


