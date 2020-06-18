#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 系统日志处理方法



class systemUnderTest_log:
    """被测系统日志处理方法"""

    def __init__(self, parameter, argument=None):
        self.parameter = parameter
        self.argument = argument
        self.result = True


    def workOrder_reassignment(self, WorkOrderNumber, state, number):
        """
        取出工单的操作日志
        :param WorkOrderNumber: 工单编号
        :param state: 工单状态
        :param number:用来判断需要获取的数据； content：判断修改内容  audit：判断修改时间
        :return:
        """
        operation = None;argument = None;TheHangFailed_time = "1";ToApplyForHang_time = "1";history = None
        parameter = None;CharacterName = None;jurisdiction = None;user_ID = None;single_operation = None
        # 判断工单在那个工单表里，主要用于工单ID
        if state == "外协_已关单" or state == "内部_已关单" or state == "内部_已撤销":
            parameter = "事件"
        else:
            parameter = "服务"
        data = []
        # list_data历史记录
        list_data = dataProcessing(parameter).database_WorkOrderNumber(WorkOrderNumber)
        m = len(list_data)
        n = m - 1
        print("WorkOrderNumber", WorkOrderNumber)
        while n >= 0:
            # 取出每条历史记录
            log_message = list_data[n]
            n = n - 1
            operation = log_message["操作"]
            # 判断需要获取数据类型
            if number == "content":
                if operation == "重新改派":
                    modification = log_message["修改内容"]
                    patt = re.compile(r"“(.*?)”", re.S)
                    history = patt.findall(modification)
                    single_operation = operation
            elif number == "audit":
                if operation == "申请挂起":
                    ToApplyForHang_time = log_message["操作时间"]
                    user_ID = log_message["用户ID"]
                elif operation == "挂起审核不通过" or operation == "解挂" or operation == "挂起审核通过" or operation == "解挂改派":
                    TheHangFailed_time = log_message["操作时间"]
        if number == "content" and single_operation == "重新改派":
            username = history[-1]
            # 根据运维工程师的名称查找所在群组
            argument = dataProcessing("username", "groupID").database_userinfo(username)
        elif number == "audit":
            # PendingApplications:正在申请挂起状态
            # processed：退出了挂起状态
            # Not_HangUp：表示日志里没有关于挂起的信息
            # jurisdiction:判断是运维组长还是运维工程师
            # 判断有没有挂起申请记录
            if ToApplyForHang_time != "1" and TheHangFailed_time != "1":
                # 判断是不是在挂起状态
                if ToApplyForHang_time > TheHangFailed_time:
                    argument = "PendingApplications"
                    CharacterName = dataProcessing.list_data = dataProcessing("userID", "roleName").database_userinfo(
                        user_ID)
                    CharacterName = CharacterName[0]
                    CharacterName = CharacterName["name"]
                    if CharacterName == "运维工程师":
                        jurisdiction = "0"
                    elif CharacterName == "运维经理":
                        jurisdiction = "1"
                elif ToApplyForHang_time < TheHangFailed_time:
                    argument = "processed"
                    jurisdiction = "1"
            elif ToApplyForHang_time != "1" and TheHangFailed_time == "1":
                argument = "PendingApplications"
                CharacterName = dataProcessing("userID", "roleName").database_userinfo(user_ID)
                CharacterName = CharacterName[0]
                CharacterName = CharacterName["name"]
                if CharacterName == "运维工程师":
                    jurisdiction = "0"
                elif CharacterName == "运维经理":
                    jurisdiction = "1"
            else:
                argument = "processed"
        return argument, jurisdiction