#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 实际值得处理方法




class actual_value:
    """处理实际值"""

    def __init__(self,actual_list):
        self.actual_list=actual_list
        self.actual_list_value = []




    def add_Complaints_DateProcessing(self):
        """
        新增投诉信息，各个权限用户检查
        去掉实际投诉信息的“创建时间”和“更新时间”的时间留日期
        :return:
        """
        if  self.actual_list:
            for actual in self.actual_list:
                #取出投诉信息的创建时间和投诉信息的更新时间
                creationTime=actual["投诉信息的创建时间"]
                turnoverTime=actual["投诉信息的更新时间"]
                #截取投诉信息的创建时间和投诉信息的更新时间的日期
                creationTime_cutOut=creationTime[:10]
                turnoverTime_cutOut=turnoverTime[:10]
                actual["投诉信息的创建时间"]=creationTime_cutOut
                actual["投诉信息的更新时间"] = turnoverTime_cutOut
                self.actual_list_value.append(actual)
        else:
            self.actual_list_value = None
        # self.actual_list_value=[{'投诉标题': '1213005受理投诉标题', '投诉内容': '1213005受理投诉标题修改--受理-投诉记者了解到，包头市五当召消防救援站建于2017年8月，位于五当召景区内部，主要担负着五当召景区火灾事故的扑救和消防保卫、抢险救援任务。',
        #                          '投诉用户名称': '普通用户', '投诉用户id': '9d62886934e2444d9ba8168d8d8e958c', '投诉单状态': '1', '投诉信息的创建时间': '2019-12-13', '投诉信息的更新时间': '2019-12-13',
        #                          '被投诉人ID': 'a876338ffd6f4dfa9348474a2b7ace29', '任务办理': ['2']}]
        return self.actual_list_value
