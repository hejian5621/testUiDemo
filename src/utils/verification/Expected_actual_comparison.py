#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 预期值跟实际值对比


from privately_owned.method import EachQuantityType_transition_CharacterString,ValueGenerationList
from utils.privately_owned.data_Verification import data_check
from utils.privately_owned.DataType_ParameterProcessing import DataType_processing

####################预期值跟实际值对比###################################


class expect_actual_dataComparison:
    """
    传入预期值和实际值进行比较，生成字符串报告
    """
    def __init__(self,expect_value,actual__value):
        # 预期值
        self.expect_value = expect_value
        # 实际值
        self.actual__value = actual__value
        # 返回值
        self.result = True
        self.dicti_str_returned = None


    def server_incident_workOrder(self):
        """
        服务端小程序--事件模块预期值跟实际值对比
        :return:
        """
        # 预期值跟实际值对比
        result,initial_testReport = data_check(self.expect_value, self.actual__value).TheTwoList_different("工单编号")
        return result, initial_testReport





    def AssetsOfEquipment_dataComparison(self):
        """
         资产设备页面数据对比，返回字符串类型的测试报告
        :return:
        """

        """预期资产列表跟实际资产列表对比"""
        self.result, self.dicti_str_returned = data_check(self.expect_value, self.actual__value).TheTwoList_different("批次")
        return self.result,self.dicti_str_returned




    def complaint_list_dataComparison(self):
        """
        投诉列表页面数据对比，生成字符串报告
        :return:
        """
         #  预期值跟实际值对比
        result, self.dicti_str_returned = data_check(self.expect_value, self.actual__value).TheTwo_list()
        # 判断测试是否通过，result：True通过； False：没有通过
        if result:
            self.dicti_str_returned = None
        return  result ,self.dicti_str_returned



    def verify_ReportStatistics_dataCheck(self,module):
        """
        工单数量统计模块数据对比，生成字符串数据类型的测试报告
        :return:
        """
        if module == "报修数量":  # 删除报修数量统计模块实际值里的单位报修数为零的单位
            basics_key="单位名称"
        else:
            basics_key = "故障名称"
        #  预期值跟实际值对比
        self.result,self.dicti_str_returned = data_check( self.expect_value,self.actual__value).TheTwoList_different(basics_key)
        return self.result,self.dicti_str_returned





class  asset_privately_dataComparison:
    """
    资产设备页面，私有的数据对比
    """

    def __init__(self,expected_result,actual_result):
        # 预期结果
        self.expected_result=expected_result
        # 实际结果
        self.actual_result=actual_result
        #  批次测试结果
        self.result_batch = None
        self.list_consequence_batch = None
        # 设备名称测试结果
        self.result_equipName = None
        self.list_consequence_equipName = None
        # 单位名称测试结果
        self.result_structureName = None
        self.list_consequence_structureName = None
        # 返回的测试结果
        self.result =True
        self.str_TestResultData =None




    def add_jurisdiction_equality(self):
        """
         新增投诉信息后，各个权限对新增数据进行对比必须相等（预期值实际值）
        :return:
        """
        self.result,self.str_TestResultData = data_check(self.expected_result,self.actual_result).TheTwoList_different("投诉单ID")
        return self.result, self.str_TestResultData


    def add_jurisdiction_include(self,Contrast):
        """
         新增工单信息后，各个权限对新增数据进行对比实际值包含预期值（预期值实际值）
        :return:
        """
        result=True;list_testReport=None; testResult=None;actual_list1=[]
        if  Contrast=="实际值包含预期值":
            # 两个列表对比，实际值包含预期值
            result, list_testReport  = data_check(self.actual_result,self.expected_result).TheTwo_list_include()
        elif Contrast=="实际值里没有预期值":
            New_actual_result=[]
            if self.actual_result and self.actual_result !=['为空']:
                # 去掉实际值里的任务办理按钮
                for actual in self.actual_result:
                    actual["任务办理"]= None
                    New_actual_result.append(actual)
            # 两个列表对比，实际值不包含预期值
            result, list_testReport = data_check(self.expected_result, New_actual_result).TheTwo_list_Not_include()
        if result:
            self.str_TestResultData = "为空"
        else:
            # 取出预期值的工单编号
            expected_WorkOrderNumber = DataType_processing(self.expected_result).list_nest_dict_list("工单编号")
            actual_WorkOrderNumber = DataType_processing(self.actual_result).list_nest_dict_list("工单编号")
            # 判断工单预期值的工单编号在实际值有没有
            if expected_WorkOrderNumber and actual_WorkOrderNumber:
                # 判断预期值是否属于实际值
                for i in expected_WorkOrderNumber:
                    if i in actual_WorkOrderNumber:
                        for actual in self.actual_result:
                            WorkOrderNumber = actual["工单编号"]
                            if i == WorkOrderNumber:
                                actual_list1.append(actual)
            # 测试结果转化成字符串
            str_ActualNotExpect = EachQuantityType_transition_CharacterString(self.expected_result).DataTypeConversion_console()
            str_ExpectNotActual = EachQuantityType_transition_CharacterString(actual_list1).DataTypeConversion_console()
            if   Contrast=="实际值包含预期值":
                testResult = "预期：实际值包含预期值；实际：实际值没有包含预期值；测试失败"
            elif Contrast=="实际值里没有预期值":
                testResult = "预期：实际值不包含预期值；实际：实际值包含了预期值；测试失败"
            self.str_TestResultData = {"预期结果": str_ActualNotExpect, "实际结果": str_ExpectNotActual, "测试结果": testResult}
            self.result = False
        return self.result, self.str_TestResultData



    def add_jurisdiction_Not_include(self):
        """
         新增信息后，各个权限对新增数据进行对比实际值不包含预期值（预期值实际值）
        :return:
        """
        result  = data_check(self.expected_result,self.actual_result).TheTwo_list_Not_include()
        if result:
            self.str_TestResultData = "为空"
        else:
            # 测试结果转化成字符串
            str_ActualNotExpect = EachQuantityType_transition_CharacterString(
                self.expected_result).DataTypeConversion_console()
            str_ExpectNotActual = EachQuantityType_transition_CharacterString(
                self.actual_result).DataTypeConversion_console()
            testResult = "实际值里有预期值，不通过，测试结果："
            self.str_TestResultData = {"预期结果": str_ActualNotExpect, "实际结果": str_ExpectNotActual, "测试结果": testResult}
            self.result = False
        return self.result, self.str_TestResultData



class OtherInterfaces_expectActual:
    """其他预期值跟实际值对比"""


    def __init__(self,expect_value,actual__value):
        # 预期值
        self.expect_value = expect_value
        # 实际值
        self.actual__value = actual__value
        # 返回值
        self.result = True
        self.dicti_str_returned = None


    def findGroupList_expectActual(self):
        """
        查询所有群组(服务台改派用):预期值更实际值对比，预期值等于实际值
        :return:
        """
        self.result ,self.dicti_str_returned = data_check(self.expect_value, self.actual__value).TheTwo_list()
        self.dicti_str_returned["测试结果"]="测试失败"
        if self.result:
            self.dicti_str_returned = None
        return self.result, self.dicti_str_returned















