#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 预期值得生成


from PrivateMethods import useCase_check_deviceList,useCase_verify_ReportStatistics,ComplaintListPage
from Task_handling_button import Task_handling_button

from utils.commonality.database_SqlRealize import AssetManagementDataQuery
from commonality.database_SqlRealize import dataProcessing
import os
from utils.privately_owned.timeDisposal import TimeFormat
from utils.privately_owned.authority_management import authorityManagement
from utils.privately_owned.DataType_ParameterProcessing import DataType_processing



###############预期值的生成################

class GenerateExpectedValues:
    """生成预期值"""

    def __init__(self,dicti_parameterPacket, actualWorkOrder=None):
        self.dicti_parameterPacket=dicti_parameterPacket
        self.actualWorkOrder = actualWorkOrder
        self.expectedValue=None




    def AssetsOfEquipmentList__expected(self,structureID):
        """
        资产设备列表页面获取所在位置和单位名称
        :param structureID:单位ID
        :return:
        """
        loginName=self.dicti_parameterPacket["登录名"];roleName=self.dicti_parameterPacket["用户权限"]
        # 初始化变量
        list_officeID = [];list_locationID=[];list_dicti_locationID =[];structureName=None
        # 判断是否是内部用户
        if roleName == "运维工程师" or roleName == "运维经理"  or roleName == "运维总监" or roleName == "服务台":
            roleName ="内部用户"
        register_userinfo = {"登录名": loginName, "用户权限": roleName}
        # 用户权限
        """单位ID编译成单位名称"""
        if structureID != None:
            structureName = useCase_check_deviceList(structureID).check_deviceList_officeID_officeName()
            list_officeID.append(structureID)
        # 如果单位筛选条件为空，就根据用户权限查询出单位id
        elif structureID == None:
            # 区域管理员返回所管辖的单位ID，用户管理员返回所在单位的ID，内部用户返回所有的外部单位
            result, list_officeID = authorityManagement(register_userinfo).AreaManager_authorityManagement("", "officeID")
        """预期值,根据单位获取单位下的关联的所有位置；该单位下面没有位置，就使用单位ID，如果单位下面有位置就位置加上单位"""
        for officeID in list_officeID:
            data_structureID = {}
            # 使用SQL语句通过单位ID查询出来位置ID
            list_locationID1 = AssetManagementDataQuery(officeID, "OfficeID_locationID").independentSQL()
            # 把单位放到位置字典里区
            data_structureID["位置ID"] = officeID;list_dicti_locationID.append(data_structureID)
            if list_locationID1:
                for locationID1 in list_locationID1:
                    list_dicti_locationID.append(locationID1)
        # 列表嵌套的字典转成列表
        for locationID in list_dicti_locationID:
            locatio = locationID["位置ID"]
            list_locationID.append(locatio)
        return list_locationID,structureName



    def AssetsOfEquipmentList_filtrate_actual(self,realAssets):
        """
        资产设备页面加上筛选条件后的资产数据实际值
        :return:
        """
        """批次,从实际资产列取出批号字段，生成一个实际批号列表"""
        practical_list_batchNumber = DataType_processing(realAssets).list_nest_dict_list("批次")
        # 生成实际单位位置ID列表
        practical_list_locationid = DataType_processing(realAssets).list_nest_dict_list("位置信息")
        # 实际单位位置ID获取单位名称列表
        if practical_list_locationid:
            list_office = AssetManagementDataQuery(practical_list_locationid).locationID_officeID()
        else:
            list_office = None
        """设备名称,取出实际资产数据里的设备名称，放到列表中"""
        practical_list_equipName = DataType_processing(realAssets).list_nest_dict_list("设备名称")
        return  practical_list_locationid,practical_list_batchNumber,list_office,practical_list_equipName




    def complaintsList_expected(self):
        """
        投诉清单页面获取预期值
        :return:
        """

        loginName = self.dicti_parameterPacket["登录名"];roleName = self.dicti_parameterPacket["用户权限"]
        userinfo ={"登录名":loginName,"用户权限":roleName}
        # 获取投诉清单页面初始数据（不带任务办理按钮）
        Complaint_list_data = ComplaintListPage(self.dicti_parameterPacket).Complaint_expected_initial()
        # 判断通过SQL语句查询到投诉清单数据是否为空
        if Complaint_list_data:
            # 转化日期数据类型转化成str
            list_dataKey_time = ["投诉信息的创建时间", "投诉信息的更新时间"]
            Complaint_timeStr_list_data = TimeFormat(Complaint_list_data, list_dataKey_time).listNestDict_TimeType_str()
            # 投诉清单列表增加任务办理按钮
            self.expectedValue = Task_handling_button(Complaint_timeStr_list_data, self.dicti_parameterPacket).Complaint_expected_taskmgr()
        else:
            self.expectedValue =None
        return self.expectedValue


    def verify_ReportStatistics_expect(self,module):
        """
        工单数量统计预期值
        FilterParameters:  单位ID
        self.list_expect：预期统计列表
        :param module:
        :return:
        """
        list_partNumber = [];list_expect = [];list_screening = None;Service_Table = None;incident_Table = None;list_WorkingOdd=None
        list_office= self.dicti_parameterPacket["所选单位ID"] ; begin_date=self.dicti_parameterPacket["开始日期"] ;finish_date=self.dicti_parameterPacket["结束日期"]
        roleName = self.dicti_parameterPacket["用户权限"];userid = self.dicti_parameterPacket["用户ID"]; carryOutSQL=None
        """判断单位筛选条件是否为空"""
        if list_office != None:
            """当单位筛选条件不为空的情况下，取出单位列表里的单个值"""
            # 通过sql语句查询出各个状态的工单数量
            if   module == "报修数量":
                carryOutSQL={"服务工单表":"报修数量-服务","事件工单表":"报修数量-事件"}
            elif  module == "故障数量":
                carryOutSQL = {"服务工单表": "故障类型-服务", "事件工单表": "故障类型-事件"}
        else:
            '''判断工单权限'''
            if module == "报修数量":
                if roleName == "区域管理员":
                    carryOutSQL = {"服务工单表": "报修数量-区域管理员-服务", "事件工单表": "报修数量-区域管理员-事件"}
                elif roleName == "用户管理员":
                    carryOutSQL = {"服务工单表": "报修数量-用户管理员-服务", "事件工单表": "报修数量-用户管理员-事件"}
                elif roleName == "运维经理" or roleName == "运维工程师" or roleName == "运维总监" or roleName == "服务台":
                    carryOutSQL = {"服务工单表": "报修数量-内部-服务", "事件工单表": "报修数量-内部-事件"}
            elif module == "故障数量":
                if roleName == "区域管理员":
                    carryOutSQL = {"服务工单表": "故障类型-区域管理员-服务", "事件工单表": "故障类型-区域管理员-事件"}
                elif roleName == "用户管理员":
                    carryOutSQL = {"服务工单表": "故障类型-用户管理员-服务", "事件工单表": "故障类型-用户管理员-事件"}
                elif roleName == "运维经理" or roleName == "运维工程师" or roleName == "运维总监" or roleName == "服务台":
                    carryOutSQL = {"服务工单表": "故障类型-内部-服务", "事件工单表": "故障类型-内部-事件"}
        #  在数据库中查询出区域管理里所管辖单位的各个工单状态统计数目
        self.expectedValue = useCase_verify_ReportStatistics(carryOutSQL).database_statistics_WorkOrderNumber(self.dicti_parameterPacket, module)
        """当有工单数的单位超过10个时，就取工单数前十名的单位，其余的工单数归纳到其他里去"""
        if module == "报修数量":
            import operator
            new_expectedValue=[];list_number=[];n=0;m=10;officeID=None
            list_value = [x['单位名称'] for x in self.actualWorkOrder] # 判断“其他”是否存在实际值中
            if "其他" in list_value:    # 判断“其他”是否存在实际值中
               for WorkOrder in self.actualWorkOrder:  # 取出其他里的单位ID
                    officeName=WorkOrder["单位名称"]
                    if officeName=="其他":
                        officeID=WorkOrder["单位ID"]
               if len(self.expectedValue)>m:
                  self.expectedValue.sort(key=operator.itemgetter('工单数'), reverse=True)
                  while n < len(self.expectedValue):
                      dict_str = self.expectedValue[n]
                      if n < m:
                          new_expectedValue.append(dict_str)
                      else:
                          int_number = int(dict_str["工单数"])
                          list_number.append(int_number)
                      n = n + 1
                  sum_number = sum(list_number)
                  rests = {"单位名称": "其他", "单位ID":officeID,"工单数":sum_number}
                  new_expectedValue.append(rests)
                  self.expectedValue=new_expectedValue
        return self.expectedValue


class addAndModification:


    def __init__(self,FilterParameters):
        """
        :param FilterParameters:生成预期值需要的参数
        self.ReturnExpected：返回的预期值
        """
        self.FilterParameters = FilterParameters
        self.ReturnExpected=None




    def add_complaint_database(self):
        """
        新增投诉预期值，检查数据是否增加到数据库
        :return:
        """
        complaintID=None
        # 通过SQL语句查询
        returnData,sql = dataProcessing("add_database","user_add").user_name(self.FilterParameters)
        if returnData:
            complaintID=returnData[0]["投诉单ID"]
            print("\033[5;34;40m外部用户新增投诉，在数据库检查新增成功")
        else:
            print("\033[5;30;41m投诉信息没有新增通过，程序停止运行")
            os._exit(0)
        return complaintID


    def accept_complaint_database(self):
        """
        服务台受理投诉信息后，检查数据库里的投诉是否被修改
        :return:
        """
        # 通过SQL语句查询
        returnData,sql = dataProcessing("accept_complaint_databaseQuery",None).user_name(self.FilterParameters)
        if returnData:
            print("\033[5;34;40m服务台受理投诉：在数据库检查修改成功")
        else:
            print("\033[5;34;40m服务台受理投诉：数据修改失败，程序停止运行")
            os._exit(0)





    def add_complaint_jurisdiction_Permission(self,post_Parameter):
        """
         新增投诉信息后，各个权限数据校验，所用预期数据
        :return:
        """
        """数据初始化"""
        complaint_userid1=[];complaint_byUserid1 = [];gobalBuyer=False
        roleName=post_Parameter["用户权限"]  # 获取检查用户
        complaint_title = self.FilterParameters["投诉标题"];  complaint_content = self.FilterParameters["投诉内容"]
        time1 = self.FilterParameters["创建日期"];            complaint_userid = self.FilterParameters["投诉人ID"]
        complaint_byUserid = self.FilterParameters["被投诉人ID"];  complaint_state = self.FilterParameters["投诉状态"]
        complaint_userName = self.FilterParameters["投诉用户名称"] ; complaintID=self.FilterParameters["投诉单ID"]
        userID=post_Parameter["用户ID"]
        # 把投诉用户id强行转化成列表  # 把被投诉人ID强行转化成列表
        complaint_userid1.append(complaint_userid);complaint_byUserid1.append(complaint_byUserid)
        ################################################################################################
        """判断查看权限"""
        if   roleName == "普通用户":
            # 如果投诉信息的投诉人等于登录用户，该用户就能查看到该投诉信息，并生成预期值
            if complaint_userid == userID:
                gobalBuyer = True
        elif roleName == "用户管理员" or roleName == "区域管理员":
            # 如果投诉信息的投诉人属于该用户管理员所在单位里的用户，该用户管理员就能够查看该投诉信息
            # 如果投诉信息的投诉人属于该登录区域管理所管辖单位里的用户，该区域管理员就能够查看该投诉信息
            gobalBuyer,list_unitsIDuserID = authorityManagement(post_Parameter).AreaManager_authorityManagement(complaint_userid1,"userID")
        elif roleName == "运维工程师":
            # 如果投诉信息的被投诉人是登录的运维工程师，该登录的运维工程师就能够查看到该投诉信息
            # gobalBuyer,list_unitsIDuserID = authorityManagement(post_Parameter).AreaManager_authorityManagement(complaint_byUserid1,"userID")
            if userID==complaint_byUserid:
                gobalBuyer=True
        elif roleName == "运维经理":
            gobalBuyer, list_unitsIDuserID = authorityManagement(post_Parameter).AreaManager_authorityManagement(complaint_byUserid1, "userID")
        elif roleName == "服务台" or roleName == "运维总监":
            gobalBuyer =True
        else:
            gobalBuyer = False
        ###############################################################################################################
        # 如果gobalBuyer =True登录用户就有查看投诉信息的权限
        if gobalBuyer :
            # 获取系统日期by
            expectedValue =[{"投诉单ID":complaintID,"投诉标题":complaint_title,"投诉内容":complaint_content,"投诉用户名称":complaint_userName,
                            "投诉用户id":complaint_userid,"投诉单状态":complaint_state, "投诉信息的创建时间":time1,"投诉信息的更新时间":time1,
                            "被投诉人ID": complaint_byUserid,"任务办理": None}]
            # 投诉清单列表增加任务办理按钮
            self.ReturnExpected = Task_handling_button(expectedValue, post_Parameter).Complaint_expected_taskmgr()
        else:
            self.ReturnExpected =None
        ############################################################################################################
        # # 测试用例
        # self.ReturnExpected = [{"投诉标题": "qwsdfg", "投诉内容": "qwsdfg", "投诉用户名称": username,
        #                   "投诉用户id": userid, "投诉单状态": "0", "投诉信息的创建时间": 2019, "投诉信息的更新时间": 12,
        #                   "被投诉人ID": None, "任务办理": "11"}]
        return self.ReturnExpected






class WorkOrderProcess_expectedValue:
    """工单流程预期值"""

    def __init__(self, FilterParameters):
        """
        :param FilterParameters:生成预期值需要的参数
        self.ReturnExpected：返回的预期值
        """
        self.FilterParameters = FilterParameters
        self.ReturnExpected = None


    def add_workOrder_database(self):
        """
        普通用户新建工单后数据检查数据是否增加
        :return:
        """
        WorkOrderID=None
        # 通过SQL语句查询
        returnData,sql = dataProcessing("add_WorkOrder_databaseQuery", None).user_name(self.FilterParameters)
        if returnData:
            WorkOrderID = returnData[0]["工单ID"]
            print("\033[5;34;40m普通用户-一键报修后再数据库检查工单是否增加成功")
        else:
            print("\033[5;34;40m普通用户-一键报修：在数据库检查工单是否增加失败")
            print("\033[5;34;40m普通用户-一键报修：查询SQL：",sql)
            os._exit(0)
        return WorkOrderID


    def amend_workOrder_database(self,procedure):
        """
        用户操作工单数据后检查数据是否更改
        :return:
        """
        WorkOrderID=None
        # 通过SQL语句查询
        returnData,sql = dataProcessing("alter_WorkOrder_database_DataChanges", None).user_name(self.FilterParameters)
        if returnData:
            print("\033[5;34;40m“%r”，操作后，通过SQL语句在数据库查询，查询到该修改工单，操作成功"%procedure)
        else:
            print("\033[5;34;40m“%r”，操作后，通过SQL语句在数据库查询，没有查询到该工单，操作失败" % procedure)
            print("操作失败后返回的SQL：",sql)
            os._exit(0)
        return WorkOrderID



    def clientSide_repairsPlazaMy_expected(self,CheckModule,procedure):
        """
        小程序工单流程预期值
        :return:
        """
        # 初始化变量
        ticketServeCd = None;title = None;state = None;prbTp_ID = None;cuser_ID = None;workOrder_ID = None;createBy_ID = None;cuser_name = None
        cuser_ID = None;updateBy_ID = None;update_Date = None;prbTp_Nm = None;description = None;cuser_office_name = None
        customerPhone = None;ticketServeType = None;inOutTicket = None;orderSlot = None;list_TaskToDealWith = None;handler_id = None
        ExpectationsThat=None;hangUp_roleName=None;Solution=None; self.FilterParameters["任务办理"] = None
        # 获取用户信息
        roleName = self.FilterParameters["用户权限"];ticketServeType = self.FilterParameters["工单服务类型"]; selected_module = self.FilterParameters["所属模块"]
        # 获取服务台解挂后，工单出现的模块和申请挂起的用户权限
        if  selected_module == "服务台-已挂起-解挂" or selected_module == "服务台(一号)-已挂起-改派-工程师(四组)" or selected_module == "服务台(一号)-已挂起-改派-工程师(五组)":
            # 取出工单在挂起前的状态
            front_state=self.FilterParameters["工单在挂起前的状态"]
            if front_state == "3":
                Solution = "服务台-已挂起-解挂和改派-预约中"
            elif front_state == "5":
                Solution = "服务台-已挂起-解挂和改派-处理中"
            # 取出工单在挂起前用户权限
            hangUp_roleName = self.FilterParameters["申请挂起用户权限"]
        """增加任务办理按钮"""
        self.FilterParameters,ExpectationsThat=WorkOrderProcess_expectedValue(self.FilterParameters).WorkOrderProcess_expect_TaskToDealWith(selected_module,CheckModule,Solution,hangUp_roleName,ticketServeType,roleName)
        # 取出参数值
        ticketServeCd=self.FilterParameters["工单编号"] ;           title=self.FilterParameters["工单标题"]
        state = self.FilterParameters["工单状态"];                  prbTp_ID = self.FilterParameters["故障类型ID"]
        cuser_ID = self.FilterParameters["工单报修人ID"];               workOrder_ID = self.FilterParameters["工单ID"]
        createBy_ID = self.FilterParameters["工单创建人ID"];        cuser_name = self.FilterParameters["报修人名称"]
        create_Date = self.FilterParameters["工单创建日期"];        updateBy_ID = self.FilterParameters["工单更新人ID"]
        update_Date = self.FilterParameters["工单更新日期"];        prbTp_Nm = self.FilterParameters["故障类型名称"]
        description = self.FilterParameters["工单报修描述"];        cuser_office_name = self.FilterParameters["报修人单位名称"]
        customerPhone = self.FilterParameters["报修人电话"];         list_TaskToDealWith = self.FilterParameters["任务办理"]
        inOutTicket = self.FilterParameters["工单范围"];             orderSlot = self.FilterParameters["预约时间段"]
        handler_id = self.FilterParameters["工单处理人ID"]  ;          stateHang = self.FilterParameters["挂起状态"]
        userGroupId = self.FilterParameters["工单所在群组ID"]
        if CheckModule == "客户端--报修广场--我的报修":
            self.ReturnExpected = [{"工单编号": ticketServeCd, "工单标题": title, "工单状态": state, "故障类型ID": prbTp_ID,"故障类型名称": prbTp_Nm,"报修人ID": cuser_ID,
                                      "报修人名称": cuser_name, "报修人单位名称": cuser_office_name,"工单ID": workOrder_ID, "工单创建人ID": createBy_ID,"工单创建日期": create_Date,
                                      "工单更新日期": update_Date, "工单范围": inOutTicket,"工单描述": description, "预约时间段": orderSlot,"服务类型": ticketServeType,
                                      "挂起状态": stateHang,"任务办理": list_TaskToDealWith}]
        elif CheckModule == "客户端--报修广场--内部":
            self.ReturnExpected = [{"工单编号": ticketServeCd, "工单标题": title, "工单状态": state, "故障类型ID": prbTp_ID,"故障类型名称": prbTp_Nm,
                                  "报修人ID": cuser_ID, "报修人名称": cuser_name,"报修人单位名称": cuser_office_name,"工单ID": workOrder_ID,"工单创建人ID":createBy_ID,
                                  "工单创建日期": create_Date, "工单更新日期": update_Date,"工单范围": inOutTicket,"工单描述":description,"预约时间段":orderSlot,
                                  "服务类型":ticketServeType,"任务办理":list_TaskToDealWith}]
        elif CheckModule == "客户端--报修广场--外协":
            self.ReturnExpected =[{"工单编号": ticketServeCd, "工单标题": title, "工单状态": state, "故障类型ID": prbTp_ID,"故障类型名称": prbTp_Nm,"报修人ID": cuser_ID,
                                  "报修人名称": cuser_name, "报修人单位名称": cuser_office_name,"工单ID": workOrder_ID, "工单创建人ID": createBy_ID,"工单创建日期": create_Date,
                                  "工单更新日期": update_Date, "工单范围": inOutTicket,"工单描述": description, "预约时间段": orderSlot,"服务类型": ticketServeType,
                                  "挂起状态": stateHang,"任务办理": list_TaskToDealWith}]
        elif CheckModule == "小程序--首页":
            self.ReturnExpected = [{"工单编号": ticketServeCd,"工单标题": title,"工单状态": state, "故障类型ID":prbTp_ID,
                             "报修人ID":cuser_ID,"工单ID": workOrder_ID,"报修人名称":cuser_name,"工单创建日期":create_Date ,"工单更新日期":update_Date,
                             "故障类型名称": prbTp_Nm,"工单处理人ID": handler_id,"报修人单位名称": cuser_office_name,"工单范围": inOutTicket,"挂起状态":stateHang,
                             "工单所在群组ID":userGroupId,"任务办理": list_TaskToDealWith}]
        elif CheckModule == "客户端-报修广场-已完成" or CheckModule == "客户端-报修广场-全部" or CheckModule == "小程序--紧急报修" or CheckModule == "小程序--驻场服务":
            self.ReturnExpected = [{"工单编号": ticketServeCd, "工单标题": title, "工单状态": state, "故障类型ID": prbTp_ID,"故障类型名称": prbTp_Nm,"报修人ID": cuser_ID,
                                  "报修人名称": cuser_name, "报修人单位名称": cuser_office_name,"工单ID": workOrder_ID, "工单创建人ID": createBy_ID,"工单创建日期": create_Date,
                                  "工单更新日期": update_Date, "工单范围": inOutTicket,"工单描述": description, "预约时间段": orderSlot,"服务类型": ticketServeType,
                                  "挂起状态": stateHang,"任务办理": list_TaskToDealWith}]
        return self.ReturnExpected,ExpectationsThat



    def WorkOrderProcess_expect_TaskToDealWith(self,selected_module,CheckModule,Solution,hangUp_roleName,ticketServeType,roleName):
        """
        工单流程--预期--任务办理按钮
        :return:
        """
        ExpectationsThat=None
        if selected_module == "普通用户-一键报修":
            if roleName == "普通用户" and (CheckModule == "客户端--报修广场--我的报修" or CheckModule == "小程序--首页" or CheckModule == "客户端-报修广场-全部"):
                self.FilterParameters["任务办理"] = ["进度", "撤销", "催单"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "用户管理员" and (CheckModule == "客户端--报修广场--内部" or CheckModule == "小程序--首页"):
                self.FilterParameters["任务办理"] = ["进度", "撤销", "内部处理", "外协处理"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "区域管理员" and (CheckModule == "客户端--报修广场--内部" or CheckModule == "小程序--首页" or CheckModule == "客户端-报修广场-全部"):
                self.FilterParameters["任务办理"] = ["进度", "评论"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            else:
                ExpectationsThat = "实际值里没有预期值"
        elif selected_module ==  "普通用户-内部-评论" or selected_module ==  "普通用户-外部-评论":
            if roleName == "普通用户" and (CheckModule == "客户端-报修广场-已完成"  or CheckModule == "客户端-报修广场-全部"):
                if  selected_module ==  "普通用户-内部-评论":
                    self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                elif selected_module ==  "普通用户-外部-评论":
                    self.FilterParameters["任务办理"] = ["进度","投诉"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "用户管理员" and ( CheckModule == "客户端-报修广场-已完成" or CheckModule == "客户端-报修广场-全部" ):
                self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "区域管理员" and (CheckModule == "客户端-报修广场-已完成" or CheckModule == "客户端-报修广场-全部" ):
                self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "运维工程师" and (selected_module ==  "普通用户-外部-评论" or selected_module ==  "普通用户-内部-评论") and (CheckModule == "服务端--事件--已关单"
                  or CheckModule == "小程序--首页"):
                if CheckModule == "服务端-事件-全部工单" and selected_module ==  "普通用户-外部-评论":
                    ExpectationsThat = "实际值包含预期值"
                    self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                elif CheckModule == "服务端--事件--已关单" :
                    ExpectationsThat = "实际值包含预期值"
                else:
                    ExpectationsThat = "实际值里没有预期值"
            elif roleName == "运维经理" and(selected_module ==  "普通用户-外部-评论" or selected_module ==  "普通用户-内部-评论") and (
                CheckModule == "服务端--事件--已关单"  or CheckModule == "小程序--首页" ):
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "服务台" and (selected_module ==  "普通用户-外部-评论" or selected_module ==  "普通用户-内部-评论") and (
                CheckModule == "服务端--事件--已关单"  or CheckModule == "小程序--首页" ):
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "运维总监" and (selected_module ==  "普通用户-外部-评论" or selected_module ==  "普通用户-内部-评论") and (
                CheckModule == "服务端--事件--已关单"  or CheckModule == "小程序--首页" ):
                ExpectationsThat = "实际值包含预期值"
            else:
                ExpectationsThat = "实际值里没有预期值"
        elif selected_module == "用户管理员-内部处理":
            if roleName == "普通用户" and (CheckModule == "客户端-报修广场-已完成" or CheckModule == "小程序--首页" or CheckModule == "客户端-报修广场-全部"):
                self.FilterParameters["任务办理"] = ["进度", "评价"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "用户管理员" and ( CheckModule == "客户端-报修广场-已完成" or CheckModule == "客户端-报修广场-全部" or CheckModule == "小程序--首页"):
                self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "区域管理员" and (CheckModule == "客户端-报修广场-已完成" or CheckModule == "客户端-报修广场-全部" or CheckModule == "小程序--首页"):
                self.FilterParameters["任务办理"] = ["进度", "评论"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            else:
                ExpectationsThat = "实际值里没有预期值"
        elif selected_module == "用户管理员-外协处理":
            if roleName == "普通用户" and (CheckModule == "客户端--报修广场--我的报修" or CheckModule == "小程序--首页" or CheckModule == "客户端-报修广场-全部"):
                self.FilterParameters["任务办理"] = ["进度", "投诉","催单"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "用户管理员" and (CheckModule == "客户端--报修广场--外协" or CheckModule == "客户端-报修广场-全部" or CheckModule == "小程序--首页" or
                                          (ticketServeType=="1" and CheckModule == "小程序--紧急报修") or  (ticketServeType=="2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度", "投诉","催单"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "区域管理员" and (CheckModule == "客户端--报修广场--外协" or CheckModule == "客户端-报修广场-全部" or CheckModule == "小程序--首页"  or
                                          (ticketServeType=="1" and CheckModule == "小程序--紧急报修") or  (ticketServeType=="2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度", "投诉","评论","催单"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "运维工程师" and (CheckModule == "服务端--事件--待响应"  or CheckModule == "小程序--首页" or
                                          (ticketServeType=="1" and CheckModule == "小程序--紧急报修") or  (ticketServeType=="2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "运维经理" and ( CheckModule == "服务端--事件--待响应"  or CheckModule == "小程序--首页" or
                                          (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度", "接单", "改派"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "服务台" and (CheckModule == "服务端--事件--待响应"  or CheckModule == "小程序--首页" or
                                          (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度", "撤销"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "运维总监" and (CheckModule == "服务端--事件--待响应"  or CheckModule == "小程序--首页" or
                                          (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            else:
                ExpectationsThat = "实际值里没有预期值"
        elif selected_module == "组长(四组)-待响应-改派-工程师(四组)" or selected_module == "组长（四组）-待响应-接单" or selected_module == "工程师(四组)-预约中-申请挂起" or selected_module == "工程师(五组)-预约中-申请挂起" or\
                selected_module == "组长(四组)-预约中-申请挂起"  or selected_module == "组长(四组)-预约中-审核挂起-通过" or selected_module == "服务台-预约中-审核挂起-通过" \
                or selected_module == "组长(四组)-预约中-审核挂起-不通过" or selected_module == "服务台-预约中-审核挂起-不通过" or Solution=="服务台-已挂起-解挂和改派-预约中":
            if roleName == "普通用户" and (CheckModule == "客户端--报修广场--我的报修" or CheckModule == "小程序--首页" or CheckModule == "客户端-报修广场-全部"):
                self.FilterParameters["任务办理"] = ["进度", "投诉","催单"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "用户管理员" and (CheckModule == "客户端--报修广场--外协" or CheckModule == "客户端-报修广场-全部" or CheckModule == "小程序--首页" or
                                          (ticketServeType=="1" and CheckModule == "小程序--紧急报修") or  (ticketServeType=="2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度", "投诉","催单"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "区域管理员" and (CheckModule == "客户端--报修广场--外协" or CheckModule == "客户端-报修广场-全部" or CheckModule == "小程序--首页"  or
                                          (ticketServeType=="1" and CheckModule == "小程序--紧急报修") or  (ticketServeType=="2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度", "投诉","评论","催单"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "运维工程师" and (CheckModule == "服务端--事件--预约中"  or CheckModule == "小程序--首页" or
                                             (ticketServeType=="1" and CheckModule == "小程序--紧急报修") or  (ticketServeType=="2" and CheckModule == "小程序--驻场服务") ):
                if selected_module == "组长(四组)-待响应-改派-工程师(四组)" or selected_module == "组长(四组)-预约中-审核挂起-不通过" or hangUp_roleName =="运维工程师" :
                    self.FilterParameters["任务办理"] = ["进度","到达现场","挂起"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                elif selected_module == "组长（四组）-待响应-接单" or selected_module == "工程师(四组)-预约中-申请挂起" or selected_module == "工程师(五组)-预约中-申请挂起" or \
                        selected_module == "组长(四组)-预约中-申请挂起" or selected_module == "服务台-预约中-审核挂起-不通过" or hangUp_roleName =="运维经理":
                    self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                else:
                    ExpectationsThat = "实际值里没有预期值"
            elif roleName == "运维经理" and ( CheckModule == "服务端--事件--预约中"  or CheckModule == "小程序--首页" or
                                          (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                if selected_module == "组长(四组)-待响应-改派-工程师(四组)"or  selected_module == "组长(四组)-预约中-申请挂起" or selected_module == "组长(四组)-预约中-审核挂起-不通过"\
                        or hangUp_roleName =="运维工程师":
                    self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                elif selected_module == "组长（四组）-待响应-接单" or selected_module == "服务台-预约中-审核挂起-不通过"  or hangUp_roleName =="运维经理":
                    self.FilterParameters["任务办理"] = ["进度", "到达现场", "挂起"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                elif selected_module == "工程师(四组)-预约中-申请挂起" or selected_module == "工程师(五组)-预约中-申请挂起":
                    self.FilterParameters["任务办理"] = ["进度","挂起审核"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                else:
                    ExpectationsThat = "实际值里没有预期值"
            elif roleName == "服务台" and (CheckModule == "服务端--事件--预约中"  or CheckModule == "小程序--首页" or
                                          (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                if selected_module == "组长(四组)-待响应-改派-工程师(四组)" or selected_module == "组长（四组）-待响应-接单" or  selected_module == "组长(四组)-预约中-审核挂起-不通过" \
                    or selected_module == "服务台-预约中-审核挂起-不通过"  or selected_module == "工程师(四组)-预约中-申请挂起" or selected_module == "工程师(五组)-预约中-申请挂起" or \
                    Solution=="服务台-已挂起-解挂和改派-预约中":
                    self.FilterParameters["任务办理"] = ["进度", "撤销"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                elif selected_module == "组长(四组)-预约中-申请挂起":
                    self.FilterParameters["任务办理"] =  ["进度", "撤销","挂起审核"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                elif (selected_module == "组长(四组)-预约中-审核挂起-通过" or selected_module == "服务台-预约中-审核挂起-通过") and CheckModule == "服务端-事件-全部工单":
                    self.FilterParameters["任务办理"] = ["进度", "撤销", "解挂", "改派"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                else:
                    ExpectationsThat = "实际值里没有预期值"
            elif roleName == "运维总监" and (CheckModule == "服务端--事件--预约中"  or CheckModule == "小程序--首页" or
                                          (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                if selected_module == "组长(四组)-待响应-改派-工程师(四组)" or selected_module == "组长（四组）-待响应-接单" or selected_module == "组长(四组)-预约中-审核挂起-不通过" \
                        or selected_module == "服务台-预约中-审核挂起-不通过" or selected_module == "工程师(四组)-预约中-申请挂起" or selected_module == "组长(四组)-预约中-申请挂起"  \
                        or Solution=="服务台-已挂起-解挂和改派-预约中" or selected_module == "工程师(五组)-预约中-申请挂起" :
                    self.FilterParameters["任务办理"] = ["进度"]                         # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                else:
                    ExpectationsThat = "实际值里没有预期值"
            elif (roleName == "运维工程师" or roleName == "运维经理" or roleName == "服务台" or roleName == "运维总监") and CheckModule == "服务端--事件--已挂起" :
                if  roleName != "服务台" and (selected_module == "组长(四组)-预约中-审核挂起-通过" or selected_module == "服务台-预约中-审核挂起-通过"):
                    self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                elif roleName == "服务台" and (selected_module == "组长(四组)-预约中-审核挂起-通过" or selected_module == "服务台-预约中-审核挂起-通过"):
                    self.FilterParameters["任务办理"] = ["进度","撤销","解挂","改派"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                else:
                    ExpectationsThat = "实际值里没有预期值"
            else:
                ExpectationsThat = "实际值里没有预期值"
        elif selected_module == "工程师（四组）-预约中-到达现场" or  selected_module == "工程师（五组）-预约中-到达现场" or selected_module == "组长（四组）-预约中-到达现场" or selected_module == "工程师(四组)-处理中-申请挂起" or \
                selected_module == "组长(四组)-处理中-申请挂起" or selected_module == "组长(四组)-处理中-审核挂起-通过" or selected_module == "服务台-处理中-审核挂起-通过" or selected_module == "工程师(五组)-处理中-申请挂起" or \
                selected_module == "组长(四组)-处理中-审核挂起-不通过" or  selected_module == "组长(五组)-处理中-审核挂起-不通过" or selected_module == "服务台-处理中-审核挂起-不通过" or \
                Solution == "服务台-已挂起-解挂和改派-处理中":
            if roleName == "普通用户" and ( CheckModule == "客户端--报修广场--我的报修" or CheckModule == "小程序--首页" or CheckModule == "客户端-报修广场-全部"):
                self.FilterParameters["任务办理"] = ["进度", "投诉", "催单"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "用户管理员" and (CheckModule == "客户端--报修广场--外协" or CheckModule == "客户端-报修广场-全部" or CheckModule == "小程序--首页" or
                (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度", "投诉", "催单"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "区域管理员" and (CheckModule == "客户端--报修广场--外协" or CheckModule == "客户端-报修广场-全部" or CheckModule == "小程序--首页" or
                    (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度", "投诉", "评论", "催单"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "运维工程师" and (CheckModule == "服务端--事件--处理中"  or CheckModule == "小程序--首页" or
                    (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                if selected_module == "工程师（四组）-预约中-到达现场" or  selected_module == "工程师（五组）-预约中-到达现场" or  selected_module == "组长(四组)-处理中-审核挂起-不通过"  \
                        or hangUp_roleName =="运维工程师" or  selected_module == "组长(五组)-处理中-审核挂起-不通过":
                    self.FilterParameters["任务办理"] = ["进度", "完成工单", "挂起"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                elif selected_module == "组长（四组）-预约中-到达现场" or selected_module == "工程师(四组)-处理中-申请挂起"  or selected_module == "工程师(五组)-处理中-申请挂起" or  \
                    selected_module == "组长(四组)-处理中-申请挂起" or  selected_module == "服务台-处理中-审核挂起-不通过" or hangUp_roleName =="运维经理":
                    self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                else:
                    ExpectationsThat = "实际值里没有预期值"
            elif roleName == "运维经理" and ( CheckModule == "服务端--事件--处理中"  or CheckModule == "小程序--首页" or
                    (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                if selected_module == "工程师（四组）-预约中-到达现场" or  selected_module == "工程师（五组）-预约中-到达现场" or selected_module == "组长(四组)-处理中-申请挂起" \
                        or selected_module == "组长(四组)-处理中-审核挂起-不通过"  or selected_module == "组长(五组)-处理中-审核挂起-不通过" or hangUp_roleName =="运维工程师":
                    self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                elif selected_module == "组长（四组）-预约中-到达现场" or selected_module == "服务台-处理中-审核挂起-不通过" or hangUp_roleName =="运维经理":
                    self.FilterParameters["任务办理"] = ["进度", "完成工单", "挂起"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                elif selected_module == "工程师(四组)-处理中-申请挂起" or selected_module == "工程师(五组)-处理中-申请挂起":
                    self.FilterParameters["任务办理"] = ["进度", "挂起审核"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                else:
                    ExpectationsThat = "实际值里没有预期值"
            elif roleName == "服务台" and ( CheckModule == "服务端--事件--处理中"  or CheckModule == "小程序--首页" or
                    (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                if selected_module == "工程师（四组）-预约中-到达现场" or  selected_module == "工程师（五组）-预约中-到达现场" or selected_module == "组长（四组）-预约中-到达现场" \
                   or selected_module == "工程师(四组)-处理中-申请挂起" or selected_module == "组长(四组)-处理中-审核挂起-不通过" or selected_module == "服务台-处理中-审核挂起-不通过" \
                or Solution == "服务台-已挂起-解挂和改派-处理中" or selected_module == "工程师(五组)-处理中-申请挂起" or selected_module == "组长(五组)-处理中-审核挂起-不通过":
                    self.FilterParameters["任务办理"] = ["进度", "撤销"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                elif selected_module == "组长(四组)-处理中-申请挂起":
                    self.FilterParameters["任务办理"] = ["进度", "撤销","挂起审核"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                else:
                    ExpectationsThat = "实际值里没有预期值"
            elif roleName == "运维总监" and (CheckModule == "服务端--事件--处理中"  or CheckModule == "小程序--首页" or(ticketServeType == "1" and CheckModule == "小程序--紧急报修"
            ) or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                if selected_module == "工程师（四组）-预约中-到达现场" or  selected_module == "工程师（五组）-预约中-到达现场" or selected_module == "组长（四组）-预约中-到达现场" \
                    or selected_module == "工程师(四组)-处理中-申请挂起" or selected_module == "组长(四组)-处理中-审核挂起-不通过" or selected_module == "服务台-处理中-审核挂起-不通过" \
                    or selected_module == "组长(四组)-处理中-申请挂起" or selected_module == "工程师(五组)-处理中-申请挂起" or Solution == "服务台-已挂起-解挂和改派-处理中" \
                        or selected_module == "组长(五组)-处理中-审核挂起-不通过":
                    self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                else:
                    ExpectationsThat = "实际值里没有预期值"
            elif (roleName == "服务台" or roleName == "运维总监" or roleName == "运维经理" or roleName == "运维工程师") and CheckModule == "服务端--事件--已挂起" :
                if  roleName != "服务台" and (selected_module == "组长(四组)-处理中-审核挂起-通过" or selected_module == "服务台-处理中-审核挂起-通过"):
                    self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                elif roleName == "服务台" and (selected_module == "组长(四组)-处理中-审核挂起-通过" or selected_module == "服务台-处理中-审核挂起-通过"):
                    self.FilterParameters["任务办理"] = ["进度", "撤销", "解挂","改派"]  # 获取预期任务办理按钮
                    ExpectationsThat = "实际值包含预期值"
                else:
                    ExpectationsThat = "实际值里没有预期值"
            else:
                ExpectationsThat = "实际值里没有预期值"
        elif selected_module == "工程师(四组)-处理中-完成工单" or selected_module == "工程师(五组)-处理中-完成工单" or selected_module == "组长(四组)-处理中-完成工单":
            if roleName == "普通用户" and ( CheckModule == "客户端-报修广场-已完成" or CheckModule == "小程序--首页" or CheckModule == "客户端-报修广场-全部"):
                self.FilterParameters["任务办理"] = ["进度", "投诉", "评价"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "用户管理员" and (CheckModule == "客户端-报修广场-已完成" or CheckModule == "客户端-报修广场-全部" or CheckModule == "小程序--首页" or
                    (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度", "投诉"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "区域管理员" and (CheckModule == "客户端-报修广场-已完成" or CheckModule == "客户端-报修广场-全部" or CheckModule == "小程序--首页" or
                    (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度", "投诉", "评论"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "运维工程师" and (CheckModule == "服务端--事件--已处理"  or CheckModule == "小程序--首页" or
                    (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "运维经理" and ( CheckModule == "服务端--事件--已处理"  or CheckModule == "小程序--首页" or
                    (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "服务台" and ( CheckModule == "服务端--事件--已处理"  or CheckModule == "小程序--首页" or
                    (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度", "撤销"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            elif roleName == "运维总监" and (CheckModule == "服务端--事件--已处理"  or CheckModule == "小程序--首页" or
                    (ticketServeType == "1" and CheckModule == "小程序--紧急报修") or (
                            ticketServeType == "2" and CheckModule == "小程序--驻场服务")):
                self.FilterParameters["任务办理"] = ["进度"]  # 获取预期任务办理按钮
                ExpectationsThat = "实际值包含预期值"
            else:
                ExpectationsThat = "实际值里没有预期值"
        else:
            self.FilterParameters["任务办理"]=None
            ExpectationsThat = "实际值里没有预期值"
        return self.FilterParameters,ExpectationsThat






class workOrder_list_expect:
    """工单清单页面预期值"""

    def __init__(self, userinfo, parameterSet =None,port=None):
        self.userinfo = userinfo
        self.parameterSet  = parameterSet
        self.port = port
        self.expectedValue = None



    def workOrder_list_Management(self):
        """
        工单清单各个接口预期值管理
        :return:
        """
        atLast_list_workOrder=None
        if self.port=="小程序首页工单":
            atLast_list_workOrder=workOrder_list_expect(self.userinfo,self.parameterSet).noOffTicketListData()
        elif self.port == "内部代办理工单":
            atLast_list_workOrder = workOrder_list_expect(self.userinfo, self.parameterSet).InsideRepairListData()
        elif self.port == "用户管理员区域管理员外协报修列表数据":
            atLast_list_workOrder = workOrder_list_expect(self.userinfo, self.parameterSet).ExternalRepairListData()
        elif self.port == "外部用户-我的报修":
            atLast_list_workOrder = workOrder_list_expect(self.userinfo, self.parameterSet).MyRepairListData()
        elif self.port == "全部工单、紧急事件、驻场事件（包含已关单数据）":
            atLast_list_workOrder = workOrder_list_expect(self.userinfo, self.parameterSet).allListData()
        return atLast_list_workOrder





    def noOffTicketListData(self):
        """
        工单清单-内部代办理工单
        :return:
        """
        print(" ")
        print("\033[37;40m%%%%%%%%%%%%%%%%%%%%%%%%开始获取预期值%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        appletName=None;list_workOrder=None;atLast_list_workOrder=None
        # 取出平台名称
        appletName=self.parameterSet["平台名称"]
        # 通过SQL获取预期值
        list_workOrder_time, sql = dataProcessing("noOffTicketListData_WorkOrderList").user_name(self.userinfo, appletName)
        if list_workOrder_time:
            # 获取任务办理按钮
            list_workOrder = Task_handling_button(list_workOrder_time, self.userinfo).applet_TaskHandlingButton(appletName) #工单清单-首页-预期值
            # 转化时间格式为字符串
            list_dataKey_time = ["工单创建日期", "工单更新日期"]
            atLast_list_workOrder = TimeFormat(list_workOrder, list_dataKey_time).listNestDict_TimeType_str()
        else:
            atLast_list_workOrder = None
        print("\033[1;34;40m返回的最终预期值：",atLast_list_workOrder)
        print(" ")
        return  atLast_list_workOrder



    def InsideRepairListData(self):
        """
        工单清单-客户端-外协工单
        :return:
        """
        print(" ")
        print("\033[37;40m%%%%%%%%%%%%%%%%%%%%%%%%开始获取预期值%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        appletName=None;list_workOrder=None;atLast_list_workOrder=None
        # 取出平台名称
        appletName=self.parameterSet["平台名称"]
        # 通过SQL获取预期值
        list_workOrder_time, sql = dataProcessing("InsideRepairListData_WorkOrderList").user_name(self.parameterSet,self.userinfo)
        if list_workOrder_time:
            # 获取任务办理按钮
            list_workOrder = Task_handling_button(list_workOrder_time, self.userinfo).applet_TaskHandlingButton(appletName) #工单清单-首页-预期值
            # 转化时间格式为字符串
            list_dataKey_time = ["工单创建日期", "工单更新日期"]
            atLast_list_workOrder = TimeFormat(list_workOrder, list_dataKey_time).listNestDict_TimeType_str()
        else:
            atLast_list_workOrder=None
        print("\033[1;34;40m返回的最终预期值：",atLast_list_workOrder)
        print(" ")
        return  atLast_list_workOrder



    def ExternalRepairListData(self):
        """
        工单清单-客户端-外协工单
        :return:
        """
        print(" ")
        print("\033[37;40m%%%%%%%%%%%%%%%%%%%%%%%%开始获取预期值%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        appletName=None;list_workOrder=None;atLast_list_workOrder=None
        # 取出平台名称
        appletName=self.parameterSet["平台名称"]
        # 通过SQL获取预期值
        list_workOrder_time, sql = dataProcessing("ExternalRepairListData_WorkOrderList").user_name(self.parameterSet,self.userinfo)
        if list_workOrder_time:
            # 获取任务办理按钮
            list_workOrder = Task_handling_button(list_workOrder_time, self.userinfo).applet_TaskHandlingButton(appletName) #工单清单-首页-预期值
            # 转化时间格式为字符串
            list_dataKey_time = ["工单创建日期", "工单更新日期"]
            atLast_list_workOrder = TimeFormat(list_workOrder, list_dataKey_time).listNestDict_TimeType_str()
        else:
            atLast_list_workOrder=None
        print("\033[1;34;40m返回的最终预期值：",atLast_list_workOrder)
        print(" ")
        return  atLast_list_workOrder


    def MyRepairListData(self):
        """
        工单清单-客户端-我的报修
        :return:
        """
        print(" ")
        print("\033[37;40m%%%%%%%%%%%%%%%%%%%%%%%%开始获取预期值%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        appletName = None;list_workOrder = None;atLast_list_workOrder = None
        # 取出平台名称
        appletName = self.parameterSet["平台名称"]
        # 通过SQL获取预期值
        list_workOrder_time, sql = dataProcessing("MyRepairListData_WorkOrderList").user_name(self.parameterSet)
        if list_workOrder_time:
            # 获取任务办理按钮
            list_workOrder = Task_handling_button(list_workOrder_time, self.userinfo).applet_TaskHandlingButton(
                appletName)  # 工单清单-首页-预期值
            # 转化时间格式为字符串
            list_dataKey_time = ["工单创建日期", "工单更新日期"]
            atLast_list_workOrder = TimeFormat(list_workOrder, list_dataKey_time).listNestDict_TimeType_str()
        else:
            atLast_list_workOrder = None
        print("\033[1;34;40m返回的最终预期值：", atLast_list_workOrder)
        print(" ")
        return atLast_list_workOrder



    def allListData(self):
        """
        工单清单-客户端-我的报修
        :return:
        """
        print(" ")
        print("\033[37;40m%%%%%%%%%%%%%%%%%%%%%%%%开始获取预期值%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        appletName = None;list_workOrder = None;atLast_list_workOrder = None;list_workOrder_time=None
        # 取出平台名称
        appletName = self.parameterSet["平台名称"]
        # 通过SQL获取预期值
        list_workOrder_time_serve, sql_serve = dataProcessing("allListData_WorkOrderList","sj_ticket_serve").user_name(self.parameterSet) # 查询服务工单表
        list_workOrder_time_incident, sql_incident = dataProcessing("allListData_WorkOrderList","sj_ticket_serve_history").user_name(self.parameterSet) # 查询事件库表
        if type(list_workOrder_time_serve)==type(["a","b"]) and type(list_workOrder_time_incident)==type(["a","b"]): # 如果服务工单和事件表返回的工单为空，就合并两个列表
            list_workOrder_time=list_workOrder_time_serve+list_workOrder_time_incident # 合并服务工单和事件两个列表
        elif type(list_workOrder_time_serve) == type(["a","b"]):
            list_workOrder_time=list_workOrder_time_serve
        elif type(list_workOrder_time_incident) == type(["a","b"]):
            list_workOrder_time=list_workOrder_time_incident
        if list_workOrder_time:
            # 获取任务办理按钮
            list_workOrder = Task_handling_button(list_workOrder_time, self.userinfo).applet_TaskHandlingButton(appletName)  # 全部工单、紧急事件、驻场事件（包含已关单数据）
            # 转化时间格式为字符串
            list_dataKey_time = ["工单创建日期", "工单更新日期"]
            atLast_list_workOrder = TimeFormat(list_workOrder, list_dataKey_time).listNestDict_TimeType_str()
        else:
            atLast_list_workOrder = None
        print("\033[1;34;40m返回的最终预期值：", atLast_list_workOrder)
        print(" ")
        return atLast_list_workOrder