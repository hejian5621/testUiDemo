#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 任务办理按钮的获取


from privately_owned.method import logTreatment
from utils.commonality.database_SqlRealize import dataProcessing
from privately_owned.Task_handling_button import IndependentMethod
from privately_owned.TestReport_sorting import TestReport_data_neaten
from privately_owned.professional_Work import professionalWork_data_dispose
import  sys,os,time
from tqdm import tqdm
from privately_owned.dicti_data_dispose import dictionaries


# 预期值私有方法



class Task_handling_button:
    """获取任务办理按钮"""
    def __init__(self,ProcessingDataList,userinfo):
        self.ProcessingDataList=ProcessingDataList
        self.userinfo=userinfo

    #
    # def miniProgram_incident_TaskToDealWith(self,screening):
    #     """
    #     小程序--事件模块--关于任务办理按钮方法
    #     根据权限等获取该登录用户应该有的任务办理按钮
    #     :return:
    #     """
    #     Timeout=None; list_dicti_WorkOrder=[];jurisdiction=None;expect_taskManagement=None;loginName=None;roleName=None
    #     JSESSIONID=None
    #     # 取出登录用户信息
    #     loginName = self.userinfo["登录名"];roleName = self.userinfo["用户权限"];JSESSIONID = self.userinfo["登录用户JSESSIONID"]
    #     userID = self.userinfo["用户ID"]
    #     module = screening["工单状态名称"]
    #     # 判断传过来的参数是否为空
    #     if self.ProcessingDataList:
    #         # 取出列表里的字典
    #         for dicti_WorkOrder in self.ProcessingDataList:
    #             whether_handler=None
    #             # 获取工单信息
    #             update_Date=dicti_WorkOrder["工单更新日期"] ;WorkOrder_number=dicti_WorkOrder["工单编号"]
    #             WorkOrder_Status=dicti_WorkOrder["工单状态"];WorkOrder_handlerID=dicti_WorkOrder["工单处理人ID"]
    #             # 如果登录用户是运维工程师（运维组长）就获取登录用户是不是组长，如果登录用户是服务台，就获取处理人是不是组长
    #             if roleName == "服务台" and module != "外协_待响应":
    #                 # 判断登录用户是不是组长,"2"代表不是组长，"1"代表是组长
    #                 userinfo1={}
    #                 userinfo1["登录名"]=WorkOrder_handlerID
    #                 jurisdiction = professionalWork_data_dispose().judge_loginName_groupLeader(userinfo1,WorkOrder_number)
    #             else:
    #                 # 判断登录用户是不是组长,"2"代表不是组长，"1"代表是组长
    #                 jurisdiction = professionalWork_data_dispose().judge_loginName_groupLeader(self.userinfo,WorkOrder_number)
    #             if module == "外协_待响应":
    #                 # 在外协_待响应模块实际工单是否超时,获取系统时候和工单的更新时间加上超时分钟对比，判断检查的工单是否超时
    #                 # 读取系统时间
    #                 SystemTime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    #                 # 根据工单的更新日期，加上耗时时间，返回最终预期的超时时间节点
    #                 time_Timeout = str(professionalWork_data_dispose().timeOutPeriod(JSESSIONID, update_Date))
    #                 # 当系统时间大于工单耗时预期的时间节点，证明工单已经超过了系统设置的耗时(1超时，2没有超时)
    #                 if SystemTime > time_Timeout:
    #                     Timeout = 1
    #                 else:
    #                     Timeout = 2
    #                 expect_taskManagement = IndependentMethod(self.userinfo).state_taskManagement_incident(module,jurisdiction, Timeout)
    #             elif module == "外协_预约中" or module == "外协_处理中" or module == "外协_待处理" or module == "外协_已处理" or module == "外协_已挂起":
    #                 # 通过工单的历史记录判断工单是否在挂起状态；"1"为申请挂起状态，"2"为没有在申请挂起状态
    #                 argument = professionalWork_data_dispose.workOrder_whether_suspended_state(WorkOrder_Status, WorkOrder_number)
    #                 #  判断该工单的处理人是不是登录用户,"1"为代表处理人是登录用户；"2"为代表处理人不是登录用户
    #                 if  userID==WorkOrder_handlerID:
    #                     whether_handler="1"
    #                 else:
    #                     whether_handler = "2"
    #                 expect_taskManagement = IndependentMethod(self.userinfo).state_taskManagement_incident(module, argument,whether_handler,jurisdiction)
    #             # 把任务办理按钮存入工单字典里    "任务办理": list_TaskToDealWith
    #             dicti_WorkOrder["任务办理"] = expect_taskManagement
    #             list_dicti_WorkOrder.append(dicti_WorkOrder)
    #         return list_dicti_WorkOrder



    def applet_TaskHandlingButton(self,appletName):
        """
        小程序任务办理按钮获取
        根据预期工单编号，通过平台名称（客户端、服务端）、登录用户，工单状态来获取任务办理按钮
        :param appletName: 平台名称（客户端、服务端）
        :return:
        """
        schedule_number=1;text=""
        # 统计返回工单的条数
        num=len(self.ProcessingDataList)
        """数据初始化"""
        expect_taskManagement = None;new_list_dicti_WorkOrder=[]
        # 取出登录用户信息
        loginName = self.userinfo["登录名"];                 roleName = self.userinfo["用户权限"]
        JSESSIONID = self.userinfo["登录用户JSESSIONID"];    userID = self.userinfo["用户ID"]
        if self.ProcessingDataList:  # 判断传过来的参数是否为空
            for dicti_WorkOrder in tqdm(self.ProcessingDataList):  # 便利出工单列表里的单条工单
                text = text + str(dicti_WorkOrder)
                update_Date=None;number=None;Int_Status=None;handlerID=None;in_out_ticket=None;repairsID=None;state_hang=None
                user_group_id=None
                # # 打印进度条
                # ProgressBar(schedule_number, num)
                schedule_number = schedule_number + 1
                expect_taskManagement = None;sort_logIn_arguments=None;Timeout=2;sort_handler_arguments=None
                sort_logIn=None;sort_handler=None;sort_logIn=None;sort_handler=None
                # 取出需要判断的单条工单基础信息
                Int_Status = dicti_WorkOrder["工单状态"]; in_out_ticket = dicti_WorkOrder["工单范围"];repairsID = dicti_WorkOrder["报修人ID"]
                if "工单更新日期" in  dicti_WorkOrder:
                    update_Date = dicti_WorkOrder["工单更新日期"]
                if "工单处理人ID" in dicti_WorkOrder:
                    handlerID = dicti_WorkOrder["工单处理人ID"]
                if "挂起状态" in dicti_WorkOrder:
                    state_hang = dicti_WorkOrder["挂起状态"]
                if "工单所在群组ID" in dicti_WorkOrder:
                    user_group_id = dicti_WorkOrder["工单所在群组ID"]
                # 整数类型的工单状态通过字典表编译成工单状态名称
                Str_Status = dictionaries(JSESSIONID, Int_Status).ADictionaryTable()
                # 判断工单有没有超时，因为工单超时后，工单在外协_待响应状态下改派权就到服务台那里去了
                # SystemTime = passShh_connectToServer("%Y-%m-%d %H:%M:%S").Get_server_time() # 获取服务器时间
                SystemTime =time.strftime("%Y-%m-%d %H:%M:%S")
                time_Timeout = str(professionalWork_data_dispose().timeOutPeriod(JSESSIONID, update_Date)) # 根据工单的更新日期，加上耗时时间，返回最终预期的超时时间节点
                if SystemTime > time_Timeout: # 当系统时间大于工单耗时预期的时间节点，证明工单已经超过了系统设置的耗时(1超时，2没有超时)
                    Timeout = 1
                # 当工单状态是一下状态的时候，工单处理人字段为空，无法通过处理人查询出是不是组长
                if Str_Status=="内部_待办理" or Str_Status=="内部_已完成" or Str_Status=="内部_已完成" or Str_Status == "内部_已关单" or \
                   Str_Status == "外协_待响应" or (Str_Status == "已撤销" and in_out_ticket =="1") or (Str_Status == "已撤销" and in_out_ticket =="0"):
                    pass
                else:
                    if user_group_id:
                        # 判断工单处理是不是组长
                        sort_handler, sql_handler = dataProcessing("groupIDuserID_Sort").user_name(user_group_id, handlerID)
                        if sort_handler:
                            sort_handler_arguments = sort_handler[0]["sort"]
                # 判断登录用户在工单所在的群组里是不是组长(None不是组长，"1":是组长)
                if appletName =="服务端":
                    if user_group_id:
                        sort_logIn, sql_logIn = dataProcessing("groupIDuserID_Sort").user_name(user_group_id, userID)
                        if sort_logIn:
                            sort_logIn_arguments = sort_logIn[0]["sort"]
                """开始获取，获取任务办理按钮的参数"""
                if appletName =="客户端" and roleName =="普通用户":
                    expect_taskManagement=Task_handling_button(None, None).clientSide_domesticConsumer(Str_Status, in_out_ticket)  # 普通用户根据工单状态判断获取任务办理按钮
                elif appletName =="客户端" and roleName =="用户管理员":
                    expect_taskManagement=Task_handling_button(None, self.userinfo).clientSide_UserAdministrator(Str_Status, in_out_ticket, repairsID)  # 用户管理员根据工单状态判断获取任务办理按钮
                elif appletName == "客户端" and roleName == "区域管理员":
                    expect_taskManagement=Task_handling_button(None, self.userinfo).clientSide_AreaManager(Str_Status, in_out_ticket, repairsID)  # 区域管理员根据工单状态判断获取任务办理按钮
                elif appletName == "服务端" and roleName == "运维工程师":
                    expect_taskManagement=Task_handling_button(None, self.userinfo).server_OPSengineer(Str_Status, handlerID, state_hang)  # 运维工程师根据工单状态判断获取任务办理按钮
                elif appletName == "服务端" and roleName == "运维经理":
                    expect_taskManagement=Task_handling_button(None, self.userinfo).server_OPSgroup(Str_Status, handlerID, state_hang, sort_logIn_arguments, Timeout)  # 运维组长根据工单状态判断获取任务办理按钮
                elif appletName == "服务端" and roleName == "服务台":
                    expect_taskManagement=Task_handling_button(None, self.userinfo).server_service(Str_Status, handlerID, state_hang, sort_logIn_arguments, sort_handler_arguments, Timeout)  # 运维组长根据工单状态判断获取任务办理按钮
                elif appletName == "服务端" and roleName == "运维总监":
                    expect_taskManagement = Task_handling_button(None, self.userinfo).server_OPSmajordomo(Str_Status)  # 运维组长根据工单状态判断获取任务办理按钮
                else:
                    print("在“小程序任务办理按钮获取”方法中，传入的平台名称“%r”和用户权限“%r”不符合以上判断，由此程序停止运行"%(appletName,roleName), __file__, sys._getframe().f_lineno)
                    os._exit(0)
                dicti_WorkOrder["任务办理"]=expect_taskManagement
                new_list_dicti_WorkOrder.append(dicti_WorkOrder)
        else:
            new_list_dicti_WorkOrder=None
        return  new_list_dicti_WorkOrder



    def clientSide_domesticConsumer(self,Str_Status,in_out_ticket):
        """
        根据平台名称和登录用户，获取任务办理按钮
        平台名称：客户端
        登录用户：普通用户
        :return:
        """
        expect_taskManagement=None
        if Str_Status == "内部_待办理":
            expect_taskManagement = ['进度', '撤销', '催单']
        elif Str_Status == "内部_已完成":
            expect_taskManagement = ['进度','评价']
        elif Str_Status == "内部_已关单" or (Str_Status == "已撤销" and in_out_ticket =="1") :
            expect_taskManagement = ['进度']
        elif Str_Status == "外协_待响应" or Str_Status == "外协_预约中" or Str_Status == "外协_待处理" or Str_Status == "外协_处理中" or Str_Status == "外协_已挂起":
            expect_taskManagement = ['进度','投诉','催单']
        elif Str_Status == "外协_已处理":
            expect_taskManagement = ['进度','投诉','评价']
        elif  Str_Status ==  "外协_已关单" or (Str_Status == "已撤销" and in_out_ticket =="0") :
            expect_taskManagement = ['进度','投诉']
        return expect_taskManagement


    def clientSide_UserAdministrator(self,Str_Status,in_out_ticket,repairsID):
        """
        根据平台名称和登录用户，获取任务办理按钮
        平台名称：客户端
        登录用户：用户管理员
        :return:
        """
        expect_taskManagement = None;userID = self.userinfo["用户ID"]
        if userID==repairsID:
            if Str_Status == "外协_待响应" or Str_Status == "外协_预约中" or Str_Status == "外协_待处理" or Str_Status == "外协_处理中" or Str_Status == "外协_已挂起":
                expect_taskManagement = ['进度', '投诉', '催单']
            elif Str_Status == "外协_已处理":
                expect_taskManagement = ['进度', '投诉', '评价']
            elif Str_Status == "外协_已关单" or (Str_Status == "已撤销" and in_out_ticket == "0"):
                expect_taskManagement = ['进度', '投诉']
        else:
            if Str_Status == "内部_待办理":
                expect_taskManagement = ['进度', '撤销','内部处理','外协处理']
            elif Str_Status == "内部_已完成" or Str_Status == "内部_已关单" or (Str_Status == "已撤销" and in_out_ticket == "1"):
                expect_taskManagement = ['进度']
            elif Str_Status == "外协_待响应" or Str_Status == "外协_预约中" or Str_Status == "外协_待处理" or Str_Status == "外协_处理中" or Str_Status == "外协_已挂起":
                expect_taskManagement = ['进度', '投诉', '催单']
            elif Str_Status == "外协_已处理" or Str_Status == "外协_已关单" or (Str_Status == "已撤销" and in_out_ticket == "0"):
                expect_taskManagement = ['进度', '投诉']
        return expect_taskManagement


    def clientSide_AreaManager(self,Str_Status,in_out_ticket,repairsID):
        """
        根据平台名称和登录用户，获取任务办理按钮
        平台名称：客户端
        登录用户：区域管理员
        :return:
        """
        expect_taskManagement = None; userID = self.userinfo["用户ID"]
        if userID == repairsID:
            if Str_Status == "外协_待响应" or Str_Status == "外协_预约中" or Str_Status == "外协_待处理" or Str_Status == "外协_处理中" or Str_Status == "外协_已挂起":
                expect_taskManagement = ['进度', '投诉','评论','催单']
            elif Str_Status == "外协_已处理":
                expect_taskManagement = ['进度', '投诉','评论','评价']
            elif Str_Status == "外协_已关单" or (Str_Status == "已撤销" and in_out_ticket == "0"):
                expect_taskManagement = ['进度', '投诉','评论']
        else:
            if Str_Status == "内部_待办理" or Str_Status == "内部_已完成" or Str_Status == "内部_已关单" or (Str_Status == "已撤销" and in_out_ticket == "1"):
                expect_taskManagement = ['进度','评论']
            elif Str_Status == "外协_待响应" or Str_Status == "外协_预约中" or Str_Status == "外协_待处理" or Str_Status == "外协_处理中" or Str_Status == "外协_已挂起":
                expect_taskManagement = ['进度', '投诉','评论','催单']
            elif Str_Status == "外协_已处理" or Str_Status == "外协_已关单" or (Str_Status == "已撤销" and in_out_ticket == "0"):
                expect_taskManagement = ['进度', '投诉','评论']
        return expect_taskManagement


    def server_OPSengineer(self,Str_Status,handlerID,state_hang):
        """
        根据平台名称和登录用户，获取任务办理按钮
        平台名称：客户端
        登录用户：运维工程师
        :return:
        """
        expect_taskManagement = None;userID = self.userinfo["用户ID"]
        # 当工单处理人是登录用户时
        if userID == handlerID:
            if  Str_Status == "外协_预约中" or Str_Status == "外协_待处理":
                if state_hang:          # 当挂起状态字段为空时，证明该工单并没有申请挂起
                    expect_taskManagement = ['进度']
                else:
                    expect_taskManagement = ['进度', '到达现场', '挂起']
            elif Str_Status == "外协_处理中":
                if state_hang:  # 当挂起状态字段为空时，证明该工单并没有申请挂起
                    expect_taskManagement = ['进度']
                else:
                    expect_taskManagement = ['进度', '完成工单', '挂起']
            elif Str_Status == "外协_已挂起" or Str_Status == "外协_已处理":
                expect_taskManagement = ['进度']
        # 当工单处理人不是登录用户时或者工单没有处理人时
        else:
            if Str_Status == "外协_待响应" or Str_Status == "外协_预约中" or Str_Status == "外协_待处理" or Str_Status == "外协_处理中" or \
                    Str_Status == "外协_已挂起" or Str_Status == "外协_已处理":
                expect_taskManagement = ['进度']
        return expect_taskManagement


    def server_OPSgroup(self,Str_Status,handlerID,state_hang,sort_arguments, Timeout):
        """
        根据平台名称和登录用户，获取任务办理按钮
        平台名称：客户端
        登录用户：运维组长
        :return:
        """

        expect_taskManagement = None;userID = self.userinfo["用户ID"];sort=None; sql=None
        # 当工单状态是外协_待响应的时候，没有处理人，通过工单的处理人无法判断任务办理按钮
        if  Str_Status == "外协_待响应":
            expect_taskManagement =['进度']
            if sort_arguments == '1' and Timeout ==2:  # 如果登录用户在工单所关联群组里是组长
                expect_taskManagement = ['进度','接单','改派']
        else:
            # 当工单处理人是登录用户时
            if userID == handlerID:
                if Str_Status == "外协_预约中" or Str_Status == "外协_待处理":
                    if state_hang:  # 当挂起状态字段为空时，证明该工单并没有申请挂起
                        expect_taskManagement = ['进度']
                    else:
                        expect_taskManagement = ['进度', '到达现场', '挂起']
                elif Str_Status == "外协_处理中":
                    if state_hang:  # 当挂起状态字段为空时，证明该工单并没有申请挂起
                        expect_taskManagement = ['进度']
                    else:
                        expect_taskManagement = ['进度', '完成工单', '挂起']
                elif Str_Status == "外协_已挂起" or Str_Status == "外协_已处理":
                    expect_taskManagement = ['进度']
            # 当工单处理人不是登录用户时或者工单没有处理人时
            else:
                if Str_Status == "外协_预约中" or Str_Status == "外协_待处理" or Str_Status == "外协_处理中":
                    expect_taskManagement = ['进度']
                    if state_hang:  # 当挂起状态字段为空时，证明该工单并没有申请挂起
                        if sort_arguments =='1': # 如果登录用户是组长
                            expect_taskManagement = ['进度', '挂起审核']
                elif Str_Status == "外协_已挂起" or Str_Status == "外协_已处理":
                    expect_taskManagement = ['进度']
        return expect_taskManagement


    def server_service(self,Str_Status,handlerID,state_hang,sort_logIn_arguments,sort_handler_arguments,Timeout):
        """
        根据平台名称和登录用户，获取任务办理按钮
        平台名称：客户端
        登录用户：服务台
        :return:
        """
        expect_taskManagement = None;userID = self.userinfo["用户ID"]
        # 当工单状态是外协_待响应的时候，没有处理人，通过工单的处理人无法判断任务办理按钮
        if Str_Status == "外协_待响应":
            expect_taskManagement = ['进度','撤销']
            if    sort_logIn_arguments == '1' and Timeout==2:  # 如果登录用户在工单所关联群组里是组长，并且工单没有超时
                expect_taskManagement = ['进度','撤销', '接单', '改派']
            elif  Timeout==1:
                expect_taskManagement = ['进度', '撤销','改派']
        else:
            # 判断工单的处理人是否是组长
            if sort_handler_arguments=="1":  # 工单处理人是组长
                if Str_Status == "外协_预约中" or Str_Status == "外协_待处理" or Str_Status == "外协_处理中":
                    if userID == handlerID:
                        if Str_Status == "外协_处理中":
                            expect_taskManagement = ['进度','撤销', '到达现场', '挂起'] # 当挂起状态字段为空时，证明该工单并没有申请挂起
                        else:
                            expect_taskManagement = ['进度','撤销', '完成工单', '挂起']  # 当挂起状态字段为空时，证明该工单并没有申请挂起
                        if state_hang:  # 当挂起状态字段不为为空时，证明该工单在申请挂起状态
                            expect_taskManagement = ['进度','撤销','挂起审核']
                    else:
                        expect_taskManagement = ['进度', '撤销'] # 当挂起状态字段为空时，证明该工单并没有申请挂起
                        if state_hang:  # 当挂起状态字段不为为空时，证明该工单在申请挂起状态
                            expect_taskManagement = ['进度', '撤销', '挂起审核']
                elif Str_Status == "外协_已挂起":
                    expect_taskManagement = ['进度', '撤销', '解挂', '改派']
                elif Str_Status == "外协_已处理":
                    expect_taskManagement = ['进度','撤销']
            else:  # 工单处理人不是组长
                if Str_Status == "外协_预约中" or Str_Status == "外协_待处理" or Str_Status == "外协_处理中":
                    expect_taskManagement = ['进度', '撤销']
                    if userID == handlerID:
                        if Str_Status == "外协_处理中":
                            expect_taskManagement = ['进度', '撤销', '完成工单', '挂起']
                        else:
                            expect_taskManagement = ['进度', '撤销', '到达现场', '挂起']
                        if state_hang:  # 当挂起状态字段不为为空时，证明该工单在申请挂起状态
                            expect_taskManagement = ['进度', '撤销']
                elif Str_Status == "外协_已挂起":
                    expect_taskManagement = ['进度', '撤销', '解挂', '改派']
                elif Str_Status == "外协_已处理":
                    expect_taskManagement = ['进度', '撤销']
        return expect_taskManagement


    def server_OPSmajordomo(self,Str_Status):
        """
        根据平台名称和登录用户，获取任务办理按钮
        平台名称：客户端
        登录用户：运维总监
        :return:
        """
        expect_taskManagement = None
        if Str_Status == "外协_待响应" or Str_Status == "外协_预约中" or Str_Status == "外协_待处理" or Str_Status == "外协_处理中" or  \
                Str_Status == "外协_已挂起" or Str_Status == "外协_已处理":
            expect_taskManagement = ['进度']
        return expect_taskManagement



    def Complaint_expected_taskmgr(self):
        """
        在投诉清单页面的数据中增加任务办理按钮
        状态：0：待受理；1：已受理；2：已处理；3：已解决
        任务办理按钮：1：任务受理；2：
        :return:
        """
        loginName = self.userinfo["登录名"];roleName = self.userinfo["用户权限"]
        # 生成一个新的投诉信息列表
        new_Complaint_list_data  =[]
        #  根据登录名获取登录用户ID
        login_userid,sql= dataProcessing("loginName_userID").user_name(loginName)
        login_userid = login_userid[0]["id"]
        if self.ProcessingDataList:
            # 取出单个投诉信息
            for Complaint_data in self.ProcessingDataList:
                #  取出投诉信息状态
                Complaint_state = Complaint_data["投诉单状态"]
                # 取出单个投诉信息的投诉人ID
                Complaint_userID = Complaint_data["投诉用户id"]
                # 取出单个投诉信息的投诉人ID
                complainant_By_ID = Complaint_data["被投诉人ID"]
                if roleName == "普通用户" :
                    #  登录用户如果是普通用户，用户ID和投诉信息的投诉用户id对比，如果赌博通过，就增加确定按钮
                    if login_userid == Complaint_userID:
                        #判断投诉信息状态,2:已处理
                        if Complaint_state == "2":
                                Complaint_data["任务办理"] =['3']
                        else:
                            Complaint_data["任务办理"] = None
                    else:
                        Complaint_data["任务办理"] = None
                elif roleName == "用户管理员" or roleName == "区域管理员":
                    # 登录用户如果是用户管理员，就判断投诉信息的投诉用户id是否是该用户管理员单位里的用户，如果是就加上确定按钮
                    # 登录用户如果是区域管理员，就判断投诉信息的投诉用户id是否是该区域管理员所管辖单位里的用户，如果是就加上确定按钮
                    # 投诉人ID强行转化成列表
                    Complaint_userIDlist = []
                    Complaint_userIDlist.append(Complaint_userID)
                    gobalBuyer,list_unitsIDuserID = authorityManagement(self.userinfo).AreaManager_authorityManagement(Complaint_userIDlist, "userID")
                    if gobalBuyer == True:
                        # 判断投诉信息状态,2:已处理
                        if Complaint_state == "2":
                            Complaint_data["任务办理"] = ['3']
                        else:
                            Complaint_data["任务办理"] = None
                    else:
                        Complaint_data["任务办理"] = None
                elif roleName == "运维工程师" or roleName == "运维经理" or roleName == "运维总监" :
                    if login_userid == complainant_By_ID:
                        # 判断投诉信息状态,1:已受理
                        if Complaint_state == "1":
                            Complaint_data["任务办理"] = ['2']
                        else:
                            Complaint_data["任务办理"] = None
                    else:
                        Complaint_data["任务办理"] = None
                elif roleName == "服务台" :
                    # 判断投诉信息状态,0:待受理；任务办理按钮：1：任务受理
                    if Complaint_state == "0":
                        Complaint_data["任务办理"] = ['1']
                    else:
                        Complaint_data["任务办理"] = None
                else:
                    Complaint_data["任务办理"] = None
                new_Complaint_list_data.append(Complaint_data)
        else:
            new_Complaint_list_data="为空"
        return new_Complaint_list_data



















