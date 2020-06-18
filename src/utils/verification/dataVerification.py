from Test_Report_Generate import WorkOrderProcess_testReport
from utils.verification.Expected_actual_comparison import asset_privately_dataComparison
from utils.verification.Actual_value import WorkOrderProcess_actualValue
from utils.verification.Expected__value import WorkOrderProcess_expectedValue


# 获取预期值和实时值，实际跟预期对比，返回测试结果



class WorkListPage:
    """工单页面"""

    def __init__(self,FilterParameters):
        self.FilterParameters=FilterParameters


    def clientSide_repairsPlaza_my(self,CheckModule,procedure):
        """
        新增工单或者修改后，检查各个工单页面数据
        :return:
        """
        result=True;alone_TestingReport=None;list_expectedValue=None;new_list_actualValue=[];list_actualValue=None;Contrast = "0"
        str_consequence=None;post_Parameter=None;ExpectationsThat=None
        # 获取用户信息
        JSESSIONID = self.FilterParameters["登录用户JSESSIONID"];loginName = self.FilterParameters["登录名"]
        roleName = self.FilterParameters["用户权限"];userid = self.FilterParameters["用户ID"];username = self.FilterParameters["用户名称"]
        self.FilterParameters["所属模块"]=CheckModule
        """获取实际值"""
        if   CheckModule =="客户端--报修广场--我的报修":
            list_actualValue,post_Parameter,url = WorkOrderProcess_actualValue(self.FilterParameters).TheRepairSquare_page()
        elif CheckModule =="客户端--报修广场--内部":
            list_actualValue,post_Parameter,url = WorkOrderProcess_actualValue(self.FilterParameters).TheRepairSquare_InsideRepairListData()
        elif CheckModule == "客户端--报修广场--外协":
            list_actualValue,post_Parameter,url = WorkOrderProcess_actualValue(self.FilterParameters).TheRepairSquare_ExternalRepairListData()
        elif CheckModule == "小程序--首页":
            list_actualValue,post_Parameter,url = WorkOrderProcess_actualValue(self.FilterParameters).TheRepairSquare_noOffTicketListData()
        elif CheckModule == "客户端-报修广场-已完成" or CheckModule == "客户端-报修广场-全部" or CheckModule == "小程序--紧急报修" or CheckModule == "小程序--驻场服务" :
            list_actualValue,post_Parameter = WorkOrderProcess_actualValue(self.FilterParameters).TheRepairSquare_allListData()
            # list_workOrder_strState=[]
            # # 把工单整数类型的工单状态编译成状态名称
            # for workOrder in list_actualValue:
            #     int_state = workOrder["工单状态"]
            #     state_name = IndependentMethod.ADictionaryTable(JSESSIONID, int_state)  # 整数的工单状态转化成str工单名称
            #     workOrder["工单状态"] = state_name
            #     list_workOrder_strState.append(workOrder)
            # # 截取工单更新日期和创建日期的日期
            # list_dataKey = ["工单创建日期", "工单更新日期"]
            # list_workOrder = transform_dataType(list_workOrder_strState, list_dataKey).CaptureTheAate("%Y-%m-%d")
        elif CheckModule == "服务端--事件--待响应" or CheckModule == "服务端--事件--预约中" or CheckModule == "服务端--事件--待处理" or CheckModule == "服务端--事件--处理中"  \
                or CheckModule == "服务端--事件--已处理"  or CheckModule == "服务端--事件--已挂起":
            list_actualValue,post_Parameter = WorkOrderProcess_actualValue(self.FilterParameters).TheRepairSquare_chooseListData()
        elif CheckModule == "服务端--事件--已关单":
            list_actualValue, post_Parameter = WorkOrderProcess_actualValue(self.FilterParameters).TheRepairSquare_closedTicketListData()
        """获取预期值"""
        # 生成预期值
        list_expectedValue,ExpectationsThat = WorkOrderProcess_expectedValue(self.FilterParameters).clientSide_repairsPlazaMy_expected(CheckModule,procedure)
        """预计值跟实际值对比"""
        result, str_consequence = asset_privately_dataComparison(list_expectedValue,list_actualValue).add_jurisdiction_include(ExpectationsThat)
        """生成测试结果"""
        result, alone_TestingReport = WorkOrderProcess_testReport(result, str_consequence).clientSide_MyService(loginName,CheckModule,procedure)
        """打印参数和测试结果"""
        print("\033[5;30;44m进行“%r”步骤操作，所检查模块：“%r”；登录名：%r；用户权限：%r；用户ID：%r；用户名称：%r*****" % (
        procedure,CheckModule, loginName, roleName, userid, username))
        print("\033[1;34;40m%r检查所用生成预期值参数：\033[0m\033[4;35;40m%r" % (procedure, self.FilterParameters))
        print("\033[1;34;40m%r检查所用获取实际值post参数：\033[0m\033[4;35;40m%r" % (procedure, post_Parameter))
        print("\033[1;34;40m%r说明：%r；预期值：\033[0m\033[4;35;40m%r" % (procedure,ExpectationsThat, list_expectedValue))
        print("\033[1;34;40m%r说明：%r；实际值：\033[0m\033[4;35;40m%r" % (procedure,ExpectationsThat, list_actualValue))
        print("\033[1;34;40m%r是否通过：\033[0m\033[4;35;40m%r" % (procedure, result))
        print("\033[1;34;40m%r测试报告：\033[0m\033[4;35;40m%r" % (procedure, str_consequence))
        print("")
        return result, alone_TestingReport







