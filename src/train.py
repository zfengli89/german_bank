# -*- coding: utf-8 -*-

'''
Created on 2019/7/9

@author: lizhifeng

@requirement: python3.5

@description:
'''

import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from src.constants import logger
from sklearn.metrics import classification_report

def read_data(file_path):
    '''
    数据读取
    :return:
    '''
    return pd.read_csv(file_path)

def preprocess(X, y):
    '''
    预处理
    :return:
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)
    return X_train, X_test, y_train, y_test

def train(X_train, y_train):
    '''
    模型训练
    :return:
    '''
    # 决策树模型
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    return model

def score(X_test, y_test, model):
    '''
    模型评估
    :return:
    '''
    y_predict = model.predict(X_test)
    logger.info("**** 准确率 ****")
    logger.info(accuracy_score(y_test, y_predict))
    logger.info("**** 混淆矩阵 ****")
    logger.info(confusion_matrix(y_test, y_predict))
    logger.info(classification_report(y_predict, y_test, target_names=['信用坏', '信用好']))

if __name__ == '__main__':
    y_key = ["信用好坏"]
    x_keys = ['帐户余额','信贷期限','之前的信贷的付款状态','贷款目的','信贷金额'
            ,'存款/股票价值','当前就业的时间长度','分期付款','性别婚姻状况','担保人'
            ,'在当前地址居住时间','提供最有价值的资产','年龄','其他信用卡情况','公寓类型'
            ,'信用卡数','职业','有无家属','有无电话','是否国外工作者']
    logger.info("数据读取")
    df_data = read_data('../data/german_credit.csv')
    # 制作数据集
    y_data = df_data[y_key]
    X_data = df_data[x_keys]
    logger.info("数据预处理")
    X_train, X_test, y_train, y_test = preprocess(X_data, y_data)
    logger.info("模型训练")
    tree_model = train(X_train, y_train)
    logger.info("模型评估")
    score(X_test, y_test, tree_model)
