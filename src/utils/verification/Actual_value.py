#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 接口实际值处理（返回编译过的实际值）


from assertpy import assert_that
from privately_owned.Port_Compile import OtherInterfaces_compile,workOrder_compile,\
    equipmentSchedule,StatisticsOfRepairQuantity,ListOfComplaints
from appletConnector import initialize,TheRepairOrderInterface,assets_management,rests, addKind,SystemAppController
from appletConnector import UserAppController
from privately_owned.method import transform_dataType
from privately_owned.Task_handling_button import IndependentMethod
from privately_owned.dicti_data_dispose import dictionaries
from utils.privately_owned.timeDisposal import TimeFormat



############接口实际处理（返回实际值）###################################

class repairs_workOrder:
    """报修工单模块实际值"""

    def __init__(self, JSESSIONID, post_Parameter):
        """
        :param JSESSIONID:
        :param post_Parameter: 接口要传入的post参数
        """
        self.JSESSIONID = JSESSIONID
        self.post_Parameter = post_Parameter
        self.compile_actualValue = None



    def applet_EventModules(self,state_name,userinfo):
        """
        小程序事件模块实际值
        :return:
        """
        url=None
        post_Parameter={};finish_date2=None;list_workOrder_strState=[];list_workOrder=None
        for key, value in self.post_Parameter.items():
            post_Parameter[key]=value
        # 去掉开始日期和结束日期的时间
        begin_date=post_Parameter["开始日期"]
        if begin_date:
            begin_date=begin_date[:10]
        finish_date1 = post_Parameter["结束日期"]
        if finish_date1:
            finish_date2 = finish_date1[:10]
        post_Parameter["开始日期"]=begin_date
        post_Parameter["结束日期"] = finish_date2
        list_workOrder_initial=None
        #获取待响应/预约中/待处理/处理中/已处理/已挂起列表数据接口的数据,小程序事件，返回工单列表
        if state_name == "外协_待响应" or state_name == "外协_预约中" or state_name == "外协_待处理" or state_name == "外协_处理中" or state_name == "外协_已处理" or state_name == "外协_已挂起":
            list_workOrder_initial,req_text,url = TheRepairOrderInterface(self.JSESSIONID, post_Parameter).chooseListData()
        #获取外协_已关单列表数据接口的数据,小程序事件，返回工单列表
        elif state_name == "外协_已关单":
            list_workOrder_initial,req_text,url = TheRepairOrderInterface(self.JSESSIONID,post_Parameter).closedTicketListData()
        #获取全部工单、紧急事件、驻场事件（包含已关单数据）列表数据接口的数据,小程序事件，返回工单列表
        elif state_name == "全部工单":
            post_Parameter["是否完成的工单"] = None
            list_workOrder_initial,url = TheRepairOrderInterface(self.JSESSIONID,post_Parameter).allListData()
        list_workOrder_intState = workOrder_compile(self.JSESSIONID, list_workOrder_initial).compile_homePage(userinfo )
        # 把工单整数类型的工单状态编译成状态名称
        for workOrder in list_workOrder_intState:
            int_state=workOrder["工单状态"]
            state_name = dictionaries(self.JSESSIONID, int_state).ADictionaryTable()  # 整数的工单状态转化成str工单名称
            workOrder["工单状态"]=state_name
            list_workOrder_strState.append( workOrder)
        # 截取工单更新日期和创建日期的日期
        list_dataKey = ["工单创建日期", "工单更新日期"]
        list_workOrder = TimeFormat(list_workOrder_strState, list_dataKey).CaptureTheAate("%Y-%m-%d")
        return list_workOrder,url




class ReportStatistics_class :
    """报修统计模块数据对比测试实际值"""

    def __init__(self, dicti_parameterPacket):
        """
        :param dicti_parameterPacket: 接口要传入的post参数
        """
        self.dicti_parameterPacket = dicti_parameterPacket



    def inquire_ReportStatistics(self, module):
        """
        报修统计页面（报修数据统计、故障类型统计）
        :return:
        """
        deviceList=None;list_office=None;begin_date=None;finish_date=None;deviceList=None;url=None;list_workOrder_compile=None;test_module=None
        new_workOrder_compile=[]
        list_office=self.dicti_parameterPacket["所选单位ID"];begin_date=self.dicti_parameterPacket["开始日期"];finish_date=self.dicti_parameterPacket["结束日期"]
        JSESSIONID = self.dicti_parameterPacket["登录用户JSESSIONID"]
        if module == "报修数量":
            deviceList,url = rests(JSESSIONID).numCountData(list_office, begin_date, finish_date)
            test_module="客户端-首页-报修统计（除普通用户外）-报修数量统计；服务端-报修统计-报修数量统计；"
            # deviceList=[{'cuser': {'office': {'id': 'e155a7d8e34f4e339d5207ab33e2add4', 'name': '生物城第一高级中学分校', 'hasChildren': False, 'type': '2', 'parentId': '0'},
            #                        'loginFlag': '1', 'roleNames': '', 'admin': False}, 'officeCountNum': '208', 'handleTaskFlag': False, 'histroryFlag': False}]
        elif module == "故障数量":
            deviceList,url = rests(JSESSIONID).faultCountData(list_office, begin_date, finish_date)
            test_module = "客户端-首页-报修统计（除普通用户外）-故障类型统计；服务端-报修统计-故障类型统计；"
            # deviceList =[{'prbTp': {'id': '3c1fa83ea73e46aa8b0745ea6e424f0c', 'prbTpNm': '教学功能室设备'}, 'prbTpTypeNum': '52', 'handleTaskFlag': False, 'histroryFlag': False, 'customSort': 0},
            #              {'prbTp': {'id': '0756e6cf572a4ecf82074b84fb298182', 'prbTpNm': '电脑故障'}, 'prbTpTypeNum': '33', 'handleTaskFlag': False, 'histroryFlag': False, 'customSort': 0},
            #              {'prbTp': {'id': 'fc5478163a6749f78300dbc6801d99ed', 'prbTpNm': '摄像头'}, 'prbTpTypeNum': '33', 'handleTaskFlag': False, 'histroryFlag': False, 'customSort': 0},
            #              {'prbTp': {'id': 'c5c08f65faf049778e391588565d5ad4', 'prbTpNm': '电子教学设备'}, 'prbTpTypeNum': '27', 'handleTaskFlag': False, 'histroryFlag': False, 'customSort': 0},
            #              {'prbTp': {'id': '7370317620c443cfbe717945ec59771c', 'prbTpNm': '其他设备'}, 'prbTpTypeNum': '14', 'handleTaskFlag': False, 'histroryFlag': False, 'customSort': 0},
            #              {'prbTp': {'id': 'e0f6567f1d9c4db3b114fd54f89523a4', 'prbTpNm': '网络设备'}, 'prbTpTypeNum': '14', 'handleTaskFlag': False, 'histroryFlag': False, 'customSort': 0},
            #              {'prbTp': {'id': '802a6a7a1dbb4bc389cb46f1b54980e1', 'prbTpNm': '办公设备'}, 'prbTpTypeNum': '14', 'handleTaskFlag': False, 'histroryFlag': False, 'customSort': 0},
            #              {'prbTp': {'id': 'bc860ff03eb54441954b1a794e835a8c', 'prbTpNm': '监控设备'}, 'prbTpTypeNum': '9', 'handleTaskFlag': False, 'histroryFlag': False, 'customSort': 0},
            #              {'prbTp': {'id': '5851adfeb3fd469aac7c60ec17545061', 'prbTpNm': '广播设备'}, 'prbTpTypeNum': '6', 'handleTaskFlag': False, 'histroryFlag': False, 'customSort': 0},
            #              {'prbTp': {'id': 'f65b0b91ae074eecb330dabb994653dd', 'prbTpNm': '打印设备'}, 'prbTpTypeNum': '6', 'handleTaskFlag': False, 'histroryFlag': False, 'customSort': 0}]
            # 编译接口返回的数据
        list_workOrder_compile = StatisticsOfRepairQuantity(JSESSIONID, deviceList).ReportStatistics(module)
        for workOrder_compile in list_workOrder_compile: # 把字符串的工单数转化成整数
            workOrder_number=int(workOrder_compile["工单数"])
            workOrder_compile["工单数"]=workOrder_number
            new_workOrder_compile.append(workOrder_compile)
        return  new_workOrder_compile,url, test_module



class AssetsOfEquipment_actualValue:
    """资产设备模块实际值"""

    def __init__(self,dicti_parameterPacket):
        """
        :param JSESSIONID:
        :param post_Parameter: 接口要传入的post参数
        """
        self.dicti_parameterPacket = dicti_parameterPacket
        self.compile_actualValue=None


    def equipmentSchedule(self):
        """
        设备清单页面实际值
        :return:
        """
        deviceList = None;url = None;list_workOrder_compile = None;str_officeID=None
        str_officeID= self.dicti_parameterPacket["所选单位ID"]
        devicename = self.dicti_parameterPacket["设备名称"]
        batchNo = self.dicti_parameterPacket["批次"]
        JSESSIONID = self.dicti_parameterPacket["登录用户JSESSIONID"]
        post_Parameter = {"单位ID": str_officeID, "设备名称": devicename, "批次": batchNo}
        """获取接口数据"""
        deviceList,url = assets_management(JSESSIONID,post_Parameter).equipListData()
        """编译接口数据"""
        list_workOrder_compile = equipmentSchedule(JSESSIONID, deviceList).compile_equipmentSchedule()
        # list_workOrder_compile=[{'设备名称': '硬盘dddddddddddddddddddddddddd', '跟新时间': '2019-08-09 10:32:12', '创建时间': '2019-08-01 13:52:21',
        #                          '批次': '202008014560024', '设备品牌': '戴尔1', '设备状态': '1', '位置信息': 'e70aeecc0eab411dbc20214b98ee3807',
        #                          '设备类型ID': '090ccfed6c0e49c9a097dba47ab069b7', '设备ID': 'd8b86fbe8f3840a389c7671e6228eaea', '设备编号': '878637654536355840.jpg'}]
        return list_workOrder_compile,url




class  ComplaintsModule:
    """投诉模块实际值"""

    def __init__(self,dicti_parameterPacket):
        """
        :param dicti_parameterPacket:参数包
        """
        self.dicti_parameterPacket = dicti_parameterPacket
        self.compile_actualValue=None



    def add_ComplaintsModule(self):
        """
        新增投诉接口
        :return:
        """
        loginName = self.dicti_parameterPacket["登录名"] ; roleName = self.dicti_parameterPacket["用户权限"]
        JSESSIONID =self.dicti_parameterPacket["登录用户JSESSIONID"] ;complaint_Title =self.dicti_parameterPacket["投诉标题"]
        complaint_phone = self.dicti_parameterPacket["用户联系电话"] ;complaint_content = self.dicti_parameterPacket["投诉内容"]
        post_Parameter={"投诉标题":complaint_Title,"投诉人电话":complaint_phone,"投诉内容":complaint_content}
        # 调用新增投诉接口
        InterfaceReturnValue,url = addKind(JSESSIONID).add_manualOperation_complain(post_Parameter)
        # 断言返回值
        assert_that(InterfaceReturnValue).described_as('新增投诉失败').is_equal_to("投诉成功，已通知服务台处理")
        print("\033[0;37;40m登录用户：%r，用户权限：%r,新增投诉成功,已通知服务台处理"%(loginName,roleName))
        return url


    def amend_ComplaintsModule(self,procedure):
        """
        投诉模块数据修改
        :param procedure:
        :return:
        """
        JSESSIONID=self.dicti_parameterPacket["登录用户JSESSIONID"]; post_Parameter=None
        if procedure == "服务台受理投诉，指派被投诉人：运维工程师（四组）" or procedure == "服务台受理投诉，指派被投诉人：运维组长（四组）":
            post_Parameter = {"投诉标题": self.dicti_parameterPacket["投诉标题"], "投诉人电话": self.dicti_parameterPacket["投诉人电话"],"投诉内容": self.dicti_parameterPacket["投诉内容"],
                              "投诉级别": self.dicti_parameterPacket["投诉级别"],"处理方案": self.dicti_parameterPacket["处理方案"],
                              "投诉单ID": self.dicti_parameterPacket["投诉单ID"],"被投诉人ID": self.dicti_parameterPacket["被投诉人ID"],
                              "处理结果":None,"操作": self.dicti_parameterPacket["操作"]}
        elif procedure == "运维工程师填写处理结果" or procedure == "运维组长填写处理结果" or procedure == "运维工程师修改处理结果" or procedure == "运维组长修改处理结果":
            post_Parameter =  {"投诉单ID": self.dicti_parameterPacket["投诉单ID"],"处理结果":self.dicti_parameterPacket["处理结果"],"操作": self.dicti_parameterPacket["操作"]}
        elif procedure == "服务台再次受理投诉，指派被投诉人：运维工程师（四组）" or procedure == "服务台再次受理投诉，指派被投诉人：运维组长（四组）":
            post_Parameter =  {"投诉单ID": self.dicti_parameterPacket["投诉单ID"],"被投诉人ID": self.dicti_parameterPacket["被投诉人ID"],"处理方案": self.dicti_parameterPacket["处理方案"],
                              "操作": self.dicti_parameterPacket["操作"]}
        elif procedure == "普通用户确认处理结果：未解决" or procedure == "用户管理员确认处理结果：未解决":
            post_Parameter =  {"投诉单ID": self.dicti_parameterPacket["投诉单ID"],"操作": self.dicti_parameterPacket["操作"]}
        elif procedure == "普通用户再次确认处理结果：已解决" or procedure == "用户管理员确认处理结果：已解决":
            post_Parameter =  {"投诉单ID": self.dicti_parameterPacket["投诉单ID"],"操作": self.dicti_parameterPacket["操作"]}
        # 修改投诉信息数据接口
        InterfaceReturnValue,url = addKind(JSESSIONID).add_manualOperation_updatesuggest(post_Parameter)
        if procedure =="服务台受理投诉，指派被投诉人：运维工程师（四组）" or procedure =="服务台受理投诉，指派被投诉人：运维组长（四组）" or procedure =="服务台再次受理投诉，指派被投诉人：运维工程师（四组）":
            assert_that(InterfaceReturnValue).described_as('服务台受理投诉，并且填写处理意见不成功').is_equal_to("填写处理意见成功，已通知工程师")
        elif procedure =="运维工程师修改处理结果" or procedure =="运维工程师填写处理结果" or procedure =="运维组长填写处理结果":
            assert_that(InterfaceReturnValue).described_as('运维工程师（运维组长），填写处理结果不成功').is_equal_to("填写处理结果成功，已通知客户确认")
        return url


    def  inquire_complaint_page(self):
        """
        投诉页面数据查询接口，返回编译过的数据
        :return:
        """
        JSESSIONID=self.dicti_parameterPacket["登录用户JSESSIONID"] ; monthNum=self.dicti_parameterPacket["日期参数"]
        titleAndcontent = self.dicti_parameterPacket["筛选条件内容或者标题"]
        post_Parameter ={"日期范围":monthNum,"筛选条件内容或者标题":titleAndcontent}
        # 调用投诉清单接口
        list_ListOfComplaints,url = rests(JSESSIONID).Complaint_list_page(post_Parameter)
        ##############################################################################################################
        """编译从接口投诉清单返回的数据"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        list_workOrder_compile = ListOfComplaints(list_ListOfComplaints).compile_TheComplaintpage()
        return list_workOrder_compile,url


class WorkOrderProcess_actualValue:
    """工单流程，调接口获取返回值，并编译返回值"""

    def __init__(self, FilterParameters,post_Parameter=None):
        """
        :param JSESSIONID:
        :param post_Parameter: 接口要传入的post参数
        """
        self.FilterParameters=FilterParameters
        self.post_Parameter = post_Parameter
        self.compile_actualValue = None


    def WorkOrderList_actualValue_console(self,connector):
        """
        工单清单页面数据对比实际值控制台
        :return:
        """
        list_actualValue=None; post_Parameter=None; url=None
        if connector=="小程序首页工单":
            list_actualValue, post_Parameter, url = WorkOrderProcess_actualValue(self.FilterParameters).TheRepairSquare_noOffTicketListData()  # 小程序首页工单
        elif connector=="内部代办理工单":
            officeID = self.FilterParameters["所选单位ID"]
            list_actualValue, post_Parameter, url = WorkOrderProcess_actualValue(self.FilterParameters).TheRepairSquare_InsideRepairListData(True,officeID) # 内部代办理工单
        elif connector=="用户管理员区域管理员外协报修列表数据":
            officeID = self.FilterParameters["所选单位ID"]
            list_actualValue, post_Parameter, url = WorkOrderProcess_actualValue(self.FilterParameters).TheRepairSquare_ExternalRepairListData(officeID) # 用户管理员区域管理员外协报修列表数据
        elif connector=="外部用户-我的报修":
            list_actualValue, post_Parameter, url = WorkOrderProcess_actualValue(self.FilterParameters).TheRepairSquare_page( ) # 外部用户-我的报修
        elif connector=="全部工单、紧急事件、驻场事件（包含已关单数据）":
            list_actualValue, post_Parameter, url = WorkOrderProcess_actualValue(self.FilterParameters).TheRepairSquare_allListData( ) # 全部工单、紧急事件、驻场事件（包含已关单数据）
        elif connector == "外协未关单工单列表页面":
            list_actualValue, post_Parameter, url = WorkOrderProcess_actualValue(self.FilterParameters).TheRepairSquare_chooseListData()  # 外协未关单工单列表页面
        elif connector == "已关单列表数据":
            list_actualValue, post_Parameter, url = WorkOrderProcess_actualValue(self.FilterParameters).TheRepairSquare_closedTicketListData()  # 已关单列表数据
        return list_actualValue, post_Parameter, url


    def add_workOrder(self,procedure):
        """
       一键报修接口，并编译返回值
       :return:
       """
        InterfaceReturnValue=None
        JSESSIONID = self.FilterParameters["登录用户JSESSIONID"]
        post_Parameter={"工单标题":self.FilterParameters["工单标题"], "故障类型ID":self.FilterParameters["故障类型ID"],"工单报修描述":self.FilterParameters["工单报修描述"],
                        "预约日期":self.FilterParameters["预约日期"], "预约时间段":self.FilterParameters["预约时间段"],"资产设备id":self.FilterParameters["资产设备id"],
                        "工单服务类型":self.FilterParameters["工单服务类型"]}
        # 调用新增工单接口
        if procedure == "普通用户-一键报修":
            InterfaceReturnValue = initialize(JSESSIONID).AKeyRepairService(post_Parameter)
        elif procedure == "服务台-PC端-报修工单":
            pass
        # 断言返回值
        assert_that(InterfaceReturnValue).described_as('2/新增工单失败').is_equal_to("提交成功，请等待信息中心管理员进行处理！")
        print("")


    def amend_sjTicketOperating_sjTicketOperating(self,Subordinate_procedure):
        """
         操作按钮获取表单流程，做除了一件报修以外的所有操作，都要先调一下
       接单/改派/改派审核/到达现场/挂起/挂起审核/解挂/完成工单/评价接口
        :param Subordinate_procedure: 工单操作步骤名称
        :param loginName:
        :param roleName:
        :return:
        """
        InterfaceReturnValue=None; positional="操作成功"; JSESSIONID = self.FilterParameters["登录用户JSESSIONID"]
        # 获取接单/改派/改派审核/到达现场/挂起/挂起审核/解挂/完成工单/评价接口post参数
        sjTicketOperating_post={"工单ID":self.FilterParameters["工单ID"],"工单编号":self.FilterParameters["工单编号"],"工单报修人ID":self.FilterParameters["工单报修人ID"],"工单状态":self.FilterParameters["工单状态"],
                                "工单改派人ID":self.FilterParameters["工单改派人ID"],"工单处理人ID":self.FilterParameters["工单处理人ID"],"流程实例id":self.FilterParameters["流程实例id"],"报修人电话":self.FilterParameters["报修人电话"],
                                "预约开始时间":self.FilterParameters["预约开始时间"],"预约结束时间":self.FilterParameters["预约结束时间"],"确认开始服务时间":self.FilterParameters["确认开始服务时间"],"确认结束服务时间":self.FilterParameters["确认结束服务时间"],
                                "工单范围":self.FilterParameters["工单范围"],"任务名称":self.FilterParameters["任务名称"],"任务定义Key":self.FilterParameters["任务定义Key"],"意见状态":self.FilterParameters["意见状态"],
                                "工单服务类型":self.FilterParameters["工单服务类型"],"任务意见":self.FilterParameters["任务意见"],"事件解决方案":self.FilterParameters["事件解决方案"],"预约时间段":self.FilterParameters["预约时间段"],
                                "内部处理结果":self.FilterParameters["内部处理结果"],"评级":self.FilterParameters["评级"],"用户评价":self.FilterParameters["用户评价"],"挂起下拉框理由":self.FilterParameters["挂起下拉框理由"],
                                "挂起状态字段":self.FilterParameters["挂起状态字段"],"改派人群组ID":self.FilterParameters["改派人群组ID"]}
        # 调用关于工作流的接口接口
        sjTicketFlow_post ={"任务id":self.FilterParameters["任务id"],"任务名称":self.FilterParameters["任务名称"],"任务定义Key":self.FilterParameters["任务定义Key"],"流程实例id":self.FilterParameters["流程实例id"],
                            "流程定义id":self.FilterParameters["流程定义id"],"任务状态":self.FilterParameters["任务状态"],"处理类型":self.FilterParameters["处理类型"]}
        # 当运维组长改派待响应状态下的工单时，系统会获取改派人的位置信息
        if  Subordinate_procedure =="组长(四组)-待响应-改派-工程师(四组)" or Subordinate_procedure =="服务台(一号)-已挂起-改派-工程师(四组)" or Subordinate_procedure =="服务台-已挂起-改派-五组-运维工程师":
            changeTicketPosition_post={"工单ID":self.FilterParameters["工单ID"],"工单改派人ID":self.FilterParameters["工单改派人ID"]}
            positional,req_text = SystemAppController(JSESSIONID, changeTicketPosition_post).changeTicketPosition()
        # 调用“操作按钮获取表单流程”接口
        operating = TheRepairOrderInterface(JSESSIONID, sjTicketFlow_post).sjTicketFlow()
        if operating=="操作成功" and positional=="操作成功":
            # 调用接单/改派/改派审核/到达现场/挂起/挂起审核/解挂/完成工单/评价接口
            InterfaceReturnValue = TheRepairOrderInterface(JSESSIONID, sjTicketOperating_post).sjTicketOperating()
        else:
            print("操作按钮获取表单流程接口：",operating);print("改派更新位置接口：", operating)
        # 断言返回值
        assert_that(InterfaceReturnValue).described_as("“%r”操作，调用sjTicketOperating接口操作失败"%procedure).is_equal_to("操作成功")
        print("\033[1;34;40m操作按钮获取表单流程，操作成功；\033[0m\033[4;35;40m登录用户：%r，用户权限：%r" % (loginName, roleName))
        print("")






    def  TheRepairSquare_page(self):
        """
        报修广场数据查询接口,调用小程序--客户端--报修广场--我的报修接口，返回编译过的数据
        :return:
        """
        JSESSIONID = self.FilterParameters["登录用户JSESSIONID"]
        startDate = self.FilterParameters["开始日期"];endingDate = self.FilterParameters["结束日期"]
        post_Parameter = {"开始日期": startDate, "结束日期": endingDate}
        # 调用小程序--客户端--报修广场--我的报修接口
        list_ListWorkOrder,url = TheRepairOrderInterface(JSESSIONID,post_Parameter).MyRepairListData()
        ##############################################################################################################
        """编译从接口投诉清单返回的数据"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        list_workOrder = workOrder_compile(list_ListWorkOrder).WorkOrderProcess_MyRepairListData(self.FilterParameters)
        return list_workOrder,post_Parameter,url



    def TheRepairSquare_InsideRepairListData(self,effect=True,location_office=None):
        """
        报修广场--内部--数据查询接口，返回编译过的数据
        :return:
        """
        list_workOrder=None;JSESSIONID = self.FilterParameters["登录用户JSESSIONID"]
        startDate = self.FilterParameters["开始日期"]
        if type(startDate)==type(["1"]):
            startDate=startDate[0]
        endingDate = self.FilterParameters["结束日期"]
        if type(endingDate)==type(["1"]):
            endingDate=endingDate[0]
        post_Parameter = {"开始日期": startDate, "结束日期": endingDate,"所在单位":location_office}
        # 调用小程序--客户端--报修广场--内部
        list_ListWorkOrder,req_text,url = TheRepairOrderInterface(JSESSIONID, post_Parameter).InsideRepairListData()
        ##############################################################################################################
        """编译从接口投诉清单返回的数据"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        # "1":数据对比用户；
        if effect:
            list_workOrder = workOrder_compile(list_ListWorkOrder).WorkOrderProcess_InsideRepairListData(self.FilterParameters)
        # "1":获取部分post请求数据
        else:
            list_workOrder = OtherInterfaces_compile(list_ListWorkOrder).WorkOrderProcess_Post(self.FilterParameters,req_text)
        return list_workOrder,post_Parameter,url


    def TheRepairSquare_ExternalRepairListData(self,office_id=None):
        """
        报修广场--外协--数据查询接口，返回编译过的数据
        :return:
        """
        list_workOrder = None
        JSESSIONID = self.FilterParameters["登录用户JSESSIONID"]
        startDate = self.FilterParameters["开始日期"]
        if type(startDate) == type(["1"]):
            startDate = startDate[0]
        endingDate = self.FilterParameters["结束日期"]
        if type(endingDate) == type(["1"]):
            endingDate = endingDate[0]
        post_Parameter = {"开始日期": startDate, "结束日期": endingDate, "所在单位": office_id}
        # 调用小程序--客户端--报修广场--外协接口
        list_ListWorkOrder,url = TheRepairOrderInterface(JSESSIONID,  post_Parameter).ExternalRepairListData()
        ##############################################################################################################
        """编译从接口投诉清单返回的数据"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        list_workOrder = workOrder_compile(list_ListWorkOrder).WorkOrderProcess_ExternalRepairListData(self.FilterParameters)
        return list_workOrder,post_Parameter,url


    def TheRepairSquare_noOffTicketListData(self):
        """
        小程序--首页--工单
        :return:
        """
        JSESSIONID = self.FilterParameters["登录用户JSESSIONID"]
        list_workOrder_port=None;list_workOrder=None
        roleName = self.FilterParameters["用户权限"]
        if  roleName == "普通用户" or roleName == "用户管理员" or roleName == "区域管理员":
            post_Parameter={"工单范围":None,"月份":"7"}
        else:
            post_Parameter = {"工单范围":"0","月份":"6"}
        # 调用小程序--首页--工单接口
        list_workOrder_port,url = TheRepairOrderInterface(JSESSIONID, post_Parameter).noOffTicketListData()
        ##############################################################################################################
        """编译从接口工单清单返回的数据"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        list_workOrder = workOrder_compile( list_workOrder_port).compile_homePage(self.FilterParameters) # 编译调用小程序--首页--工单接口
        return list_workOrder,post_Parameter,url



    def TheRepairSquare_allListData(self,effect=True):
        """
        小程序--客户端-报修广场-已完成和全部；小程序--服务端-事件-全部工单列表实际值；小程序--服务端--首页--紧急报修和驻场服务实际值
        :return:
        """
        post_Parameter={};list_workOrder=None;list_ListWorkOrder=None;list_workOrder_intState=None;list_workOrder_strState=[]
        selected_office=None;selected_module=None;startDate=None;endingDate=None
        print("self.FilterParameters:",self.FilterParameters)
        startDate = self.FilterParameters["开始日期"];endingDate = self.FilterParameters["结束日期"]; JSESSIONID = self.FilterParameters["登录用户JSESSIONID"]
        selected_module=self.FilterParameters["所属模块"];selected_office=self.FilterParameters["所选单位"]
        if selected_office=="空":
            selected_office=None
        if selected_module == "客户端-报修广场-已完成":
            post_Parameter={"工单类型":None,"开始日期":startDate,"结束日期":endingDate,"所选单位":selected_office,"工单范围":None,"是否完成的工单":"true","工单服务类型":None}
        elif selected_module == "客户端-报修广场-全部":
            post_Parameter = {"工单类型": None, "开始日期":startDate,"结束日期":endingDate,"所选单位":selected_office,"工单范围":None,"是否完成的工单":None,"工单服务类型":None}
        elif selected_module =="首页-紧急报修-未完成" :
            post_Parameter = {"工单类型": None, "开始日期":startDate,"结束日期":endingDate,"所选单位":selected_office,"工单范围":None,"是否完成的工单":"false","工单服务类型":"1"}
        elif  selected_module =="首页-紧急报修-已完成" :
            post_Parameter = {"工单类型": None, "开始日期":startDate,"结束日期":endingDate,"所选单位":selected_office,"工单范围":None,"是否完成的工单":"true","工单服务类型":"1"}
        elif  selected_module =="首页-紧急报修-全部" :
            post_Parameter = {"工单类型": None, "开始日期":startDate,"结束日期":endingDate,"所选单位":selected_office,"工单范围":None,"是否完成的工单":None,"工单服务类型":"1"}
        elif selected_module == "首页-驻场服务-未完成" :
            post_Parameter = {"工单类型": None, "开始日期":startDate,"结束日期":endingDate,"所选单位":selected_office,"工单范围":None,"是否完成的工单":"false","工单服务类型":"2"}
        elif  selected_module == "首页-驻场服务-已完成" :
            post_Parameter = {"工单类型": None, "开始日期":startDate,"结束日期":endingDate,"所选单位":selected_office,"工单范围": None,"是否完成的工单":"true", "工单服务类型":"2"}
        elif selected_module == "首页-驻场服务-全部":
            post_Parameter = {"工单类型": None,"开始日期":startDate,"结束日期":endingDate,"所选单位":selected_office,"工单范围": None,"是否完成的工单":None,"工单服务类型": "2"}
        elif selected_module == "服务端-事件-全部工单":
            post_Parameter = {"工单类型": None, "开始日期":startDate,"结束日期":endingDate,"所选单位":selected_office,"工单范围":None,"是否完成的工单":None,"工单服务类型":None}
        print("post_Parameter:",post_Parameter)
        # 调用接口
        list_ListWorkOrder,req_text,url  = TheRepairOrderInterface(JSESSIONID, post_Parameter).allListData()
        """编译从接口投诉清单返回的数据"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        # "1":数据对比用户；
        if effect:
            list_workOrder = workOrder_compile(list_ListWorkOrder).WorkOrderProcess_allListData(self.FilterParameters)
        # "1":获取部分post请求数据
        else:
            list_workOrder = OtherInterfaces_compile(list_ListWorkOrder).WorkOrderProcess_Post(self.FilterParameters,req_text)
        return list_workOrder,post_Parameter,url


    def TheRepairSquare_chooseListData(self,effect=True):
        """
        小程序--服务端--事件（待响应；预约中；待处理；处理中；已处理；已关单；已挂起）
        :return:
        """
        req_text=None;list_workOrder_strState=[];post_Parameter = {};list_workOrder=None;list_ListWorkOrder=None
        JSESSIONID = self.FilterParameters["登录用户JSESSIONID"];startDate = self.FilterParameters["开始日期"];endingDate = self.FilterParameters["结束日期"]
        selected_module = self.FilterParameters["所属模块"]
        if selected_module == "服务端--事件--待响应":
            post_Parameter = {"工单状态":"2","开始日期":startDate,"结束日期":endingDate,"所在单位":None,"查看范围":None}
        elif selected_module == "服务端--事件--预约中":
            post_Parameter = {"工单状态":"3","开始日期":startDate,"结束日期":endingDate,"所在单位":None,"查看范围":None}
        elif selected_module == "服务端--事件--待处理":
            post_Parameter = {"工单状态": "4", "开始日期": startDate, "结束日期": endingDate, "所在单位": None, "查看范围": None}
        elif selected_module == "服务端--事件--处理中":
            post_Parameter = {"工单状态":"5","开始日期":startDate,"结束日期":endingDate,"所在单位":None,"查看范围":None}
        elif selected_module == "服务端--事件--已处理":
            post_Parameter = {"工单状态":"7","开始日期":startDate,"结束日期":endingDate,"所在单位":None,"查看范围":None}
        elif selected_module == "服务端--事件--已挂起":
            post_Parameter = {"工单状态": "6", "开始日期": startDate, "结束日期": endingDate, "所在单位": None, "查看范围": None}
        # 调用小程序--服务端--事件--待响应；预约中；待处理；处理中；已处理；已挂起
        list_ListWorkOrder,req_text,url = TheRepairOrderInterface(JSESSIONID,  post_Parameter).chooseListData()
        ##############################################################################################################
        """编译从接口投诉清单返回的数据"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        if effect:
            list_workOrder_intState = workOrder_compile(list_ListWorkOrder).compile_homePage(self.FilterParameters)
            # 把工单整数类型的工单状态编译成状态名称
            for workOrder in list_workOrder_intState:
                int_state = workOrder["工单状态"]
                state_name = dictionaries(JSESSIONID, int_state).ADictionaryTable()  # 整数的工单状态转化成str工单名称
                workOrder["工单状态"] = state_name
                list_workOrder_strState.append(workOrder)
            # 截取工单更新日期和创建日期的日期
            list_dataKey = ["工单创建日期", "工单更新日期"]
            list_workOrder = TimeFormat(list_workOrder_strState, list_dataKey).CaptureTheAate("%Y-%m-%d")
        else:
            list_workOrder = OtherInterfaces_compile(list_ListWorkOrder).WorkOrderProcess_Post(self.FilterParameters,req_text)
        return list_workOrder,post_Parameter,url


    def TheRepairSquare_closedTicketListData(self):
        """
        已关单列表数据
        :param effect:
        :return:
        """
        req_text = None;post_Parameter = {};list_workOrder = None;list_ListWorkOrder = None;list_workOrder_strState=[]
        JSESSIONID = self.FilterParameters["登录用户JSESSIONID"];startDate = self.FilterParameters["开始日期"]
        endingDate = self.FilterParameters["结束日期"];selected_module = self.FilterParameters["所属模块"]
        post_Parameter = {"工单状态": "2", "开始日期": startDate, "结束日期": endingDate, "所在单位": None, "查看范围": None}
        # 调用小程序--服务端--事件--已关单
        list_ListWorkOrder, req_text, url = TheRepairOrderInterface(JSESSIONID, post_Parameter).closedTicketListData()
        list_workOrder_intState = workOrder_compile(list_ListWorkOrder).WorkOrderProcess_closedTicketListData(self.FilterParameters)
        # 把工单整数类型的工单状态编译成状态名称
        for workOrder in list_workOrder_intState:
            int_state = workOrder["工单状态"]
            state_name = dictionaries(JSESSIONID, int_state).ADictionaryTable()  # 整数的工单状态转化成str工单名称
            workOrder["工单状态"] = state_name
            list_workOrder_strState.append(workOrder)
        # 截取工单更新日期和创建日期的日期
        list_dataKey = ["工单创建日期", "工单更新日期"]
        list_workOrder = TimeFormat(list_workOrder_strState, list_dataKey).CaptureTheAate("%Y-%m-%d")
        return list_workOrder,post_Parameter,url






    def TheRepairSquare_sjTicketServe_details(self,post_Parameter):
        """
        工单详情
        :return:
        """
        new_workOrder_details=[]
        JSESSIONID = self.FilterParameters["登录用户JSESSIONID"]
        # 调用小程序--详情页面
        workOrder_details,url = TheRepairOrderInterface(JSESSIONID, post_Parameter).sjTicketServe_details()
        # 因为只有一条数据，所有加转化成列表
        new_workOrder_details.append(workOrder_details)
        """编译从接口工单清单返回的数据"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        compile_workOrder = workOrder_compile(new_workOrder_details).connector_one(self.FilterParameters) # 编译调用小程序--首页--工单接口
        return compile_workOrder ,post_Parameter,url



class OtherInterfaces_actualValue:
    """其他接口实际值"""

    def __init__(self, JSESSIONID, FilterParameters=None,post_Parameter=None):
        """
        :param JSESSIONID:
        :param post_Parameter: 接口要传入的post参数
        """
        self.JSESSIONID = JSESSIONID
        self.FilterParameters=FilterParameters
        self.post_Parameter = post_Parameter
        self.compile_actualValue = None


    def findGroupList_actualValue(self):
        """
        查询所有群组(服务台改派用)
        :return:
        """
        # 调用接口获取接口返回值
        list_actualValue,url = UserAppController(self.JSESSIONID, None).findGroupList()
        # 编译接口返回值
        list_workOrder = OtherInterfaces_compile(self.JSESSIONID, list_actualValue).findGroupList_compile()
        # list_workOrder=[{'群组ID': '1c60c437542f44c8f8aa83a7c6a08dff9', '群组名称': '机动组5'}]
        return list_workOrder,url

    def findUserListByGroup_actualValue(self,group_id):
        """
        工单操作改派选人
        :return:
        """
        post_Parameter={"群组ID":group_id}
        # 调用接口获取接口返回值
        list_actualValue, url = UserAppController(self.JSESSIONID, None).findUserListByGroup(post_Parameter)
        # 编译接口返回值
        list_workOrder = OtherInterfaces_compile(self.JSESSIONID, list_actualValue).findUserListByGroup_compile()
        # list_workOrder=[{'用户ID': '5c2e57e50d904563b78acc6091970a67', '用户名称': '运维人员四'}, {'用户ID': 'fa20e86b843b4a53936d714afb967a7b', '用户名称': '运维组长'}]
        return list_workOrder, url









