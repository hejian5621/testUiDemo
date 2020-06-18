#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo


class dictionaries:
    """字典数据处理"""


    def __init__(self,JSESSIONID,parameters):
        self.JSESSIONID=JSESSIONID  # Session:登录状态
        self.parameters = parameters  # 需要编译的参数
        



    def ADictionaryTable(self):
        """
        把状态参数编译成状态名称
        :return: 返回中文状态名称
        """
        WorkOrderStatus=None
        # # 判断传过来的工单状态是否是数字，如果不是数字，直接返回传过来的参数，如果是数字编译在字典表里编译成str类型的数据返回
        # data_type = dataType_dispose_method(self.parameters ).acquire_dataType()
        if self.parameters  == "0" or self.parameters  == "1" or self.parameters  == "2" or self.parameters  == "3"or self.parameters  == "4" or self.parameters  == "5" or self.parameters  == "6" \
            or self.parameters  == "7"  or self.parameters  == "8"  or self.parameters  == "9"  or self.parameters  == "10"  or self.parameters  == 0  or self.parameters  == 1  or self.parameters  == 2 \
                or self.parameters  == 3  or self.parameters  == 4  or self.parameters  == 5  or self.parameters  == 6  or self.parameters  == 7  or self.parameters  == 8  or self.parameters  == 9 or self.parameters  == 10:
            self.parameters =str(self.parameters )
            list1 = rests(self.JSESSIONID, "ticket_self.parameters ").getDictByKey()  # 工单状态
            m = len(list1)
            n = 0
            while n < m:
                data = list1[n]
                key_v = data["sort"]
                if key_v == self.parameters :
                    WorkOrderStatus = data["label"]
                    break
                n = n + 1
        else:
            WorkOrderStatus = self.parameters 
        return WorkOrderStatus
