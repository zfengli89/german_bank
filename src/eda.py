# -*- coding: utf-8 -*-

'''
Created on 2019/7/8

@author: lizhifeng

@requirement:

@description:
'''

import pandas as pd
import src.constants as constants
from src.constants import logger
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def load_data(file_path):
    return pd.read_csv(file_path)

def display_discrete_variable(df):
    '''
    离散变量预览
    :param df:
    :return:
    '''
    for col in df.columns:
        if col in constants.DISCRETE_VARIABLE:
            print(df[col].value_counts().sort_index())

def display_contin_variable(df):
    '''
    连续变量预览
    :param df:
    :return:
    '''
    contin_variable_dict = {}
    for col in df.columns:
        if col in constants.CONTIN_VARIABLE:
            contin_variable_dict[col] = df[col].values
            plt.figure(1)
            ax1 = plt.subplot()
            plt.boxplot(df[col].values, labels='x')
            ax1.set_xlabel(col)
            plt.show()

def check_null(df):
    '''
    空值检查
    :param df:
    :return:
    '''
    null_flag = True
    res = df.isnull().any()
    for feature in res.index.tolist():
        if res[feature] == True:
            logger.warn("特征列：%s 包含缺失值，请进行缺失值处理" % feature)
            null_flag = False
    if null_flag:
        logger.info("数据不存在缺失值，无需进行缺失值处理。")

if __name__ == '__main__':
    # load数据
    df_data = load_data('../data/german_credit.csv')
    # 缺失值检测
    check_null(df_data)
    # 离散特征预览
    display_discrete_variable(df_data)
    # 连续特征异常值判断  使用箱线图
    display_contin_variable(df_data)