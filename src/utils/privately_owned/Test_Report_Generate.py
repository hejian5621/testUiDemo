#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 处理测试结果


from privately_owned.Task_handling_button import IndependentMethod
from commonality.database_SqlRealize import dataProcessing
from src.utils.privately_owned.TestReport_sorting import  TestReport_data_neaten



##############处理测试结果#####################



class GenerateTestReport:
    """ 生成测试报表数据类型"""


    def __init__(self,result,dicti_testResult,dicti_pack=None):
        # 测试结果
        self.result = result
        # 测试结果参数
        self.dicti_testResult = dicti_testResult
        # 打包--字典键名
        self.dicti_pack = dicti_pack
        self.testResultDict ={}
        self.number_report_list=None



    def commonality_testResult(self):
        """
        公共测试结果方法
        返回数据类型：{a：[b,c,d,e],a：[b,c,d,e]}
        :return:
        """
        # 所属接口
        test_interface = self.dicti_testResult["所属接口"]
        # 所属模块
        test_module = self.dicti_testResult["所属模块"]
        #检查登录用户信息
        Check_user = self.dicti_testResult["检查登录用户信息"]
        # 测试点
        test_point = self.dicti_testResult["测试点"]
        # 预期结果
        expectedResult = self.dicti_testResult["预期结果"]
        # 实际结果
        actualResult = self.dicti_testResult["实际结果"]
        """测试结果"""
        testResult = self.dicti_testResult["测试结果"]
        """把测试点、预期结果、 实际结果、测试结果存入列表"""
        self.number_report_list = TestReport_data_neaten.TestResultContent(test_interface,test_module,Check_user,test_point, expectedResult,actualResult, testResult)
        """测试结果打包"""
        self.testResultDict[self.dicti_pack] = self.number_report_list
        return self.testResultDict


    def commonality_testResult_list(self):
        """
        公共测试结果方法
        返回数据类型：{a：[b,c,d,e],a：[b,c,d,e]}
        :return:
        """
        # 所属接口
        dicti_pack = self.dicti_testResult["字典的键"]
        # 所属接口
        test_interface = self.dicti_testResult["所属接口"]
        # 所属模块
        test_module = self.dicti_testResult["所属模块"]
        #检查登录用户信息
        Check_user = self.dicti_testResult["检查登录用户信息"]
        # 测试点
        test_point = self.dicti_testResult["测试点"]
        # 预期结果
        expectedResult = self.dicti_testResult["预期结果"]
        # 实际结果
        actualResult = self.dicti_testResult["实际结果"]
        """测试结果"""
        testResult = self.dicti_testResult["测试结果"]
        """把测试点、预期结果、 实际结果、测试结果存入列表"""
        self.number_report_list = TestReport_data_neaten.TestResultContent(test_interface,test_module,Check_user,test_point, expectedResult,actualResult, testResult)
        """测试结果打包"""
        self.testResultDict[dicti_pack] = self.number_report_list
        return self.testResultDict



    def commonality_testReport_dicti(self,userinfo_parameter):
        """
        公共的生成可以写入电子表格的测试报告列表
        :param userinfo_parameter: 测试报告的“所属接口”和“所属模块”
        :return:
        """
        if self.result :
            pass
        else:
            self.dicti_testResult["字典的键"] = userinfo_parameter["字典的键"]
            self.dicti_testResult["所属接口"]=userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["测试点"] = userinfo_parameter["测试点"]
            self.dicti_testResult["测试结果"] = userinfo_parameter["测试结果"]
            self.testResultDict = GenerateTestReport( None,self.dicti_testResult).commonality_testResult_list()
        return self.result,self.testResultDict




    def TestReportType_repairsQuantityStatistics(self,list_office,loginName,roleName,Str_date,begin_date,finish_date,module,userinfo_parameter):
        """
        报修数量统计数据对比测试报告数据类型
        :return:
        """
        testPoint=None
        if self.result:
            pass
        else:
            officeName = None
            if list_office != None:
                officeId = list_office[0]
                officeName,sql = dataProcessing("officeID_officeName").user_name(officeId)
                officeName = officeName[0]
                officeName = officeName["单位名称"]
            if module == "报修数量":
                testPoint = "单位筛选：%r；时间筛选：%r（开始时间：%r；结束时间：%r）；测试报修数量统计." % (
                officeName, Str_date, begin_date, finish_date)
            elif module == "故障数量":
                testPoint = "单位筛选：%r；时间筛选：%r（开始时间：%r；结束时间：%r）；测试故障类型统计." % (
                     officeName, Str_date, begin_date, finish_date)
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["所属接口"] = userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["测试点"]=testPoint
            dicti = "报修数量统计"
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult, dicti).commonality_testResult()
        return self.result,self.testResultDict



class ListDataDuplication:
    """列表数据重复"""

    def __init__(self,result,dicti_testResult,dicti_pack=None):
        # 测试结果
        self.result = result
        # 测试结果参数
        self.dicti_testResult = dicti_testResult
        # 打包--字典键名
        self.dicti_pack = dicti_pack
        self.testResultDict ={}
        self.number_report_list=None




    def examine_repetition_testReport(self,userinfo_parameter):
        """
        检查数据重复生成测试报告
        :return:
        """
        loginName =userinfo_parameter["登录名"]
        roleName = userinfo_parameter["用户权限"]
        FilterParameters = userinfo_parameter["重复筛选参数"]
        if self.result:
            pass
        else:
            """测试点"""
            test_point = "1、登录名：%r；权限：%r”；%r；\n" \
                         "2、接口返回编译过的数据列表里的数据有没重复" % (loginName,roleName,FilterParameters)
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["所属接口"] = userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["测试点"] = test_point
            dicti = "%r%r%r"% (loginName,roleName,userinfo_parameter)
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult,dicti).commonality_testResult()
        return self.result,self.testResultDict





class AssetsOfEquipment:
    """
    资产设备带上筛选条件生成测试报告数据类型
    """

    def __init__(self,result,dicti_testResult,dicti_pack=None):
        # 测试结果
        self.result = result
        # 测试结果参数
        self.dicti_testResult = dicti_testResult
        # 打包--字典键名
        self.dicti_pack = dicti_pack
        self.testResultDict ={}
        self.number_report_list=None


    def AssetsOfEquipment_interior_batch_equipNameNone_structureNameNone(self,userinfo_parameter):
        """
        内部用户
        2/批次不为空，设备名称为空，单位id为空
        :return:
        """
        if self.result:
            pass
        else:
            """测试点"""
            test_point = "筛选条件：内部用户，“2/批次不为空，设备名称为空，单位id为空”"
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["所属接口"] = userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["测试点"] = test_point
            dicti = "内部用户，批次不为空，设备名称为空,单位id为空"
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult, dicti).commonality_testResult()
        return self.result,self.testResultDict




    def AssetsOfEquipment_external_batch_equipNameNone_structureNameNone(self,userinfo_parameter):
        """
        内部用户
        2/批次不为空，设备名称为空，单位id为空
        :return:
        """
        if self.result:
            pass
        else:
            """测试点"""
            test_point = "筛选条件：外部用户，“2/批次不为空，设备名称为空，单位id为空；批号和设备名称筛选条件对比”"
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["所属接口"] = userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["测试点"] = test_point
            dicti = "外部用户，批次不为空、设备名称为空、单位id为空"
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult, dicti).commonality_testResult()
        return self.result,self.testResultDict


    def AssetsOfEquipment_interior_batchNone_equipName_structureNameNone(self,userinfo_parameter):
        """
        内部用户
        # 3/批次为空、设备名称不为空、单位id为空
        :return:
        """
        if self.result:
            pass
        else:
            """测试点"""
            test_point = "筛选条件：内部用户,“3/批次为空、设备名称不为空、单位id为空；设备名称筛选条件对比”"
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["所属接口"] = userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["测试点"] = test_point
            dicti = "内部用户，批次为空、设备名称不为空、单位id为空"
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult, dicti).commonality_testResult()
        return self.result,self.testResultDict


    def AssetsOfEquipment_external_batchNone_equipName_structureNameNone(self,userinfo_parameter):
        """
       外部用户
       # 3/批次为空、设备名称不为空、单位id为空
        :return:
        """
        if self.result:
            pass
        else:
            """测试点"""
            test_point = "筛选条件：外部用户,“3/批次为空、设备名称不为空；单位和设备名称筛选条件对比”"
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["所属接口"] = userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["测试点"] = test_point
            dicti = "内部用户，批次为空、设备名称不为空、单位id为空"
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult, dicti).commonality_testResult()
        return self.result,self.testResultDict



    def AssetsOfEquipment_interior_batchNone_equipNameNone_structureName(self,userinfo_parameter):
        """
       外部用户
        # 4/批次为空、设备名称为空、单位id不为空
        :return:
        """
        if self.result:
            pass
        else:
            """测试点"""
            test_point = "筛选条件：外部和内部用户，“4/批次为空、设备名称为空、单位id不为空；单位名称筛选条件对比”"
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["所属接口"] = userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["测试点"] = test_point
            dicti = "内部用户或者内部用户，批次为空、设备名称为空、单位id不为空"
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult, dicti).commonality_testResult()
        return self.result,self.testResultDict


    def AssetsOfEquipmentinterior_batch_equipName_structureNameNone(self,userinfo_parameter):
        """
       内部用户
        # 5/批次不为空、设备名称不为空、单位id为空
        :return:
        """
        if self.result:
            pass
        else:
            """测试点"""
            test_point = "筛选条件：内部用户，“5/批次不为空、设备名称不为空、单位id为空；批号和设备名称筛选条件对比”"
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["所属接口"] = userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["测试点"] = test_point
            dicti = "内部用户，批次不为空、设备名称不为空、单位id为空"
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult, dicti).commonality_testResult()
        return self.result,self.testResultDict


    def AssetsOfEquipmentinterior_external_batch_equipName_structureNameNone(self,userinfo_parameter):
        """
       外部用户
        # 5/批次不为空、设备名称不为空、单位id为空
        :return:
        """
        if self.result:
            pass
        else:
            """测试点"""
            test_point = "筛选条件：外部用户，“5/批次不为空、设备名称不为空、单位id为空；批号、设备名称和批号筛选条件对比”"
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["所属接口"] = userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["测试点"] = test_point
            dicti = "外部用户，批次不为空、设备名称不为空、单位id为空"
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult, dicti).commonality_testResult()
        return self.result,self.testResultDict



    def AssetsOfEquipmentinterior_interior_batch_equipNameNone_structureName(self,userinfo_parameter):
        """
       外部用户和内部用户
        # 6/批次不为空、设备名称为空、单位id不为空
        :return:
        """
        if self.result:
            pass
        else:
            """测试点"""
            test_point = "筛选条件：外部和内部用户，“6/批次不为空、设备名称为空、单位id不为空；批号和单位名称筛选条件对比”"
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["所属接口"] = userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["测试点"] = test_point
            dicti = "内部用户或者内部用户，批次不为空、设备名称为空、单位id不为空"
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult, dicti).commonality_testResult()
        return self.result,self.testResultDict


    def AssetsOfEquipmentinterior_interior_batchNone_equipName_structureName(self,userinfo_parameter):
        """
       外部和内部用户
        # 7/批次为空、设备名称不为空、单位id不为空
        :return:
        """
        if self.result:
            pass
        else:
            """测试点"""
            test_point = "筛选条件：外部和内部用户，“7/批次为空、设备名称不为空、单位id不为空；设备名称和单位名称筛选条件对比”"
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["所属接口"] = userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["测试点"] = test_point
            dicti = "内部用户和外部用户，批次为空、设备名称不为空、单位id不为空"
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult, dicti).commonality_testResult()
        return self.result,self.testResultDict


    def AssetsOfEquipmentinterior_interior_batch_equipName_structureName(self,userinfo_parameter):
        """
         外部和内部用户
        # 8/批次不为空，设备名称不为空，单位id不为空
        :return:
        """
        if self.result:
            pass
        else:
            """测试点"""
            test_point = "筛选条件：外部和内部用户，“8/批次不为空，设备名称不为空，单位id不为空；批号、设备名称和单位名称称筛选条件对比”"
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["所属接口"] = userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["测试点"] = test_point
            dicti = "内部用户和外部用户，单位id不为空，设备名称不为空，批次不为空"
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult, dicti).commonality_testResult()
        return self.result,self.testResultDict




    def add_external_complaint_examine(self,userinfo_parameter,operation_url,userinfo,procedure):
        """
        外部用户新增投诉信息生成测试报告
        :return:
        """
        loginName=userinfo["登录名"]
        if self.result:
            pass
        else:
            """测试点"""
            test_point = "登录名为“%r”的用户通过接口“%r”%r，后检查数据是否展示正确"%(loginName,operation_url,procedure)
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["所属接口"] = userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["测试点"] = test_point
            dicti = "外部用户，新增投诉信息"
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult, dicti).commonality_testResult()
        return self.result,self.testResultDict



class  WorkOrderProcess_testReport:
    """工单流程测试报告"""



    def __init__(self,result,dicti_testResult,dicti_pack=None):
        # 测试结果
        self.result = result
        # 测试结果参数
        self.dicti_testResult = dicti_testResult
        # 打包--字典键名
        self.dicti_pack = dicti_pack
        self.testResultDict ={}
        self.number_report_list=None


    def clientSide_MyService(self,loginName,CheckModule,procedure):
        """
        工单流程测试报告
        :return:
        """
        if self.result:
            pass
        else:
            """测试点"""
            test_point = "1、用户名为“%r”的用户进行“%r”操作后，\n" \
                         "2、“%r”页面预期值跟实际值对比" % (loginName,procedure,CheckModule)
            self.dicti_testResult["测试点"] = test_point
            dicti = "外部用户，新增投诉信息"
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult, dicti).commonality_testResult()
        return self.result, self.testResultDict


    def findGroupList_MyService(self,userinfo_parameter):
        """
        工单流程测试报告
        :return:
        """
        if self.result:
            pass
        else:
            """测试点"""
            test_point = "服务在对已挂起的工单进行改派操作，在弹出的改派窗口中，群组选择框中的参数是否正确，是否可以选择全部的群组"
            self.dicti_testResult["检查登录用户信息"] = userinfo_parameter["检查登录用户信息"]
            self.dicti_testResult["所属接口"] = userinfo_parameter["所属接口"]
            self.dicti_testResult["所属模块"] = userinfo_parameter["所属模块"]
            self.dicti_testResult["测试点"] = test_point
            dicti = "服务台改派选择群组"
            self.testResultDict = GenerateTestReport(self.result, self.dicti_testResult, dicti).commonality_testResult()
        return self.result, self.testResultDict






