#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 被测系统进行业务流程测试中，每个步骤执行完成后，进行数据检查



from utils.verification.Expected__value import addAndModification
from utils.verification.Actual_value import ComplaintsModule
from utils.verification.Process_actualValue import actual_value
from utils.verification.Expected_actual_comparison import asset_privately_dataComparison
from utils.verification.dataVerification import WorkListPage
from privately_owned.userinfo_processing import userinfo_acquire_And_Dispose
from Test_Report_Generate import GenerateTestReport
from src.utils.commonality.spreadsheet_location_And_Data import resdLocation_And_SpreadsheetData








#################新增数据校验


class addDta_checkout:
    """每个步骤所要执行的方法"""

    def __init__(self,FilterParameters):
        """
        :param FilterParameters: 需要校验的参数
        :param loginName: 登录名
        :param roleName: 用户权限
        返回测试报告
        """
        self.FilterParameters=FilterParameters
        self.report =True
        self.TestingReport={}
        self.result=True




    def add_complaint_dataCheck(self,procedure):
        """
        新增投诉后检查数据是否正常，各个权限的用户查看新增的投诉信息是否正确。
        self.FilterParameters:检查需要的参数
        :return:
        """
        """获取初始数据"""
        """检查新增的投诉信息在各个权限下的用户页面显示是否正确"""
        add_Permission = resdLocation_And_SpreadsheetData("全部权限用户账号", "小程序工单流程测试用例","列表嵌套字典").GetSpreadsheetData()  # 读取电子表格里的检查用户
        # add_Permission =[{"用户权限": "运维工程师", "用户所在单位": "四组"}]
        for add_Perm in add_Permission:
            #初始化预期值和实际值
            expectedValue = None;list_complaint=None;alone_TestingReport=None
            # 获取各登录用户信息
            list_dicti_userinfo = userinfo_acquire_And_Dispose(add_Perm).UserDetails()
            dicti_userinfo=list_dicti_userinfo[0]
            loginName=dicti_userinfo["登录名"]
            roleName = dicti_userinfo["用户权限"];  userid = dicti_userinfo["用户ID"]
            username = dicti_userinfo["用户名称"]
            # 获取实际值接口需要的参数
            post = {"日期参数": None, "筛选条件内容或者标题": self.FilterParameters["投诉标题"]}
            post_Parameter = dict(dicti_userinfo, **post)  # 获取检查需要的参数
            # 获取实际值
            list_complaint,url=ComplaintsModule(post_Parameter).inquire_complaint_page() # 根据接口获取实际值
            actualValue = actual_value(list_complaint).add_Complaints_DateProcessing() # 处理实际值（时间格式）
            # 获取预期值
            expectedValue = addAndModification(self.FilterParameters).add_complaint_jurisdiction_Permission(post_Parameter)
            # 实际值跟预期值对比
            """预计值跟实际值对比；预期值必须等于实际值"""
            result, str_consequence = asset_privately_dataComparison(expectedValue,actualValue).add_jurisdiction_equality()
            """生成测试结果"""
            result,alone_TestingReport = GenerateTestReport(result,str_consequence).commonality_testReport_dicti(self.FilterParameters)
            print("\033[1;34;40m******%r后检查用登录用户信息，登录名：%r；用户权限：%r；用户ID：%r；用户名称：%r*****"%(procedure,loginName, roleName, userid,username))
            print("\033[1;34;40m%r说明：预期值必须等于实际值；预期值：\033[0m\033[4;35;40m%r"%(procedure,expectedValue))
            print("\033[1;34;40m%r说明：预期值必须等于实际值；实际值：\033[0m\033[4;35;40m%r"%(procedure, actualValue))
            print("\033[1;34;40m%r是否通过：\033[0m\033[4;35;40m%r"%(procedure,result))
            print("\033[1;34;40m%r测试报告：\033[0m\033[4;35;40m%r"%(procedure,alone_TestingReport))
            if result == False:
                self.TestingReport[loginName] = alone_TestingReport
                self.result =False
            print("")
        return self.result,self.TestingReport



    def add_workOrder_dataCheck(self,procedure):
        """
        新增工单后检查数据是否正常，各个权限的用户查看新增的投诉信息是否正确。
        :param procedure:流程步骤
        :return:
        """
        n=1;add_Permission=None
        """获取检查用户信息"""
        if procedure == "服务台(一号)-已挂起-改派-工程师(五组)" or procedure == "工程师(五组)-处理中-完成工单" or procedure == "工程师（五组）-预约中-到达现场" or \
           procedure == "工程师(五组)-预约中-申请挂起" or procedure == "工程师(五组)-处理中-申请挂起" or procedure == "组长(五组)-处理中-审核挂起-不通过":
            add_Permission = resdLocation_And_SpreadsheetData("全部权限用户账号（五组）", "小程序工单流程测试用例","列表嵌套字典").GetSpreadsheetData()  # 读取电子表格里的检查用户
        else:
            add_Permission = resdLocation_And_SpreadsheetData("全部权限用户账号（四组）", "小程序工单流程测试用例","列表嵌套字典").GetSpreadsheetData()  # 读取电子表格里的检查用户
        #########################################
        for add_Perm in add_Permission:
            list_CheckModule=None
            list_dicti_userinfo = userinfo_acquire_And_Dispose(add_Perm).UserDetails();dicti_userinfo = list_dicti_userinfo[0] # 获取各登录用户信息
            parameterPacket = dict( list_dicti_userinfo, **self.FilterParameters)  # 合并需要检查的登录用户和参数包
            # 从电子表格中取出相对应权限用户，需要检查的模块
            list_list_Excel = resdLocation_And_SpreadsheetData("权限检查对应模块", "小程序工单流程测试用例","列表嵌套列表").GetSpreadsheetData()  # 读取电子表格里的被测页面
            for list_Excel in list_list_Excel: #循环取出列表嵌套列表
                if list_Excel[0] == dicti_userinfo["用户权限"]:
                    del list_Excel[0]
                    list_CheckModule=list_Excel
                    break
            ####################################
            for CheckModule in list_CheckModule: # 取出需要检查的单个模块
                fragment_result=None;fragment_testResult=None;n =n + 1 ;CheckModule1=None
                fragment_result,fragment_testResult = WorkListPage(parameterPacket).clientSide_repairsPlaza_my(CheckModule,procedure) # 新增工单或者修改后，检查各个工单页面数据
                if fragment_result == False: # 获取测试结果和报告
                    n = n+1
                    self.TestingReport[n] = fragment_testResult
                    self.result = False
        return self.result, self.TestingReport




















