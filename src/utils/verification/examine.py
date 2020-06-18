#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 预期值跟实际值校验后，参数报告的处理方法

from console_colour import Complaint_ConsolePrint
from utils.verification.Expected_actual_comparison import expect_actual_dataComparison
from Test_Report_Generate import GenerateTestReport
from utils.verification.Expected__value import GenerateExpectedValues,workOrder_list_expect
from PrivateMethods import useCase_check_deviceList
from utils.privately_owned.DataType_ParameterProcessing import DataType_processing

####################数据校验###################################################


class examine_data:
    """工单各个清单页面数据校验"""

    def __init__(self,list_actualArgument,userinfo,screening=None):
        self.list_actualArgument=list_actualArgument   # 实际值
        self.userinfo = userinfo                       # 登录用户信息
        self.screening = screening                     # 筛选条件
        self.result=True
        self.testResultDict=None






    def WorkOrderList_dataComparison(self,userinfo_parameter,post_Name):
        """
        校验chooseListData接口返回的数据
        模块：事件--待响应、预约中、待处理、处理中、已处理、已关单、已挂起、全部工单模块
        :param post_Name: 需要校验的工单模块
        :param loginName: 需要校验的用户的用户名
        :param userinfo_parameter: 测试报告的“所属接口”和“所属模块”
        :return: 校验结果
        """
        n =1;all_number_reality = {}  # 初始化测试报告字典
        JSESSIONID =self.userinfo["登录用户JSESSIONID"];      loginName =self.userinfo["登录名"]
        roleName = self.userinfo["用户权限"]  ;               userid = self.userinfo["用户ID"]
        username = self.userinfo["用户名称"]
        # 获取预期值
        expect_workOrder = workOrder_list_expect(self.userinfo,userinfo_parameter,post_Name).workOrder_list_Management()
        """实际值跟预期值对比"""
        result, dicti_testResult = expect_actual_dataComparison(expect_workOrder,self.list_actualArgument).server_incident_workOrder()
        """生成测试结果"""
        self.result, self.testResultDict = GenerateTestReport(result,dicti_testResult).commonality_testReport_dicti(userinfo_parameter)
        PrintingParameters = { "预期值": expect_workOrder, "实际值": self.list_actualArgument,"测试结果": self.result, "测试报告": self.testResultDict}
        appletName=userinfo_parameter["所属模块"]
        Complaint_ConsolePrint(PrintingParameters).ProcessDivider_six("%r"%appletName)
        return self.result, self.testResultDict





class elseVerify:
    """数据校验"""


    def __init__(self,ActualValue_List,userinfo=None):
        self.ActualValue_List = ActualValue_List
        self.userinfo = userinfo
        self.dict_expect={}
        self.list_expect=[]
        self.list_expectNumber=[]
        self.testResultDict ={}
        self.result =True
        self.StandbyParameter =None


    def check_deviceList(self,dicti_parameterPacket):
        """
        校验资产列表
        :param dicti_parameterPacket: 测试报告所需参数
        :return:
        """

        result =True;dicti_testResult=None;expect_list_parameters=None;characterString=None;realAssets=None
        deviceList_result=True;deviceList_testResult=None; filtrate_result=True;filtrate_testResult=None
        """获取对比所需要的参数"""
        roleName = dicti_parameterPacket["用户权限"]
        structureID = dicti_parameterPacket["所选单位ID"];batchNo = dicti_parameterPacket["批次"];equipName = dicti_parameterPacket["设备名称"]
        character = dicti_parameterPacket["测试点"]
        list_locationID,structureName = GenerateExpectedValues(dicti_parameterPacket).AssetsOfEquipmentList__expected(structureID)
        #######################################
        #获取资产列表的预期列表
        expect_list_parameters, characterString = useCase_check_deviceList(batchNo, equipName,structureName).check_deviceList_ExpectedAssetsList(roleName, list_locationID)
        #获取资产列表的实际列表，取出实际资产列表的批次、设备名称、位置信息、设备类型和设备状态
        realAssets = DataType_processing( self.ActualValue_List).compile_property_data()
        ###############################################
        """预期资产列表跟实际资产列表对比,返回字符串类型测试结果,并且生成测试结果"""
        result, dicti_testResult = expect_actual_dataComparison(expect_list_parameters,realAssets).AssetsOfEquipment_dataComparison()
        """生成测试报告"""
        self.result,self.testResultDict = GenerateTestReport(result, dicti_testResult).commonality_testReport_dicti(dicti_parameterPacket)
        PrintingParameters = {"测试点": character, "预期值": expect_list_parameters, "实际值": realAssets,"测试结果":deviceList_result, "测试报告": deviceList_testResult}
        Complaint_ConsolePrint(PrintingParameters).ProcessDivider_five("资产设备清单页面对比")
        ################################################
        return self.result,self.testResultDict




    def verify_ReportStatistics(self,dicti_parameterPacket,module):
        """
        报修数量统计数据对比
        :param dicti_parameterPacket:
        :param module:
        :return:
        """
        compile_list_office =None;testPoint=None
        loginName = dicti_parameterPacket["登录名"];roleName = dicti_parameterPacket["用户权限"];roleName = dicti_parameterPacket["用户权限"]
        list_office = dicti_parameterPacket["所选单位ID"];begin_date = dicti_parameterPacket["开始日期"];finish_date = dicti_parameterPacket["结束日期"]
        register_userinfo = {"登录名":loginName,"用户权限":roleName}
        """获取预期值"""
        self.list_expectNumber=GenerateExpectedValues(dicti_parameterPacket,self.ActualValue_List).verify_ReportStatistics_expect(module)
        """处理实际值，去掉工单数为零的单位"""
        new_ActualValue_List = []
        for ActualValue in self.ActualValue_List:  # 生成一个新的实际值列表
            new_ActualValue_List.append(ActualValue)
        for ActualValue in new_ActualValue_List:
            repairNumber = int(ActualValue["工单数"])
            if repairNumber == 0:
                self.ActualValue_List.remove(ActualValue)
        # 预期值跟实际值对比
        Result, testReport = expect_actual_dataComparison(self.list_expectNumber,self.ActualValue_List).verify_ReportStatistics_dataCheck(module)
        """生成测试报告"""
        self.result, self.testResultDict = GenerateTestReport(Result, testReport).commonality_testReport_dicti(dicti_parameterPacket)
        print("\033[1;34;40m预期值：\033[0m\033[4;35;40m%r"%self.list_expectNumber)
        print("\033[1;34;40m实际值：\033[0m\033[4;35;40m%r"%self.ActualValue_List)
        print("\033[1;34;40m测试结果：\033[0m\033[4;35;40m%r"%self.result)
        print("\033[1;34;40m测试报告：\033[0m\033[4;35;40m%r"%self.testResultDict)
        return self.result,self.testResultDict



    def ListOfComplaints_verify(self,dicti_parameterPacket):
        """
        投诉清单页面数据校验
        :param dicti_parameterPacket: 参数包
        :return:
        """

        """获取预期值"""
        Complaint_expect_list_data = GenerateExpectedValues(dicti_parameterPacket).complaintsList_expected()
        """预期投诉清单列表与实际投诉清单列表对比"""
        result,dicti_testResult=expect_actual_dataComparison(Complaint_expect_list_data,self.ActualValue_List).complaint_list_dataComparison()
        """生成测试结果"""
        self.result,self.testResultDict= GenerateTestReport(result,dicti_testResult).commonality_testReport_dicti(dicti_parameterPacket)
        print("\033[1;34;40m投诉清单页面预期值：\033[0m\033[4;35;40m%r" % Complaint_expect_list_data)
        print("\033[1;34;40m投诉清单页面实际值：\033[0m\033[4;35;40m%r" % self.ActualValue_List)
        print("\033[1;34;40m测试结果：\033[0m\033[4;35;40m%r" % self.result)
        print("\033[1;34;40m测试报告：\033[0m\033[4;35;40m%r" % self.testResultDict)
        return self.result,self.testResultDict














































