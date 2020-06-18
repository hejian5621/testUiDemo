#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 处理测试报告的方法

from spreadsheet_dispose_method import reportTest_spreadsheet



class TestReport_data_neaten:
    """测试报告数据整理方法"""


    @staticmethod
    def data_takeOut(Usecasename, data, sheet_name, row=2):
        """
        取出字典嵌套列表数据里的列表，并把该列表写入电子表格
        :param data: 测试结果
        :param Usecasename: 测试用例
        :param sheet_name: 表单名
        :param row: 行数
        :return:
        """
        print("传入需要写入的测试报告:", data)
        # 取出最一成字典
        for allkey in data.keys():
            data2 = data[allkey]
            for allkey1 in data2.keys():              # 取出最二成字典
                data3 = data2[allkey1]                # 取出最三成字典
                for key in data3.keys():
                    data_outer = data3[key]           # 取出最四成字典
                    for ke in data_outer.keys():      # 生成空的列表，增加字段
                        result = []
                        list_result1 = data_outer[ke]
                        for result2 in list_result1:
                            result.append(result2)
                        result.insert(0, Usecasename)  # 放入用例名称
                        row = reportTest_spreadsheet(None, sheet_name).report_readInData(result, row)
        return row


    @staticmethod
    def TestResultContent(test_Interface, test_module, Check_user, test_point, expectedResult, actualResult,
                          result_test):
        """
        当测试预期结果或者实际结果的字符串数大于所限制的字符数后，该方法把该预期值或者实际值切割成小于限制的字符数的两个字符串
        :param test_Interface: 测试点参数
        :param Check_user: 检查登录用户信息
        :param test_module: 预期结果
        :param test_point: 测试点参数
        :param expectedResult: 预期结果
        :param actualResult: 实际结果
        :param result_test: 测试结果
        :return: 测试报告列表
        返回的数据模板：
        """
        number_report_list = [];number_report_dicti = {};n = 0
        expect_number = None;actual_number = None;result_number = None
        later_expectedResult_cutOut=None;later_actualResult1_cutOut=None;later_result_test1_cutOut=None;variable = 2500
        while True:
            front_expectedResult_cutOut = None;front_actualResult1_cutOut = None;front_result_test1_cutOut = None;number_report_list = []
            n = n + 1
            if n == 1:
                if expectedResult: expect_number = len(expectedResult)    # 当预期结果不为空的情况下，获取预期结果的字符串数
                else: expect_number = 0                                   # 当预期结果不空的情况下，获取给预期结果的字符串数为零
                if actualResult: actual_number = len(actualResult)        # 当实际结果不为空的情况下，获取实际结果的字符串数
                else:  actual_number = 0                                  # 当实际结果不空的情况下，获取给实际结果的字符串数为零
                if result_test: result_number = len(result_test)          # 当测试结果不为空的情况下，获取测试结果的字符串数
                else:  result_number = 0                                  # 当测试结果不空的情况下，获取给测试结果的字符串数为零
            else:
                if later_expectedResult_cutOut: expect_number = len(later_expectedResult_cutOut)
                else:  later_expectedResult_cutOut = "同上面是同一条"
                if later_actualResult1_cutOut:  actual_number = len(later_actualResult1_cutOut)
                else:  later_actualResult1_cutOut = "同上面是同一条"
                if later_result_test1_cutOut:   result_number = len(later_result_test1_cutOut)
                else:  later_result_test1_cutOut = "同上面是同一条"
            if expect_number > variable or actual_number > variable or result_number > variable:
                # 判断写入测试报告的字符数
                if expect_number > variable and actual_number > variable and result_number > variable:
                    if n == 1:  # 初始
                        # 截取前面
                        front_expectedResult_cutOut = expectedResult[:variable]
                        front_actualResult1_cutOut = actualResult[:variable]
                        front_result_test1_cutOut = result_test[:variable]
                        # 截取后面
                        later_expectedResult_cutOut = expectedResult[variable:]
                        later_actualResult1_cutOut = actualResult[variable:]
                        later_result_test1_cutOut = result_test[variable:]
                    else:
                        # 截取前面
                        front_expectedResult_cutOut = later_expectedResult_cutOut[:variable]
                        front_actualResult1_cutOut = later_actualResult1_cutOut[:variable]
                        front_result_test1_cutOut = later_result_test1_cutOut[:variable]
                        # 截取后面
                        later_expectedResult_cutOut = later_expectedResult_cutOut[variable:]
                        later_actualResult1_cutOut = later_actualResult1_cutOut[variable:]
                        later_result_test1_cutOut = later_result_test1_cutOut[variable:]
                elif expect_number > variable and actual_number > variable and result_number <= variable:
                    if n == 1:
                        # 截取前面
                        front_expectedResult_cutOut = expectedResult[:variable]
                        front_actualResult1_cutOut = actualResult[:variable]
                        front_result_test1_cutOut = result_test
                        # 截取后面
                        later_expectedResult_cutOut = expectedResult[variable:]
                        later_actualResult1_cutOut = actualResult[variable:]
                    else:
                        # 截取前面
                        front_expectedResult_cutOut = later_expectedResult_cutOut[:variable]
                        front_actualResult1_cutOut = later_actualResult1_cutOut[:variable]
                        front_result_test1_cutOut = later_result_test1_cutOut[:variable]
                        # 截取后面
                        later_expectedResult_cutOut = later_expectedResult_cutOut[variable:]
                        later_actualResult1_cutOut = later_actualResult1_cutOut[variable:]
                        later_result_test1_cutOut = None
                elif expect_number > variable and actual_number <= variable and result_number <= variable:
                    if n == 1:
                        # 截取前面
                        front_expectedResult_cutOut = expectedResult[:variable]
                        front_actualResult1_cutOut = actualResult
                        front_result_test1_cutOut = result_test
                        # 截取后面
                        later_expectedResult_cutOut = expectedResult[variable:]
                    else:
                        # 截取前面
                        front_expectedResult_cutOut = later_expectedResult_cutOut[:variable]
                        front_actualResult1_cutOut = later_actualResult1_cutOut[:variable]
                        front_result_test1_cutOut = later_result_test1_cutOut[:variable]
                        # 截取后面
                        later_expectedResult_cutOut = later_expectedResult_cutOut[variable:]
                        later_actualResult1_cutOut = None
                        later_result_test1_cutOut = None
                elif expect_number > variable and actual_number <= variable and result_number > variable:
                    if n == 1:
                        # 截取前面
                        front_expectedResult_cutOut = expectedResult[:variable]
                        front_actualResult1_cutOut = actualResult
                        front_result_test1_cutOut = result_test[:variable]
                        # 截取后面
                        later_expectedResult_cutOut = expectedResult[variable:]
                        later_result_test1_cutOut = result_test[variable:]
                    else:
                        # 截取前面
                        front_expectedResult_cutOut = later_expectedResult_cutOut[:variable]
                        front_actualResult1_cutOut = later_actualResult1_cutOut[:variable]
                        front_result_test1_cutOut = later_result_test1_cutOut[:variable]
                        # 截取后面
                        later_expectedResult_cutOut = later_expectedResult_cutOut[variable:]
                        later_actualResult1_cutOut = None
                        later_result_test1_cutOut = later_result_test1_cutOut[variable:]
                elif expect_number <= variable and actual_number > variable and result_number > variable:
                    if n == 1:
                        # 截取前面
                        front_expectedResult_cutOut = expectedResult
                        front_actualResult1_cutOut = actualResult[:variable]
                        front_result_test1_cutOut = result_test[:variable]
                        # 截取后面
                        later_actualResult1_cutOut = actualResult[variable:]
                        later_result_test1_cutOut = result_test[variable:]
                    else:
                        # 截取前面
                        front_expectedResult_cutOut = later_expectedResult_cutOut[:variable]
                        front_actualResult1_cutOut = later_actualResult1_cutOut[:variable]
                        front_result_test1_cutOut = later_result_test1_cutOut[:variable]
                        # 截取后面
                        later_expectedResult_cutOut = None
                        later_actualResult1_cutOut = later_actualResult1_cutOut[variable:]
                        later_result_test1_cutOut = later_result_test1_cutOut[variable:]
                elif expect_number <= variable and actual_number > variable and result_number <= variable:
                    if n == 1:
                        # 截取前面
                        front_expectedResult_cutOut = expectedResult
                        front_actualResult1_cutOut = actualResult[:variable]
                        front_result_test1_cutOut = result_test
                        # 截取后面
                        later_actualResult1_cutOut = actualResult[variable:]
                    else:
                        # 截取前面
                        front_expectedResult_cutOut = later_expectedResult_cutOut[:variable]
                        front_actualResult1_cutOut = later_actualResult1_cutOut[:variable]
                        front_result_test1_cutOut = later_result_test1_cutOut[:variable]
                        # 截取后面
                        later_expectedResult_cutOut = None
                        later_actualResult1_cutOut = later_actualResult1_cutOut[variable:]
                        later_result_test1_cutOut = None
                elif expect_number <= variable and actual_number <= variable and result_number > variable:
                    if n == 1:
                        # 截取前面
                        front_expectedResult_cutOut = expectedResult
                        front_actualResult1_cutOut = actualResult
                        front_result_test1_cutOut = result_test[:variable]
                        # 截取后面
                        later_result_test1_cutOut = result_test[variable:]
                    else:
                        # 截取前面
                        front_expectedResult_cutOut = later_expectedResult_cutOut[:variable]
                        front_actualResult1_cutOut = later_actualResult1_cutOut[:variable]
                        front_result_test1_cutOut = later_result_test1_cutOut[:variable]
                        # 截取后面
                        later_expectedResult_cutOut = None
                        later_actualResult1_cutOut = None
                        later_result_test1_cutOut = later_result_test1_cutOut[variable:]
                else:
                    front_expectedResult_cutOut = expectedResult
                    front_actualResult1_cutOut = actualResult
                    front_result_test1_cutOut = result_test
                    number_report_list.append(test_Interface)  # 测试接口
                    number_report_list.append(test_module)  # 测试模块
                    number_report_list.append(Check_user)  # 检查登录用户信息
                    number_report_list.append(test_point)  # 测试点
                    number_report_list.append(front_expectedResult_cutOut)  # 预期结果
                    number_report_list.append(front_actualResult1_cutOut)  # 实际结果
                    number_report_list.append(front_result_test1_cutOut)  # 测试结果
                    number_report_dicti[n] = number_report_list
                    break
                number_report_list.append(test_Interface)  # 测试接口
                number_report_list.append(test_module)  # 测试模块
                number_report_list.append(Check_user)  # 检查登录用户信息
                number_report_list.append(test_point)  # 测试点
                number_report_list.append(front_expectedResult_cutOut)  # 预期结果
                number_report_list.append(front_actualResult1_cutOut)  # 实际结果
                number_report_list.append(front_result_test1_cutOut)  # 测试结果
                number_report_dicti[n] = number_report_list
            else:
                number_report_list.append(test_Interface)  # 测试接口
                number_report_list.append(test_module)  # 测试模块
                number_report_list.append(Check_user)  # 检查登录用户信息
                number_report_list.append(test_point)  # 测试点
                if n == 1:
                    number_report_list.append(expectedResult)  # 预期结果
                    number_report_list.append(actualResult)  # 实际结果
                    number_report_list.append(result_test)  # 测试结果
                else:
                    number_report_list.append(later_expectedResult_cutOut)  # 预期结果
                    number_report_list.append(later_actualResult1_cutOut)  # 实际结果
                    number_report_list.append(later_result_test1_cutOut)  # 测试结果
                number_report_dicti[n] = number_report_list
                break
        return number_report_dicti


    @staticmethod
    def  dataType_dispose(self):
        """
        测试报告的数据类型处理，让测试报告的数据类型符合写入电子表格的类型
        :return:
        """
        """数据初始化"""
        new_introduction = [];ultimately_testReport={};list_type=None;n=1;dicti1={};dicti2={};dicti3={};number=0
        initial_list_type = EachQuantityType_transition_CharacterString(self.introduction).gain_structure_Data_type()
        """开始处理测试报告数据类型"""
        if initial_list_type=="['dict1', 'dict2', 'dict3', 'dict4', 'list5']":
            list_type=initial_list_type
            ultimately_testReport=self.introduction
        else:
            while True:
                ultimately_testReport={}
                new_introduction = []
                # 判断测试报告数据类型里有没有字典类型
                    # 去掉列表里数据类型的数字
                for duction in initial_list_type:
                    ducti=duction[:-1]
                    new_introduction.append(ducti)
                number_type=Counter(new_introduction)
                if "dict" in number_type:
                    number=Counter(new_introduction)["dict"]
                if  number==0:
                    dicti1["凑数"] = self.introduction
                    dicti2["凑数"] = dicti1
                    dicti3["凑数"] = dicti2
                    ultimately_testReport["凑数"] = dicti3
                elif number == 1:
                    dicti1["凑数"] = self.introduction
                    dicti2["凑数"] = dicti1
                    ultimately_testReport["凑数"] = dicti2
                elif number==2:
                    dicti1["凑数"] = self.introduction
                    ultimately_testReport["凑数"] = dicti1
                elif number==3:
                    ultimately_testReport["凑数"] = self.introduction
                elif number==4:
                    ultimately_testReport = self.introduction
                    list_type = initial_list_type
                    break
                elif number>=5:
                     for k, value1 in self.introduction.items():
                         for key, value in value1.items():
                             ultimately_testReport[key]=value
                self.introduction= ultimately_testReport
                initial_list_type = EachQuantityType_transition_CharacterString(ultimately_testReport).gain_structure_Data_type()
        return list_type,ultimately_testReport


    @staticmethod
    def Judge_test_results(parameter):
        """
        综合测试用例的测试结果，生成字典
        :return:
        """
        result=True; TestReportData = {}
        for para in parameter:
            #  测试结果
            result = para[0]
            # 测试报告
            testResult = para[1]
            # 生成的字典键名
            test_key = para[2]
            if result == False:
                TestReportData[test_key] = testResult
                result = False
        return result, TestReportData