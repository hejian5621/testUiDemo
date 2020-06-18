from privately_owned.method import EachQuantityType_transition_CharacterString
from Test_Report_Generate import ListDataDuplication
from utils.verification.Actual_value import WorkOrderProcess_actualValue
from commonality.database_SqlRealize import dataProcessing
from utils.verification.Expected_actual_comparison import expect_actual_dataComparison
from Test_Report_Generate import GenerateTestReport
from console_colour import Complaint_ConsolePrint
from utils.privately_owned.timeDisposal import TimeFormat
from utils.privately_owned.DataType_ParameterProcessing import DataType_processing
import random


class   dataComparison:
    """
    数据对比公共方法
    """

    def __init__(self, actualValue,expectedValue=None):
        self.annotations = actualValue
        self.expectedValue = expectedValue
        self.result = True
        self.testResultDict={}


    def ActualValue_list_repetition(self ,dicti_parameterPacket):
        """
        用户信息加上参数
        :param test_interface1:测试接口
        :param test_module: 测试模块
        :param dicti_parameterPacket: 参数集
        :return:
        """
        testResultDict =None;str_actual="测试通过";str_expect=None;str_actualValue=None;testResul = True;testReport=None;result = True
        """ 判断列表是否有重复的值"""
        if self.annotations:
            #  检查列表数据是否重复
            testResul, testReport = DataType_processing(self.annotations).ListDictionary_repetition()
            # 如果测试结果为空证明没有重复的数据
            if testResul==False:
                # 预期值
                str_expect = "列表里展示在页面的数据没有重复的"
                # 实际值，实际列表转化成字符串
                str_actualValue = EachQuantityType_transition_CharacterString(self.annotations).DataTypeConversion_console()
                # 测试结果
                str_actual = "测试不通过。重复的值：%r" % testReport
                result = False
        if result == False:
            testResultDict ={"预期结果":str_expect,"实际结果":str_actualValue,"测试结果":str_actual}
            self.result, self.testResultDict = ListDataDuplication(result,testResultDict).examine_repetition_testReport(dicti_parameterPacket)
            print("\033[1;34;40m%%%%%%%%%%%%%%%%%%%%%列表数据有重复，重复测试不通过%%%%%%%%%%%%%%%%%%%")
            print("\033[1;34;40m被测实际值：",self.annotations)
        else:
            self.testResultDict="为空"
            self.result =True
            print("\033[1;34;40m%%%%%%%%%%%%%%%%%%%%%列表数据没有重复，重复测试通过%%%%%%%%%%%%%%%%%%%%%%")
        return self.result, self.testResultDict



    def WorkOrderDetails(self,dicti_userinfo,post_Name):
        """
        工单详情页面数据对比
        :return:
        """
        JSESSIONID = dicti_userinfo["登录用户JSESSIONID"];loginName = dicti_userinfo["登录名"];roleName = dicti_userinfo["用户权限"];userid = dicti_userinfo["用户ID"]
        list_workOrderID=[];expect_withdrawn=[]
        if self.annotations:
            # 便利出实际值的所有工单ID，生成列表
            for actual in self.annotations:
                dicti_workOrder={}
                workOrderID=actual["工单ID"]
                workOrdertaskmgr = actual["任务办理"]
                dicti_workOrder={"工单ID":workOrderID,"任务办理":workOrdertaskmgr}
                list_workOrderID.append(dicti_workOrder)
            Being_dicti_workOrder = random.choice(list_workOrderID)# 随机取出工单ID列表里的一个工单
            Being_workOrderID=Being_dicti_workOrder["工单ID"];Being_workOrdertaskmgr=Being_dicti_workOrder["任务办理"];post_Parameter={"工单ID":Being_workOrderID}
            """获取工单实际值"""
            compile_workOrder ,post_Parameter,url = WorkOrderProcess_actualValue(dicti_userinfo).TheRepairSquare_sjTicketServe_details(post_Parameter)  #工单详情
            """获取工单预期值"""
            list_withdrawn_sj_ticket_serve, sql = dataProcessing("sjTicketServe_details").user_name(Being_workOrderID,"sj_ticket_serve")   # SQL根据工单ID查询工单信息
            # 时间格式转化成字符串
            list_dataKey = ["工单创建日期", "工单更新日期"]
            if list_withdrawn_sj_ticket_serve:
                str_list_workOrder = TimeFormat(list_withdrawn_sj_ticket_serve, list_dataKey).listNestDict_TimeType_str()  # 时间格式转化成字符串
                withdrawn=str_list_workOrder[0];withdrawn["任务办理"]=Being_workOrdertaskmgr
                expect_withdrawn.append(withdrawn) # 预期值里增加任务办理按钮
            else:
                list_withdrawn_sj_ticket_serve_history, sql = dataProcessing("sjTicketServe_details").user_name(Being_workOrderID,"sj_ticket_serve_history")   # SQL根据工单ID查询工单信息
                if list_withdrawn_sj_ticket_serve_history:
                    str_list_workOrder = TimeFormat(list_withdrawn_sj_ticket_serve_history,list_dataKey).listNestDict_TimeType_str()  # 时间格式转化成字符串
                    withdrawn = str_list_workOrder[0];withdrawn["任务办理"] = Being_workOrdertaskmgr
                    expect_withdrawn.append(withdrawn)  # 预期值里增加任务办理按钮
                else:
                    expect_withdrawn=None
            """实际值跟预期值对比"""
            result, dicti_testResult = expect_actual_dataComparison(expect_withdrawn,compile_workOrder).server_incident_workOrder()
            """生成测试结果"""
            userinfo_parameter ={"字典的键":"工单详情页面数据对比","所属接口":url,"所属模块":post_Name,"检查登录用户信息":"登录名：%r；权限：%r；用户ID：%r" % (
                                 loginName, roleName, userid),"测试点":"测试工单详情页面，预期值跟实际值是否一样","测试结果":"实际值不等于预期值测试失败"}
            self.result, self.testResultDict = GenerateTestReport(result,dicti_testResult).commonality_testReport_dicti(userinfo_parameter)
            PrintingParameters = {"预期值": expect_withdrawn, "实际值": compile_workOrder, "测试结果": self.result, "测试报告": self.testResultDict}
            Complaint_ConsolePrint(PrintingParameters).ProcessDivider_six("%r" % post_Name)
        else:
            self.result=True
            self.testResultDict=None
        return self.result, self.testResultDict





