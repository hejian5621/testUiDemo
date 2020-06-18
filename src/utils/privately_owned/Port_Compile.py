#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 接口返回数据编译


from config.readconfig import ProfileDataProcessing
from log import log
from privately_owned.method import  ProgressBar
import os


import sys




class workOrder_compile:
    """跟工单有关的接口编译"""

    def __init__(self, list_parameter):
        self.list_parameter = list_parameter
        self.list_work = []


    def connector_one(self,userinfo):
        """
        工单清单接口编译
        适用接口：sjTicketServe_details（工单详情）
        :return:
        """
        roleName=userinfo["用户权限"];schedule_number=1
        print("\033[1;34;40m%%%%%%%%%%%%%%%%%%%%%%开始编译接口返回的数据%%%%%%%%%%%%%%%%%%%%%%")
        # 判断如果工单列表为空就不编译工单
        if self.list_parameter:
            num=len(self.list_parameter)
            # 取出所有工单
            for workOrder in self.list_parameter:
                # 打印进度条
                ProgressBar(schedule_number, num)
                schedule_number = schedule_number + 1
                """初始参数"""
                WorkOrder_Number = None;int_state = None;state_name = None;applicant_id = None;applicant_name = None;office = None;office_name = None
                workOrder_title = None;time_creation = None;update_Date = None;handler_id = None;prbTp_id = None;prbTp_Nm = None;list_TaskToDealWith = []
                data_list=None;workOrder_ID=None;inOutTicket=None;prbTp=None;prbTp_id=None;prbTp_Nm=None;cuser=None;applicant_id=None;applicant_name=None
                office=None;office_name=None;user_handler=None;handler_id=None;TaskToDealWith=None;stateHang=None;userGroupId=None;description=None
                """获取参数"""
                WorkOrder_Number = workOrder["ticketServeCd"] # 获取工单编号
                update_Date = workOrder["updateDate"]         # 取出工单更新日期
                workOrder_title = workOrder["title"]          # 取出工单标题
                time_creation = workOrder["createDate"]       # 获取工单创建时间
                int_state = workOrder["state"]                # 取出整数类型工单的状态
                workOrder_ID =workOrder["id"]                 # 工单ID
                inOutTicket = workOrder["inOutTicket"]        # 工单范围
                if "description" in workOrder:
                    description = workOrder["description"]        # 工单描述
                if "userGroupId" in workOrder:
                    userGroupId = workOrder["userGroupId"]    # 工单所在群组ID
                if "stateHang" in workOrder:
                    stateHang = workOrder["stateHang"]        # 取出挂起字典
                if "prbTp" in workOrder:
                    prbTp = workOrder["prbTp"]
                    prbTp_id = prbTp["id"]
                    prbTp_Nm = prbTp["prbTpNm"]
                if "cuser" in workOrder:
                    cuser = workOrder["cuser"]                # 取出报修人信息
                    applicant_id = cuser["id"]                # 取出报修人ID
                    applicant_name=cuser["name"]              # 取出报修人名称
                    office = cuser["office"]                  # 取出报修人的单位信息
                    office_name = office["name"]              # 取出报修人单位名称
                if "user" in workOrder:
                    user_handler = workOrder["user"]          # 取出处理人信息
                    handler_id   = user_handler["id"]         # 取出处理人ID
                # 处理任务办理参数
                if "operationBtn" in  workOrder:
                    TaskToDealWith = workOrder["operationBtn"]
                    if "1" in TaskToDealWith:
                        TaskToDealWith.remove("1")                # 去掉联系人
                    if roleName=="运维工程师" or roleName=="运维经理" or roleName=="服务台" or roleName=="运维总监":
                        if "18" in TaskToDealWith:
                            TaskToDealWith.remove("18")               # 去掉投诉按钮
                    if TaskToDealWith:                            # 编译任务办理按钮
                        for i in TaskToDealWith:
                            ToDealWith=None
                            ToDealWith = ProfileDataProcessing( "TaskToDealWith", i).config_File()
                            list_TaskToDealWith.append(ToDealWith)
                if list_TaskToDealWith:
                    if    list_TaskToDealWith ==['催单', '投诉', '进度']:
                        list_TaskToDealWith =  ['进度', '投诉', '催单']
                    elif  list_TaskToDealWith ==['评论', '进度']:
                        list_TaskToDealWith =  ['进度', '评论']
                    elif list_TaskToDealWith == ['评论', '催单', '投诉', '进度']:
                        list_TaskToDealWith =  ['进度', '投诉', '评论', '催单']
                    elif list_TaskToDealWith ==  ['撤销', '进度', '内部处理', '外协处理']:
                        list_TaskToDealWith =  ['进度', '撤销', '内部处理', '外协处理']
                    elif list_TaskToDealWith ==   ['催单', '撤销', '进度']:
                        list_TaskToDealWith =  ['进度', '撤销', '催单']
                    elif list_TaskToDealWith ==    ['投诉', '进度']:
                        list_TaskToDealWith =   ['进度', '投诉']
                    elif list_TaskToDealWith ==    ['评论', '投诉', '进度']:
                        list_TaskToDealWith =   ['进度', '投诉', '评论']
                else:
                    list_TaskToDealWith=None
                # 存入工单参数
                data_list = {"工单编号": WorkOrder_Number,"工单标题": workOrder_title,"工单状态": int_state, "故障类型ID":prbTp_id,
                             "报修人ID":applicant_id,"工单ID": workOrder_ID,"报修人名称":applicant_name,"工单创建日期":time_creation ,"工单更新日期":update_Date,
                             "故障类型名称": prbTp_Nm,"工单处理人ID": handler_id,"报修人单位名称": office_name,"工单范围": inOutTicket,"挂起状态":stateHang,
                             "工单所在群组ID":userGroupId,"工单描述":description,"任务办理": list_TaskToDealWith}
                self.list_work.append(data_list)
            print("\033[1;34;40m编译出的实际值列表：%r" % self.list_work)
        else:
            print("\033[1;34;40m由于工单列表列表没有数据，所有没有编译资产列表")
            self.list_work = ["为空"]
        return self.list_work



    def compile_homePage(self,userinfo):
        """
       编译从接口返回的工单列表
       针对接口：
       1、小程序--首页--工单：noOffTicketListData
       2、小程序-事件-待响应、预约中、待处理、处理中、已处理、已关单、已挂起和全部工单；chooseListData、closedTicketListData、allListData
       JSESSIONID: session
       list_parameter: 没有编译的工单列表
       :return: 工单列表编译过的数据
       """
        roleName=userinfo["用户权限"];schedule_number=1
        print("\033[1;34;40m%%%%%%%%%%%%%%%%%%%%%%开始编译接口返回的数据%%%%%%%%%%%%%%%%%%%%%%")
        # 判断如果工单列表为空就不编译工单
        if self.list_parameter:
            num=len(self.list_parameter)
            # 取出所有工单
            for workOrder in self.list_parameter:
                # 打印进度条
                ProgressBar(schedule_number, num)
                schedule_number = schedule_number + 1
                """初始参数"""
                WorkOrder_Number = None;int_state = None;state_name = None;applicant_id = None;applicant_name = None;office = None;office_name = None
                workOrder_title = None;time_creation = None;update_Date = None;handler_id = None;prbTp_id = None;prbTp_Nm = None;list_TaskToDealWith = []
                data_list=None;workOrder_ID=None;inOutTicket=None;prbTp=None;prbTp_id=None;prbTp_Nm=None;cuser=None;applicant_id=None;applicant_name=None
                office=None;office_name=None;user_handler=None;handler_id=None;TaskToDealWith=None;stateHang=None;userGroupId=None
                """获取参数"""
                WorkOrder_Number = workOrder["ticketServeCd"] # 获取工单编号
                update_Date = workOrder["updateDate"]         # 取出工单更新日期
                workOrder_title = workOrder["title"]          # 取出工单标题
                time_creation = workOrder["createDate"]       # 获取工单创建时间
                int_state = workOrder["state"]                # 取出整数类型工单的状态
                workOrder_ID =workOrder["id"]                 # 工单ID
                inOutTicket = workOrder["inOutTicket"]        # 工单范围
                if "userGroupId" in workOrder:
                    userGroupId = workOrder["userGroupId"]    # 工单所在群组ID
                if "stateHang" in workOrder:
                    stateHang = workOrder["stateHang"]        # 取出挂起字典
                if "prbTp" in workOrder:
                    prbTp = workOrder["prbTp"]
                    prbTp_id = prbTp["id"]
                    prbTp_Nm = prbTp["prbTpNm"]
                if "cuser" in workOrder:
                    cuser = workOrder["cuser"]                # 取出报修人信息
                    applicant_id = cuser["id"]                # 取出报修人ID
                    applicant_name=cuser["name"]              # 取出报修人名称
                    office = cuser["office"]                  # 取出报修人的单位信息
                    office_name = office["name"]              # 取出报修人单位名称
                if "user" in workOrder:
                    user_handler = workOrder["user"]          # 取出处理人信息
                    handler_id   = user_handler["id"]         # 取出处理人ID
                # 处理任务办理参数
                if "operationBtn" in  workOrder:
                    TaskToDealWith = workOrder["operationBtn"]
                    if "1" in TaskToDealWith:
                        TaskToDealWith.remove("1")                # 去掉联系人
                    if roleName=="运维工程师" or roleName=="运维经理" or roleName=="服务台" or roleName=="运维总监":
                        if "18" in TaskToDealWith:
                            TaskToDealWith.remove("18")               # 去掉投诉按钮
                    if TaskToDealWith:                            # 编译任务办理按钮
                        for i in TaskToDealWith:
                            ToDealWith=None
                            ToDealWith = ProfileDataProcessing( "TaskToDealWith", i).config_File()
                            list_TaskToDealWith.append(ToDealWith)
                if list_TaskToDealWith:
                    if list_TaskToDealWith == ['催单', '投诉', '进度']:
                        list_TaskToDealWith = ['进度', '投诉', '催单']
                    elif list_TaskToDealWith == ['评论', '进度']:
                        list_TaskToDealWith = ['进度', '评论']
                    elif list_TaskToDealWith == ['评论', '催单', '投诉', '进度']:
                        list_TaskToDealWith = ['进度', '投诉', '评论', '催单']
                    elif list_TaskToDealWith == ['撤销', '进度', '内部处理', '外协处理']:
                        list_TaskToDealWith = ['进度', '撤销', '内部处理', '外协处理']
                    elif list_TaskToDealWith == ['催单', '撤销', '进度']:
                        list_TaskToDealWith = ['进度', '撤销', '催单']
                # 存入工单参数
                data_list = {"工单编号": WorkOrder_Number,"工单标题": workOrder_title,"工单状态": int_state, "故障类型ID":prbTp_id,
                             "报修人ID":applicant_id,"工单ID": workOrder_ID,"报修人名称":applicant_name,"工单创建日期":time_creation ,"工单更新日期":update_Date,
                             "故障类型名称": prbTp_Nm,"工单处理人ID": handler_id,"报修人单位名称": office_name,"工单范围": inOutTicket,"挂起状态":stateHang,
                             "工单所在群组ID":userGroupId,"任务办理": list_TaskToDealWith}
                self.list_work.append(data_list)
            print("\033[1;34;40m编译出的实际值列表：%r" % self.list_work)
        else:
            print("\033[1;34;40m由于工单列表列表没有数据，所有没有编译资产列表")
            self.list_work = ["为空"]
        return self.list_work


    def WorkOrderProcess_closedTicketListData(self,userinfo):
        """
        closedTicketListData
        服务端-事件-已关单
        self.list_parameter：
        :return:
        """
        roleName = userinfo["用户权限"]
        n = 1
        # 判断接口返回的数据是否为空
        if self.list_parameter:
            for dict_WorkOrder in self.list_parameter:
                workOrder_ID = None;stateHang=None;createBy = None;createBy_ID = None;create_Date = None;updateBy = None;updateBy_ID = Noneupdate_Date = NoneticketServeCd = None
                prbTp = None;prbTp_ID = None;prbTp_Nm = None;title = None;description = None;cuser = None;cuser_ID = None;cuser_name = None;cuser_office = None;cuser_office_name = None
                state = None;cuser_office_name = None;cuser_name = None;ticketServeType = None;handler_ID = None;customerPhone = None
                inOutTicket = None;orderSlot = None;user = None;handler_ID = None;TaskToDealWith = None
                ##################################################
                ticketServeCd = dict_WorkOrder["ticketServeCd"]  # 取出工单编号
                title = dict_WorkOrder["title"]  # 取出工单标题
                state = dict_WorkOrder["state"]  # 取出工单状态
                if "prbTp" in dict_WorkOrder:  # 判断有没有故障类型信息
                    prbTp = dict_WorkOrder["prbTp"]  # 取出故障类型信息
                    prbTp_ID = prbTp["id"]  # 取出故障类型ID
                    prbTp_Nm = prbTp["prbTpNm"]  # 取出故障类型名称
                if "cuser" in dict_WorkOrder:  # 判断有没有报修人信息
                    cuser = dict_WorkOrder["cuser"]  # 取出报修人信息
                    cuser_ID = cuser["id"]  # 取出报修人ID
                    cuser_name = cuser["name"]  # 取出报修人名称
                    if "office" in cuser:  # 判断有没有报修人单位信息
                        cuser_office = cuser["office"]  # 取出报修人单位信息
                        cuser_office_name = cuser_office["name"]  # 取出报修人单位名称
                workOrder_ID = dict_WorkOrder["id"]  # 获取工单ID
                if "createBy" in dict_WorkOrder:  # 判断有没有创建人
                    createBy = dict_WorkOrder["createBy"]  # 取出创建人信息
                    createBy_ID = createBy["id"]  # 取出创建人ID
                create_Date = dict_WorkOrder["createDate"]  # 工单创建日期
                update_Date = dict_WorkOrder["updateDate"]  # 取出工单更新时间
                inOutTicket = dict_WorkOrder["inOutTicket"]  # 取出工单范围
                if "ticketServeType" in dict_WorkOrder:
                    ticketServeType = dict_WorkOrder["ticketServeType"]  # 取出服务类型
                if "stateHang" in dict_WorkOrder:
                    stateHang = dict_WorkOrder["stateHang"]  # 取出挂起状态字段
                """增加任务办理按钮"""
                list_TaskToDealWith = []
                TaskToDealWith = dict_WorkOrder["operationBtn"]
                if "1" in TaskToDealWith:
                    TaskToDealWith.remove("1")  # 去掉联系人
                if roleName == "运维工程师" or roleName == "运维经理" or roleName == "服务台" or roleName == "运维总监":
                    if "18" in TaskToDealWith:
                        TaskToDealWith.remove("18")  # 去掉投诉按钮
                if TaskToDealWith:  # 编译任务办理按钮
                    for i in TaskToDealWith:
                        ToDealWith = None
                        ToDealWith = ProfileDataProcessing("TaskToDealWith", i).config_File()
                        list_TaskToDealWith.append(ToDealWith)
                if list_TaskToDealWith:
                    if list_TaskToDealWith == ['催单', '投诉', '进度']:
                        list_TaskToDealWith = ['进度', '投诉', '催单']
                    elif list_TaskToDealWith == ['评论', '进度']:
                        list_TaskToDealWith = ['进度', '评论']
                    elif list_TaskToDealWith == ['评论', '催单', '投诉', '进度']:
                        list_TaskToDealWith = ['进度', '投诉', '评论', '催单']
                    elif list_TaskToDealWith == ['撤销', '进度', '内部处理', '外协处理']:
                        list_TaskToDealWith = ['进度', '撤销', '内部处理', '外协处理']
                    elif list_TaskToDealWith == ['催单', '撤销', '进度']:
                        list_TaskToDealWith = ['进度', '撤销', '催单']
                """生成工单"""
                dict_compiled_complain = {"工单编号": ticketServeCd, "工单标题": title, "工单状态": state, "故障类型ID": prbTp_ID,"故障类型名称": prbTp_Nm,"报修人ID": cuser_ID,
                                          "报修人名称": cuser_name, "报修人单位名称": cuser_office_name,"工单ID": workOrder_ID, "工单创建人ID": createBy_ID,"工单创建日期": create_Date,
                                          "工单更新日期": update_Date, "工单范围": inOutTicket,"工单描述": description, "预约时间段": orderSlot,"服务类型": ticketServeType,
                                          "挂起状态": stateHang,"任务办理": list_TaskToDealWith}
                """生成工单列表"""
                self.list_work.append(dict_compiled_complain)
                n = n + 1
            print("\033[1;34;40m编译完成的实际值：\033[0m\033[4;35;40m%r" % self.list_work)
        else:
            print("\033[1;34;40m*******由于实际投诉列表没有数据，所有没有编译投诉列表*******")
            self.list_work = None
        return self.list_work










    def WorkOrderProcess_allListData(self,FilterParameters):
        """
        allListData
        客户端-报修广场-已完成；客户端-报修广场-全部；首页-紧急报修-未完成；首页-紧急报修-已完成；首页-紧急报修-全部
        首页-驻场服务-未完成；首页-驻场服务-已完成；首页-驻场服务-全部；服务端-事件-全部工单
        self.list_parameter：
        :return:
        """
        roleName = FilterParameters["用户权限"]; selected_module=FilterParameters["所属模块"]
        n = 1
        # 判断接口返回的数据是否为空
        if self.list_parameter:
            for dict_WorkOrder in self.list_parameter:
                workOrder_ID = None;stateHang=None;createBy = None;createBy_ID = None;create_Date = None;updateBy = None;updateBy_ID = Noneupdate_Date = NoneticketServeCd = None
                prbTp = None;prbTp_ID = None;prbTp_Nm = None;title = None;description = None;cuser = None;cuser_ID = None;cuser_name = None;cuser_office = None;cuser_office_name = None
                state = None;cuser_office_name = None;cuser_name = None;ticketServeType = None;handler_ID = None;customerPhone = None
                inOutTicket = None;orderSlot = None;user = None;handler_ID = None;TaskToDealWith = None
                ##################################################
                ticketServeCd = dict_WorkOrder["ticketServeCd"]  # 取出工单编号
                title = dict_WorkOrder["title"]  # 取出工单标题
                state = dict_WorkOrder["state"]  # 取出工单状态
                if "prbTp" in dict_WorkOrder:  # 判断有没有故障类型信息
                    prbTp = dict_WorkOrder["prbTp"]  # 取出故障类型信息
                    prbTp_ID = prbTp["id"]  # 取出故障类型ID
                    prbTp_Nm = prbTp["prbTpNm"]  # 取出故障类型名称
                if "cuser" in dict_WorkOrder:  # 判断有没有报修人信息
                    cuser = dict_WorkOrder["cuser"]  # 取出报修人信息
                    cuser_ID = cuser["id"]  # 取出报修人ID
                    cuser_name = cuser["name"]  # 取出报修人名称
                    if "office" in cuser:  # 判断有没有报修人单位信息
                        cuser_office = cuser["office"]  # 取出报修人单位信息
                        cuser_office_name = cuser_office["name"]  # 取出报修人单位名称
                workOrder_ID = dict_WorkOrder["id"]  # 获取工单ID
                if "createBy" in dict_WorkOrder:  # 判断有没有创建人
                    createBy = dict_WorkOrder["createBy"]  # 取出创建人信息
                    createBy_ID = createBy["id"]  # 取出创建人ID
                create_Date = dict_WorkOrder["createDate"]  # 工单创建日期
                update_Date = dict_WorkOrder["updateDate"]  # 取出工单更新时间
                inOutTicket = dict_WorkOrder["inOutTicket"]  # 取出工单范围
                if "ticketServeType" in dict_WorkOrder:
                    ticketServeType = dict_WorkOrder["ticketServeType"]  # 取出服务类型
                if "stateHang" in dict_WorkOrder:
                    stateHang = dict_WorkOrder["stateHang"]  # 取出挂起状态字段
                """增加任务办理按钮"""
                list_TaskToDealWith = []
                TaskToDealWith = dict_WorkOrder["operationBtn"]
                if "1" in TaskToDealWith:
                    TaskToDealWith.remove("1")  # 去掉联系人
                if roleName == "运维工程师" or roleName == "运维经理" or roleName == "服务台" or roleName == "运维总监":
                    if "18" in TaskToDealWith:
                        TaskToDealWith.remove("18")  # 去掉投诉按钮
                if TaskToDealWith:  # 编译任务办理按钮
                    for i in TaskToDealWith:
                        ToDealWith = None
                        ToDealWith = ProfileDataProcessing("TaskToDealWith", i).config_File()
                        list_TaskToDealWith.append(ToDealWith)
                if list_TaskToDealWith:
                    if list_TaskToDealWith == ['催单', '投诉', '进度']:
                        list_TaskToDealWith = ['进度', '投诉', '催单']
                    elif list_TaskToDealWith == ['评论', '进度']:
                        list_TaskToDealWith = ['进度', '评论']
                    elif list_TaskToDealWith == ['评论', '催单', '投诉', '进度']:
                        list_TaskToDealWith = ['进度', '投诉', '评论', '催单']
                    elif list_TaskToDealWith == ['撤销', '进度', '内部处理', '外协处理']:
                        list_TaskToDealWith = ['进度', '撤销', '内部处理', '外协处理']
                    elif list_TaskToDealWith == ['催单', '撤销', '进度']:
                        list_TaskToDealWith = ['进度', '撤销', '催单']
                    elif list_TaskToDealWith == ['投诉', '进度']:
                        list_TaskToDealWith =  ['进度', '投诉']
                """生成工单"""
                if selected_module!="服务端-事件-全部工单":
                        dict_compiled_complain = {"工单编号": ticketServeCd, "工单标题": title, "工单状态": state, "故障类型ID": prbTp_ID,"故障类型名称": prbTp_Nm,"报修人ID": cuser_ID,
                                          "报修人名称": cuser_name, "报修人单位名称": cuser_office_name,"工单ID": workOrder_ID,"工单创建日期": create_Date,
                                          "工单更新日期": update_Date, "工单范围": inOutTicket,"服务类型": ticketServeType,
                                          "挂起状态": stateHang,"任务办理": list_TaskToDealWith}
                else:
                        dict_compiled_complain = {"工单编号": ticketServeCd, "工单标题": title, "工单状态": state, "故障类型ID": prbTp_ID,
                                          "故障类型名称": prbTp_Nm, "报修人ID": cuser_ID,
                                          "报修人名称": cuser_name, "报修人单位名称": cuser_office_name, "工单ID": workOrder_ID,
                                          "工单创建人ID": createBy_ID, "工单创建日期": create_Date,
                                          "工单更新日期": update_Date, "工单范围": inOutTicket, "工单描述": description,
                                          "预约时间段": orderSlot, "服务类型": ticketServeType,
                                          "挂起状态": stateHang, "任务办理": list_TaskToDealWith}
                """生成工单列表"""
                self.list_work.append(dict_compiled_complain)
                n = n + 1
            print("\033[1;34;40m编译完成的实际值：\033[0m\033[4;35;40m%r" % self.list_work)
        else:
            print("\033[1;34;40m*******由于实际投诉列表没有数据，所有没有编译投诉列表*******")
            self.list_work = None
        return self.list_work


    def WorkOrderProcess_allListData_offTheStocks(self, userinfo):
        """
        allListData
        客户端-报修广场-已完成；
        self.list_parameter：
        :return:
        """
        roleName = userinfo["用户权限"]
        n = 1
        # 判断接口返回的数据是否为空
        if self.list_parameter:
            for dict_WorkOrder in self.list_parameter:
                workOrder_ID = None;stateHang = None;createBy = None;createBy_ID = None;create_Date = None;updateBy = None;updateBy_ID = None
                update_Date = None;ticketServeCd = None;prbTp = None;prbTp_ID = None;prbTp_Nm = None;title = None;description = None
                cuser = None;cuser_ID = None;cuser_name = None;cuser_office = None;cuser_office_name = None;state = None;cuser_office_name = None
                cuser_name = None;ticketServeType = None;handler_ID = None;customerPhone = NoneinOutTicket = None;orderSlot = None;user = None;handler_ID = None;TaskToDealWith = None
                ##################################################
                ticketServeCd = dict_WorkOrder["ticketServeCd"]  # 取出工单编号
                title = dict_WorkOrder["title"]  # 取出工单标题
                state = dict_WorkOrder["state"]  # 取出工单状态
                if "prbTp" in dict_WorkOrder:  # 判断有没有故障类型信息
                    prbTp = dict_WorkOrder["prbTp"]  # 取出故障类型信息
                    prbTp_ID = prbTp["id"]  # 取出故障类型ID
                    prbTp_Nm = prbTp["prbTpNm"]  # 取出故障类型名称
                if "cuser" in dict_WorkOrder:  # 判断有没有报修人信息
                    cuser = dict_WorkOrder["cuser"]  # 取出报修人信息
                    cuser_ID = cuser["id"]  # 取出报修人ID
                    cuser_name = cuser["name"]  # 取出报修人名称
                    if "office" in cuser:  # 判断有没有报修人单位信息
                        cuser_office = cuser["office"]  # 取出报修人单位信息
                        cuser_office_name = cuser_office["name"]  # 取出报修人单位名称
                workOrder_ID = dict_WorkOrder["id"]  # 获取工单ID
                if "createBy" in dict_WorkOrder:  # 判断有没有创建人
                    createBy = dict_WorkOrder["createBy"]  # 取出创建人信息
                    createBy_ID = createBy["id"]  # 取出创建人ID
                create_Date = dict_WorkOrder["createDate"]  # 工单创建日期
                update_Date = dict_WorkOrder["updateDate"]  # 取出工单更新时间
                inOutTicket = dict_WorkOrder["inOutTicket"]  # 取出工单范围
                orderSlot = dict_WorkOrder["orderSlot"]  # 取出预约时间段
                if "ticketServeType" in dict_WorkOrder:
                    ticketServeType = dict_WorkOrder["ticketServeType"]  # 取出服务类型
                if "stateHang" in dict_WorkOrder:
                    stateHang = dict_WorkOrder["stateHang"]  # 取出挂起状态字段
                """增加任务办理按钮"""
                list_TaskToDealWith = []
                TaskToDealWith = dict_WorkOrder["operationBtn"]
                if "1" in TaskToDealWith:
                    TaskToDealWith.remove("1")  # 去掉联系人
                if roleName == "运维工程师" or roleName == "运维经理" or roleName == "服务台" or roleName == "运维总监":
                    if "18" in TaskToDealWith:
                        TaskToDealWith.remove("18")  # 去掉投诉按钮
                if TaskToDealWith:  # 编译任务办理按钮
                    for i in TaskToDealWith:
                        ToDealWith = None
                        ToDealWith = ProfileDataProcessing("TaskToDealWith", i).config_File()
                        list_TaskToDealWith.append(ToDealWith)
                if list_TaskToDealWith:
                    if list_TaskToDealWith == ['催单', '投诉', '进度']:
                        list_TaskToDealWith = ['进度', '投诉', '催单']
                    elif list_TaskToDealWith == ['评论', '进度']:
                        list_TaskToDealWith = ['进度', '评论']
                    elif list_TaskToDealWith == ['评论', '催单', '投诉', '进度']:
                        list_TaskToDealWith = ['进度', '投诉', '评论', '催单']
                    elif list_TaskToDealWith == ['撤销', '进度', '内部处理', '外协处理']:
                        list_TaskToDealWith = ['进度', '撤销', '内部处理', '外协处理']
                    elif list_TaskToDealWith == ['催单', '撤销', '进度']:
                        list_TaskToDealWith = ['进度', '撤销', '催单']
                """生成工单"""
                dict_compiled_complain = {"工单编号": ticketServeCd, "工单标题": title, "工单状态": state, "故障类型ID": prbTp_ID,
                                          "故障类型名称": prbTp_Nm, "报修人ID": cuser_ID,
                                          "报修人名称": cuser_name, "报修人单位名称": cuser_office_name, "工单ID": workOrder_ID,
                                          "工单创建人ID": createBy_ID, "工单创建日期": create_Date,
                                          "工单更新日期": update_Date, "工单范围": inOutTicket, "工单描述": description,
                                          "预约时间段": orderSlot, "服务类型": ticketServeType,
                                          "挂起状态": stateHang, "任务办理": list_TaskToDealWith}
                """生成工单列表"""
                self.list_work.append(dict_compiled_complain)
                n = n + 1
            print("\033[1;34;40m编译完成的实际值：\033[0m\033[4;35;40m%r" % self.list_work)
        else:
            print("\033[1;34;40m*******由于实际投诉列表没有数据，所有没有编译投诉列表*******")
            self.list_work = None
        return self.list_work

    def WorkOrderProcess_ExternalRepairListData(self,userinfo):
        """
        报修广场--外协--数据查询；ExternalRepairListData
        self.list_parameter：
        :return:
        """
        roleName = userinfo["用户权限"]
        n = 1
        # 判断接口返回的数据是否为空
        if self.list_parameter:
            for dict_WorkOrder in self.list_parameter:
                workOrder_ID = None;stateHang=None;createBy = None;createBy_ID = None;create_Date = None;updateBy = None;updateBy_ID = Noneupdate_Date = NoneticketServeCd = None
                prbTp = None;prbTp_ID = None;prbTp_Nm = None;title = None;description = None;cuser = None;cuser_ID = None;cuser_name = None;cuser_office = None;cuser_office_name = None
                state = None;cuser_office_name = None;cuser_name = None;ticketServeType = None;handler_ID = None;customerPhone = None
                inOutTicket = None;orderSlot = None;user = None;handler_ID = None;TaskToDealWith = None
                ##################################################
                ticketServeCd = dict_WorkOrder["ticketServeCd"]  # 取出工单编号
                title = dict_WorkOrder["title"]  # 取出工单标题
                state = dict_WorkOrder["state"]  # 取出工单状态
                if "prbTp" in dict_WorkOrder:  # 判断有没有故障类型信息
                    prbTp = dict_WorkOrder["prbTp"]  # 取出故障类型信息
                    prbTp_ID = prbTp["id"]  # 取出故障类型ID
                    prbTp_Nm = prbTp["prbTpNm"]  # 取出故障类型名称
                if "cuser" in dict_WorkOrder:  # 判断有没有报修人信息
                    cuser = dict_WorkOrder["cuser"]  # 取出报修人信息
                    cuser_ID = cuser["id"]  # 取出报修人ID
                    cuser_name = cuser["name"]  # 取出报修人名称
                    if "office" in cuser:  # 判断有没有报修人单位信息
                        cuser_office = cuser["office"]  # 取出报修人单位信息
                        cuser_office_name = cuser_office["name"]  # 取出报修人单位名称
                workOrder_ID = dict_WorkOrder["id"]  # 获取工单ID
                if "createBy" in dict_WorkOrder:  # 判断有没有创建人
                    createBy = dict_WorkOrder["createBy"]  # 取出创建人信息
                    createBy_ID = createBy["id"]  # 取出创建人ID
                create_Date = dict_WorkOrder["createDate"]  # 工单创建日期
                update_Date = dict_WorkOrder["updateDate"]  # 取出工单更新时间
                inOutTicket = dict_WorkOrder["inOutTicket"]  # 取出工单范围
                description = dict_WorkOrder["description"]  # 取出报修描述
                orderSlot = dict_WorkOrder["orderSlot"]  # 取出预约时间段
                if "ticketServeType" in dict_WorkOrder:
                    ticketServeType = dict_WorkOrder["ticketServeType"]  # 取出服务类型
                if "stateHang" in dict_WorkOrder:
                    stateHang = dict_WorkOrder["stateHang"]  # 取出挂起状态字段
                """增加任务办理按钮"""
                list_TaskToDealWith = []
                TaskToDealWith = dict_WorkOrder["operationBtn"]
                if "1" in TaskToDealWith:
                    TaskToDealWith.remove("1")  # 去掉联系人
                if roleName == "运维工程师" or roleName == "运维经理" or roleName == "服务台" or roleName == "运维总监":
                    if "18" in TaskToDealWith:
                        TaskToDealWith.remove("18")  # 去掉投诉按钮
                if TaskToDealWith:  # 编译任务办理按钮
                    for i in TaskToDealWith:
                        ToDealWith = None
                        ToDealWith = ProfileDataProcessing("TaskToDealWith", i).config_File()
                        list_TaskToDealWith.append(ToDealWith)
                if list_TaskToDealWith:
                    if list_TaskToDealWith == ['催单', '投诉', '进度']:
                        list_TaskToDealWith = ['进度', '投诉', '催单']
                    elif list_TaskToDealWith == ['评论', '进度']:
                        list_TaskToDealWith = ['进度', '评论']
                    elif list_TaskToDealWith == ['评论', '催单', '投诉', '进度']:
                        list_TaskToDealWith = ['进度', '投诉', '评论', '催单']
                    elif list_TaskToDealWith == ['撤销', '进度', '内部处理', '外协处理']:
                        list_TaskToDealWith = ['进度', '撤销', '内部处理', '外协处理']
                    elif list_TaskToDealWith == ['催单', '撤销', '进度']:
                        list_TaskToDealWith = ['进度', '撤销', '催单']
                """生成工单"""
                dict_compiled_complain = {"工单编号": ticketServeCd, "工单标题": title, "工单状态": state, "故障类型ID": prbTp_ID,"故障类型名称": prbTp_Nm,"报修人ID": cuser_ID,
                                          "报修人名称": cuser_name, "报修人单位名称": cuser_office_name,"工单ID": workOrder_ID, "工单创建人ID": createBy_ID,"工单创建日期": create_Date,
                                          "工单更新日期": update_Date, "工单范围": inOutTicket,"工单描述": description, "预约时间段": orderSlot,"服务类型": ticketServeType,
                                          "挂起状态": stateHang,"任务办理": list_TaskToDealWith}
                """生成工单列表"""
                self.list_work.append(dict_compiled_complain)
                n = n + 1
            print("\033[1;34;40m编译完成的实际值：\033[0m\033[4;35;40m%r" % self.list_work)
        else:
            print("\033[1;34;40m*******由于实际投诉列表没有数据，所有没有编译投诉列表*******")
            self.list_work = None
        return self.list_work


    def WorkOrderProcess_MyRepairListData(self,userinfo):
        """
        报修广场--我的--数据查询；ExternalRepairListData
        self.list_parameter：
        :return:
        """
        roleName = userinfo["用户权限"]
        n = 1
        # 判断接口返回的数据是否为空
        if self.list_parameter:
            for dict_WorkOrder in self.list_parameter:
                workOrder_ID = None;stateHang=None;createBy = None;createBy_ID = None;create_Date = None;updateBy = None;updateBy_ID = Noneupdate_Date = NoneticketServeCd = None
                prbTp = None;prbTp_ID = None;prbTp_Nm = None;title = None;description = None;cuser = None;cuser_ID = None;cuser_name = None;cuser_office = None;cuser_office_name = None
                state = None;cuser_office_name = None;cuser_name = None;ticketServeType = None;handler_ID = None;customerPhone = None
                inOutTicket = None;orderSlot = None;user = None;handler_ID = None;TaskToDealWith = None
                ##################################################
                ticketServeCd = dict_WorkOrder["ticketServeCd"]  # 取出工单编号
                title = dict_WorkOrder["title"]  # 取出工单标题
                state = dict_WorkOrder["state"]  # 取出工单状态
                if "prbTp" in dict_WorkOrder:  # 判断有没有故障类型信息
                    prbTp = dict_WorkOrder["prbTp"]  # 取出故障类型信息
                    prbTp_ID = prbTp["id"]  # 取出故障类型ID
                    prbTp_Nm = prbTp["prbTpNm"]  # 取出故障类型名称
                if "cuser" in dict_WorkOrder:  # 判断有没有报修人信息
                    cuser = dict_WorkOrder["cuser"]  # 取出报修人信息
                    cuser_ID = cuser["id"]  # 取出报修人ID
                    cuser_name = cuser["name"]  # 取出报修人名称
                    if "office" in cuser:  # 判断有没有报修人单位信息
                        cuser_office = cuser["office"]  # 取出报修人单位信息
                        cuser_office_name = cuser_office["name"]  # 取出报修人单位名称
                workOrder_ID = dict_WorkOrder["id"]  # 获取工单ID
                if "createBy" in dict_WorkOrder:  # 判断有没有创建人
                    createBy = dict_WorkOrder["createBy"]  # 取出创建人信息
                    createBy_ID = createBy["id"]  # 取出创建人ID
                create_Date = dict_WorkOrder["createDate"]  # 工单创建日期
                update_Date = dict_WorkOrder["updateDate"]  # 取出工单更新时间
                inOutTicket = dict_WorkOrder["inOutTicket"]  # 取出工单范围
                description = dict_WorkOrder["description"]  # 取出报修描述
                orderSlot = dict_WorkOrder["orderSlot"]  # 取出预约时间段
                if "ticketServeType" in dict_WorkOrder:
                    ticketServeType = dict_WorkOrder["ticketServeType"]  # 取出服务类型
                if "stateHang" in dict_WorkOrder:
                    stateHang = dict_WorkOrder["stateHang"]  # 取出挂起状态字段
                """增加任务办理按钮"""
                list_TaskToDealWith = []
                TaskToDealWith = dict_WorkOrder["operationBtn"]
                if "1" in TaskToDealWith:
                    TaskToDealWith.remove("1")  # 去掉联系人
                if roleName == "运维工程师" or roleName == "运维经理" or roleName == "服务台" or roleName == "运维总监":
                    if "18" in TaskToDealWith:
                        TaskToDealWith.remove("18")  # 去掉投诉按钮
                if TaskToDealWith:  # 编译任务办理按钮
                    for i in TaskToDealWith:
                        ToDealWith = None
                        ToDealWith = ProfileDataProcessing("TaskToDealWith", i).config_File()
                        list_TaskToDealWith.append(ToDealWith)
                if list_TaskToDealWith:
                    if list_TaskToDealWith == ['催单', '投诉', '进度']:
                        list_TaskToDealWith = ['进度', '投诉', '催单']
                    elif list_TaskToDealWith == ['评论', '进度']:
                        list_TaskToDealWith = ['进度', '评论']
                    elif list_TaskToDealWith == ['评论', '催单', '投诉', '进度']:
                        list_TaskToDealWith = ['进度', '投诉', '评论', '催单']
                    elif list_TaskToDealWith == ['撤销', '进度', '内部处理', '外协处理']:
                        list_TaskToDealWith = ['进度', '撤销', '内部处理', '外协处理']
                    elif list_TaskToDealWith == ['催单', '撤销', '进度']:
                        list_TaskToDealWith = ['进度', '撤销', '催单']
                """生成工单"""
                dict_compiled_complain = {"工单编号": ticketServeCd, "工单标题": title, "工单状态": state, "故障类型ID": prbTp_ID,"故障类型名称": prbTp_Nm,"报修人ID": cuser_ID,
                                          "报修人名称": cuser_name, "报修人单位名称": cuser_office_name,"工单ID": workOrder_ID, "工单创建人ID": createBy_ID,"工单创建日期": create_Date,
                                          "工单更新日期": update_Date, "工单范围": inOutTicket,"工单描述": description, "预约时间段": orderSlot,"服务类型": ticketServeType,
                                          "挂起状态": stateHang,"任务办理": list_TaskToDealWith}
                """生成工单列表"""
                self.list_work.append(dict_compiled_complain)
                n = n + 1
            print("\033[1;34;40m编译完成的实际值：\033[0m\033[4;35;40m%r" % self.list_work)
        else:
            print("\033[1;34;40m*******由于实际投诉列表没有数据，所有没有编译投诉列表*******")
            self.list_work = None
        return self.list_work


    def WorkOrderProcess_InsideRepairListData(self, userinfo):
        """
        报修广场--内部--数据查询；InsideRepairListData
        self.list_parameter：
        :return:
        """
        roleName = userinfo["用户权限"]
        n = 1
        # 判断接口返回的数据是否为空
        if self.list_parameter:
            for dict_WorkOrder in self.list_parameter:
                workOrder_ID = None;createBy = None;createBy_ID = None;create_Date = None;updateBy = None;updateBy_ID = Noneupdate_Date = None
                ticketServeCd = None;prbTp = None;prbTp_ID = None;prbTp_Nm = None;title = None;description = None
                cuser = None;cuser_ID = None;cuser_name = None;cuser_office = None;cuser_office_name = None;state = None
                cuser_office_name = None;state = None;cuser_name = None;ticketServeType = None;handler_ID = None;customerPhone = None
                inOutTicket = None;orderSlot = None;user = None;handler_ID = None;TaskToDealWith = None
                ##################################################
                ticketServeCd = dict_WorkOrder["ticketServeCd"]  # 取出工单编号
                title = dict_WorkOrder["title"]  # 取出工单标题
                state = dict_WorkOrder["state"]  # 取出工单状态
                if "prbTp" in dict_WorkOrder:  # 判断有没有故障类型信息
                    prbTp = dict_WorkOrder["prbTp"]  # 取出故障类型信息
                    prbTp_ID = prbTp["id"]  # 取出故障类型ID
                    prbTp_Nm = prbTp["prbTpNm"]  # 取出故障类型名称
                if "cuser" in dict_WorkOrder:  # 判断有没有报修人信息
                    cuser = dict_WorkOrder["cuser"]  # 取出报修人信息
                    cuser_ID = cuser["id"]  # 取出报修人ID
                    cuser_name = cuser["name"] # 取出报修人名称
                    if "office" in cuser:  # 判断有没有报修人单位信息
                        cuser_office = cuser["office"]  # 取出报修人单位信息
                        cuser_office_name = cuser_office["name"]  # 取出报修人单位名称
                workOrder_ID = dict_WorkOrder["id"]  # 获取工单ID
                if "createBy" in dict_WorkOrder:  # 判断有没有创建人
                    createBy = dict_WorkOrder["createBy"]  # 取出创建人信息
                    createBy_ID = createBy["id"]  # 取出创建人ID
                create_Date = dict_WorkOrder["createDate"] # 工单创建日期
                update_Date = dict_WorkOrder["updateDate"]  # 取出工单更新时间
                inOutTicket = dict_WorkOrder["inOutTicket"]  # 取出工单范围
                description = dict_WorkOrder["description"]  # 取出报修描述
                orderSlot = dict_WorkOrder["orderSlot"]  # 取出预约时间段
                if "ticketServeType" in dict_WorkOrder:
                    ticketServeType = dict_WorkOrder["ticketServeType"]  # 取出服务类型
                """增加任务办理按钮"""
                list_TaskToDealWith = []
                TaskToDealWith = dict_WorkOrder["operationBtn"]
                if "1" in TaskToDealWith:
                    TaskToDealWith.remove("1")  # 去掉联系人
                if roleName == "运维工程师" or roleName == "运维经理" or roleName == "服务台" or roleName == "运维总监":
                    if "18" in TaskToDealWith:
                        TaskToDealWith.remove("18")  # 去掉投诉按钮
                if TaskToDealWith:  # 编译任务办理按钮
                    for i in TaskToDealWith:
                        ToDealWith = None
                        ToDealWith = ProfileDataProcessing("TaskToDealWith", i).config_File()
                        list_TaskToDealWith.append(ToDealWith)
                if list_TaskToDealWith:
                    if list_TaskToDealWith == ['催单', '投诉', '进度']:
                        list_TaskToDealWith = ['进度', '投诉', '催单']
                    elif list_TaskToDealWith == ['评论', '进度']:
                        list_TaskToDealWith = ['进度', '评论']
                    elif list_TaskToDealWith == ['评论', '催单', '投诉', '进度']:
                        list_TaskToDealWith = ['进度', '投诉', '评论', '催单']
                    elif list_TaskToDealWith == ['撤销', '进度', '内部处理', '外协处理']:
                        list_TaskToDealWith = ['进度', '撤销', '内部处理', '外协处理']
                    elif list_TaskToDealWith == ['催单', '撤销', '进度']:
                        list_TaskToDealWith = ['进度', '撤销', '催单']
                """生成工单"""
                dict_compiled_complain = {"工单编号": ticketServeCd, "工单标题": title, "工单状态": state, "故障类型ID": prbTp_ID,"故障类型名称": prbTp_Nm,
                                          "报修人ID": cuser_ID, "报修人名称": cuser_name,"报修人单位名称": cuser_office_name,"工单ID": workOrder_ID,"工单创建人ID":createBy_ID,
                                          "工单创建日期": create_Date, "工单更新日期": update_Date,"工单范围": inOutTicket,"工单描述":description,"预约时间段":orderSlot,
                                          "服务类型":ticketServeType,"任务办理":list_TaskToDealWith}
                """生成工单列表"""
                self.list_work.append(dict_compiled_complain)
                n = n + 1
            print("\033[1;34;40m编译完成的实际值：\033[0m\033[4;35;40m%r" % self.list_work)
        else:
            print("\033[1;34;40m*******由于实际投诉列表没有数据，所有没有编译投诉列表*******")
            self.list_work = None
        return self.list_work

class equipmentSchedule:
    """资产设备模块接口编译"""


    def __init__(self, JSESSIONID, list_parameter ):
        self.JSESSIONID = JSESSIONID
        self.list_parameter = list_parameter
        self.list_work = []



    def  compile_equipmentSchedule(self):
        """
        编译设备清单
        :param self:
        dict_deviceList:
        :return:dict_EquipmentField:设备清单编译过的数据
        """
        compile_deviceList =[]
        # 接口返回的数据不为空的情况下编译
        if self.list_parameter:
            #############################################################################################################
            for dict_deviceList in self.list_parameter:
                # 设备名称
                equipName           =  dict_deviceList["equipName"]
                # 跟新时间
                updateDate          =  dict_deviceList["updateDate"]
                # 创建时间
                createDate       =  dict_deviceList["createDate"]
                # 批次
                batchNo             =  dict_deviceList["batchNo"]
                # 设备品牌
                equipBrand          =  dict_deviceList["equipBrand"]
                # 设备状态
                equipState          =  dict_deviceList["equipState"]
                # 位置信息名称
                structure           =  dict_deviceList["structure"]
                structure_id      =  structure["id"]
                # 设备类型ID
                equipType         =  dict_deviceList["equipType"]
                equipType_id        =  equipType["id"]
                # 设备ID
                facility_id         =  dict_deviceList["id"]
                # 设备编号
                qrcodeName          =  dict_deviceList["qrcodeName"]
                dict_EquipmentField={"设备名称":equipName,"跟新时间":updateDate,"创建时间":createDate,"批次":batchNo,
                                     "设备品牌":equipBrand,"设备状态":equipState,"位置信息":structure_id,
                                     "设备类型ID":equipType_id,"设备ID":facility_id,"设备编号":qrcodeName}
                compile_deviceList.append(dict_EquipmentField)
            print("\033[1;34;40m编译出的实际值列表：%r" % compile_deviceList)
        else:
            print("\033[1;34;40m由于实际资产列表没有数据，所有没有编译资产列表")
            compile_deviceList=["为空"]
        return compile_deviceList


class StatisticsOfRepairQuantity:
    """报修统计模块"""

    def __init__(self, JSESSIONID, list_parameter ):
        self.JSESSIONID = JSESSIONID
        self.list_parameter = list_parameter
        self.list_work = []


    def ReportStatistics(self,module):
        """
        编译报修统计接口数据
        :return:
        """
        '''
        #{"success":true,"errorCode":"-1","msg":"查询成功","body":{"numCountData":[{"cuser":{"office":{"id":"e155a7d8e34f4e339d5207ab33e2add4","name":"生物城第一高级中学分校","hasChildren":false,"type":"2","parentId":"0"},"loginFlag":"1","roleNames":"","admin":false},"officeCountNum":"226","handleTaskFlag":false,"histroryFlag":false},{"cuser":{"office":{"id":"4e9d5a781177449bb0b74dbc6d75a9fe","name":"生物城第一高级中学分校附属幼儿园","hasChildren":false,"type":"2","parentId":"0"},"loginFlag":"1","roleNames":"","admin":false},"officeCountNum":"0","handleTaskFlag":false,"histroryFlag":false}]}}'''
        dict_WorkOrderNumber={}
        if self.list_parameter:
            log.log("开始编译设备清单列表数据", __file__, sys._getframe().f_lineno)
            for dict_deviceList in self.list_parameter:
                if module == "报修数量":
                    office=dict_deviceList["cuser"]
                    office =office['office']
                    # 单位ID
                    officeId=office["id"]
                    # 单位名称
                    officeName = office["name"]
                    # 报修数量
                    officeCountNum = dict_deviceList["officeCountNum"]
                    dict_WorkOrderNumber={"单位ID":officeId,"单位名称":officeName,"工单数":officeCountNum}
                    self.list_work.append(dict_WorkOrderNumber)
                if module == "故障数量":
                    prbTp = dict_deviceList["prbTp"]
                    faultType_id = prbTp['id']
                    faultType_Name = prbTp['prbTpNm']
                    faultType_Number = dict_deviceList["prbTpTypeNum"]
                    dict_faultType={"故障ID":faultType_id,"故障名称":faultType_Name,"工单数":faultType_Number}
                    self.list_work.append(dict_faultType)
            print("\033[1;34;40m编译出的实际值列表：%r" % self.list_work)
        else:
            print("\033[1;34;40m由于报修数量没有数据，所有没有编译报修统计列表")
            self.list_work = ["为空"]
        return self.list_work


class ListOfComplaints:
    """投诉清单模块"""

    def __init__(self, list_parameter):
        self.list_parameter = list_parameter
        self.list_work = []


    def compile_TheComplaintpage(self):
            """
            编译小程序投诉清单页面数据
            self.list_parameter：接口返回的数据清单
            :return:
            """
            n = 1
            # 判断接口返回的数据是否为空
            if self.list_parameter:
                for dict_AListOfComplaints in self.list_parameter:
                    operation = None;complainant_id = None
                    Content_id = dict_AListOfComplaints["id"]  # 投诉单ID
                    Content_title = dict_AListOfComplaints["title"]  # 投诉标题
                    breakContent =dict_AListOfComplaints["breakContent"]  # 投诉内容
                    # 投诉用户名称
                    complaintUser_message = dict_AListOfComplaints["complaintUser"]
                    complaintUser_name = complaintUser_message["name"]
                    # 投诉用户id
                    complaintUser_id = complaintUser_message["id"]
                    # 投诉单状态
                    Content_state = dict_AListOfComplaints["state"]
                    # 投诉信息的创建时间
                    createDate = dict_AListOfComplaints["createDate"]
                    # 投诉信息的更新时间
                    updateDate = dict_AListOfComplaints["updateDate"]
                    #  任务办理按钮
                    # 判断有没有任务办理按钮
                    if "operation" in dict_AListOfComplaints:
                        operation = dict_AListOfComplaints["operation"]
                    # 判断有没有被投诉人
                    if "complainant" in dict_AListOfComplaints:
                        #  取出被投诉人用户信息
                        By_complainant = dict_AListOfComplaints["complainant"]
                        complainant_id = By_complainant["id"]
                    dict_compiled_complain = {"投诉单ID":Content_id,"投诉标题": Content_title, "投诉内容": breakContent, "投诉用户名称": complaintUser_name,
                                              "投诉用户id": complaintUser_id, "投诉单状态": Content_state,
                                              "投诉信息的创建时间": createDate,
                                              "投诉信息的更新时间": updateDate,"被投诉人ID":complainant_id,"任务办理":operation}
                    self.list_work.append(dict_compiled_complain)
                    n = n+1
                print("\033[1;34;40m编译完成的实际值：\033[0m\033[4;35;40m%r"%self.list_work)
            else:
                print("\033[1;34;40m*******由于实际投诉列表没有数据，所有没有编译投诉列表*******")
                self.list_work = None
            return self.list_work


class OtherInterfaces_compile:
    """其他接口编译"""

    def __init__(self,  list_parameter):
        self.list_parameter = list_parameter
        self.list_work = []


    def findGroupList_compile(self):
        """
        查询所有群组(服务台改派用)接口返回值编译
        :return:
        """

        if self.list_parameter:
            for parameter in self.list_parameter:
                group_id=parameter["id"]
                group_name =parameter["name"]
                group_message={"群组ID":group_id,"群组名称":group_name }
                self.list_work.append(group_message)
            print("\033[1;34;40m编译完成查询所有群组(服务台改派用)接口的实际值：\033[0m\033[4;35;40m%r" % self.list_work)
        else:
            print("\033[1;34;40m*******由于查询所有群组(服务台改派用)接口没有返回数据，所有没有编译*******")
            self.list_work = None
        return self.list_work


    def findUserListByGroup_compile(self):
        """
        工单操作改派选人
        :return:
        """

        if self.list_parameter:
            for parameter in self.list_parameter:
                user_id=parameter["id"]
                user_name =parameter["name"]
                user_message={"用户ID":user_id,"用户名称":user_name }
                self.list_work.append(user_message)
            print("\033[1;34;40m编译完成工单操作改派选人接口的实际值：\033[0m\033[4;35;40m%r" % self.list_work)
        else:
            print("\033[1;34;40m*******由于查询工单操作改派选人接口没有返回数据，所有没有编译*******")
            self.list_work = None
        return self.list_work



    def WorkOrderProcess_Post(self,FilterParameters,req_text):
        """
        获取post请求部分参数
        :return:
        """
        judge=False
        expect_WorkOrderID = FilterParameters["工单ID"]
        # 判断接口返回的数据是否为空
        if self.list_parameter:
            for dict_WorkOrder in self.list_parameter:
                # 取出工单ID
                actual_WorkOrderID=dict_WorkOrder["id"]
                # 只取出需要操作的工单post参数
                if expect_WorkOrderID== actual_WorkOrderID:
                    if "task" in dict_WorkOrder:
                        task=dict_WorkOrder["task"]
                        FilterParameters["任务id"] = task["task.id"]
                        FilterParameters["任务名称"]=task["task.name"]
                        FilterParameters["任务定义Key"] = task["task.taskDefinitionKey"]
                        FilterParameters["流程实例id"] = task["task.processInstanceId"]
                        FilterParameters["流程定义id"] = task["task.processDefinitionId"]
                        FilterParameters["任务状态"]=task["status"]
                        judge = True
                    else:
                        print("该页面没有返回任务流参数",__file__, sys._getframe().f_lineno)
                        print("返回的工单列表：", req_text)
                        os._exit(0)
            if judge == False:
                print("该页面有工单，但是没有需要操作的工单",__file__, sys._getframe().f_lineno)
                print("返回的工单列表：",req_text)
                os._exit(0)
        else:
            print("该页面没有工单",__file__, sys._getframe().f_lineno)
            print("返回的工单列表：", req_text)
            os._exit(0)
        return FilterParameters
