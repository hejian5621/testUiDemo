#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 根据电子表格返回的参数，进行编译成系统所需要的参数条件，打包成参数集


from utils.commonality.database_SqlRealize import dataProcessing
from appletConnector import TheRepairOrderInterface
import time, random
from utils.verification.Actual_value import WorkOrderProcess_actualValue
from utils.privately_owned.timeDisposal import TimeFormat
from privately_owned.professional_Work import professionalWork_data_dispose
from privately_owned.userinfo_processing import userinfo_acquire_And_Dispose



class excessive_parameter:
    """获取参数的过度方法"""


    def __init__(self,step):
        self.step = step



    def acquire_TransferRecord(self,RetrieveParameter):
        """
        通过页面获取流转记录参数的过度方法
        :return:
        """
        TransferRecord=None;post_Parameter=None
        if   self.step=="用户管理员-内部处理" or self.step=="用户管理员-外协处理" :  # 客户端
            # 通过查询页面清单接口获取，获取工作流里的参数并且更新到参数集中
            TransferRecord, post_Parameter = WorkOrderProcess_actualValue(RetrieveParameter).TheRepairSquare_InsideRepairListData(False)
        elif self.step== "普通用户-外部-评论" or self.step== "普通用户-内部-评论":   # 客户端
            TransferRecord, post_Parameter = WorkOrderProcess_actualValue(RetrieveParameter).TheRepairSquare_allListData(False)
        else:   # 服务端
            TransferRecord, post_Parameter = WorkOrderProcess_actualValue(RetrieveParameter).TheRepairSquare_chooseListData(False)
        return TransferRecord, post_Parameter


class DataList_Processing:
    """列表页面数据对比，参数获取"""

    def __init__(self, useCase):
        self.useCase = useCase


    def WorkOrderList(self,connector,Usecasename):
        """
        工单列表
        :return:
        """
        Their_module =None;testPoint =None;dictionaryKeys=None;startDate=None;dateClosed=None;office_name=None;officeID=None
        selected_officeName=None;selected_officeID=None
        """取出筛选信息"""
        appletName = self.useCase["平台名称"] #取出平台名称（客户端或者服务端)
        userRight  = self.useCase["用户权限"]  # 取出被测用户权限
        user_type = self.useCase["用户类型"]  # 取出被测用户权限所在单位
        office_name =self.useCase["用户所在单位"]  # 取出被测用户权限所在单位
        selected_officeName = self.useCase["所选单位"]  # 取出被测用户权限所在单位
        Subordinate = self.useCase["所属接口"]  # 取出被测用户权限所在单位
        dateRange=self.useCase["日期范围"]   # 取出日期范围
        UseCase_number = self.useCase["用例编号"]  # 取出日期范围
        testPoint_spreadsheet = self.useCase["测试点"]  # 取出日期范围
        Their_module = self.useCase["所属模块"]  # 取出日期范围
        # 根据筛选条件列表取出用户信息
        initial_userinfo={"用户权限":userRight,"用户所在单位":office_name}
        list_dicti_userinfo = userinfo_acquire_And_Dispose(initial_userinfo).UserDetails() # 获取用户信息
        dicti_userinfo = list_dicti_userinfo[0]  # 用户打包信息
        dictionaryKeys = connector + UseCase_number # 获取字典的键
        """获取参数包"""
        loginName=dicti_userinfo["登录名"];roleName=dicti_userinfo["用户权限"];userid=dicti_userinfo["用户ID"]
        testResult = "预期值不等于实际值，测试不通过"  # 获取结果
        # 获取日期范围
        if dateRange != "空":
            dict_date =TimeFormat(dateRange).dateParameter_actualDate()  # 根据日期范围获取具体的日期（开始日期和结束日期）
            startDate = dict_date["开始日期"][0];dateClosed = dict_date["结束日期"][0]  # 获取开始日期和结束日期
        if user_type == "外部": # 获取测试报告登录用户信息 ；# 单位名称转化成单位ID
            userinfo = "用户登录名：%r；用户权限：%r；用户ID：%r；用户所在单位：%r" % (loginName, roleName, userid,office_name)  # 获取登录用户信息
            if selected_officeName!="空":
                # 单位名称转化成单位ID
                selected_officeID = dataProcessing("officeName_officeID").user_name(selected_officeName)
                selected_officeID = selected_officeID[0][0]["单位ID"]
            else:
                selected_officeName=None
        else:
            userinfo = "用户登录名：%r；用户权限：%r；用户ID：%r；所在群组：%r" % (loginName, roleName, userid, office_name)  # 获取登录用户信息
        # 测试点
        testPoint = testPoint_spreadsheet+"\n"+"备注实际筛选条件：开始日期：%r；结束日期：%r；所在单位：%r"%(startDate,dateClosed,office_name)  # 测试点
        # 打包参数包
        parameter_packet = {"所属接口":Subordinate,"平台名称":appletName ,"所属模块": Their_module, "检查登录用户信息":userinfo ,"用例名称": Usecasename,
                              "测试结果":testResult,"测试点":testPoint ,"字典的键": dictionaryKeys, "重复筛选参数": Their_module,
                            "开始日期":startDate,"结束日期":dateClosed,"所选单位名称":selected_officeName,"所选单位ID":selected_officeID}
        # 合并参数包
        dicti_userinfo_parameter_packet=dict(dicti_userinfo, **parameter_packet)
        print("\033[1;34;40m获取用例“%r”，用例编号“%r”的参数包：\033[0m\033[4;35;40m%r" % (connector,UseCase_number, dicti_userinfo_parameter_packet))
        return dicti_userinfo_parameter_packet


class initialize_parameterPacket:
    """初始化测试包"""

    def __init__(self, useCase,tableName,UseCaseName):
        self.useCase = useCase  # 电子表格返回的用例参数
        self.tableName = tableName  # 表名
        self.UseCaseName=UseCaseName  # 测试用例
        self.parameterPacket=None


    def TheLoginModule(self):
        """
        登录模块，初始化参数包（针对电子表格）
        :return:
        """
        Their_module = None;office_name = None;selected_officeName = None;appletName=None;userRight=None;Subordinate=None
        """取出筛选信息"""
        UseCase_number = self.useCase["用例编号"]  ; testPoint_spreadsheet = self.useCase["测试点"]
        appletName = self.useCase["平台名称"] ;     Their_module = self.useCase["所属模块"]
        userRight = self.useCase["用户权限"] ;       user_type = self.useCase["用户类型"]
        office_name = self.useCase["用户所在单位"] ;  Subordinate = self.useCase["所属接口"]
        """根据筛选条件列表取出用户信息"""
        initial_userinfo = {"用户权限": userRight, "用户所在单位": office_name}
        list_dicti_userinfo = userinfo_acquire_And_Dispose(initial_userinfo).UserDetails()  # 获取用户信息
        dicti_userinfo = list_dicti_userinfo[0]  # 用户打包信息
        loginName = dicti_userinfo["登录名"];roleName = dicti_userinfo["用户权限"];userid = dicti_userinfo["用户ID"];phone = dicti_userinfo["用户联系电话"]
        """获取参数包"""
        dictionaryKeys = self.tableName + UseCase_number  # 获取字典的键
        if user_type == "外部": # 获取测试报告登录用户信息
            userinfo = "用户登录名：%r；用户权限：%r；用户ID：%r；用户联系电话：%r" % (loginName, roleName, userid, phone)
        else:
            userinfo = "用户登录名：%r；用户权限：%r；用户ID：%r；用户联系电话：%r" % (loginName, roleName, userid, phone)
        testResult = "返回的结果不是200，测试不通过"  # 获取结果
        # 打包参数包
        parameter_packet = {"所属接口": Subordinate, "平台名称": appletName, "所属模块": Their_module, "检查登录用户信息": userinfo,
                            "用例名称":self.UseCaseName,"测试结果": testResult, "测试点": testPoint_spreadsheet, "字典的键": dictionaryKeys, "重复筛选参数": Their_module,
                             "所选单位": selected_officeName}
        # 合并参数包
        self.parameterPacket = dict(dicti_userinfo, **parameter_packet)
        print("\033[1;34;40m获取用例“%r”，用例编号“%r”的参数包：\033[0m\033[4;35;40m%r" % (self.UseCaseName, UseCase_number, self.parameterPacket))
        return self.parameterPacket


    def equipmentSchedule(self):
        """
        设备清单模块，初始化参数包（针对电子表格）
        :return:
        """
        Their_module = None;office_name = None;selected_officeName = None;appletName = None;userRight = None;Subordinate = None
        selected_officeID=None
        """取出筛选信息"""
        UseCase_number = self.useCase["用例编号"];           testPoint_spreadsheet = self.useCase["测试点"]
        appletName = self.useCase["平台名称"];               Their_module = self.useCase["所属模块"]
        userRight = self.useCase["用户权限"];                user_type = self.useCase["用户类型"]
        office_name = self.useCase["用户所在单位"];          selected_officeName = self.useCase["所选单位"]
        batch = self.useCase["批次"]              ;          devicename = self.useCase["设备名称"]
        Subordinate = self.useCase["所属接口"]
        """根据筛选条件列表取出用户信息"""
        initial_userinfo = {"用户权限": userRight, "用户所在单位": office_name}
        list_dicti_userinfo = userinfo_acquire_And_Dispose(initial_userinfo).UserDetails()  # 获取用户信息
        dicti_userinfo = list_dicti_userinfo[0]  # 用户打包信息
        loginName = dicti_userinfo["登录名"];roleName = dicti_userinfo["用户权限"];userid = dicti_userinfo["用户ID"];phone = dicti_userinfo["用户联系电话"]
        """生成参数包"""
        if batch=="空":
            batch = None
        else:
            if type(batch) ==type(12.0):
                batch = str(int(batch))
        if selected_officeName=="空":
            selected_officeName = None
        if devicename=="空":
            devicename = None
        dictionaryKeys = self.tableName + UseCase_number  # 获取字典的键
        if user_type == "外部":  # 获取测试报告登录用户信息 ；# 单位名称转化成单位ID
            userinfo = "用户登录名：%r；用户权限：%r；用户ID：%r" % (loginName, roleName, userid)
            if selected_officeName != "空" and selected_officeName !=None:
                # 单位名称转化成单位ID
                selected_officeID = dataProcessing("officeName_officeID").user_name(selected_officeName)
                selected_officeID = selected_officeID[0][0]["单位ID"]
            else:
                selected_officeID = None
        else:
            userinfo = "用户登录名：%r；用户权限：%r；用户ID：%r" % (loginName, roleName, userid)
        testResult = "返回资产设备清单，实际值不等于预期值，测试失败"  # 获取结果
        testPoint =testPoint_spreadsheet+"\n"+"实际筛选参数“"+"批次："+str(batch)+"；"+"所选单位:"+str(selected_officeName)+"；"+"设备名称:"+str(devicename)+"”"+"用例编号："+UseCase_number
        # 打包参数包
        parameter_packet = {"所属接口": Subordinate, "平台名称": appletName, "所属模块": Their_module, "检查登录用户信息": userinfo,"用例名称": self.UseCaseName,
                            "测试结果": testResult, "测试点": testPoint,"字典的键": dictionaryKeys, "重复筛选参数": Their_module,
                            "所选单位名称": selected_officeName,"所选单位ID": selected_officeID,"批次":batch,"设备名称":devicename}
        # 合并参数包
        self.parameterPacket = dict(dicti_userinfo, **parameter_packet)
        print("\033[1;34;40m获取用例“%r”，用例编号“%r”的参数包：\033[0m\033[4;35;40m%r" % (
        self.UseCaseName, UseCase_number, self.parameterPacket))
        return self.parameterPacket



    def StatisticsOfRepairQuantity(self):
        """
        设备清单模块，初始化参数包（针对电子表格）
        :return:
        """
        Their_module = None;office_name = None;selected_officeName = None;appletName = None;userRight = None;Subordinate = None
        selected_officeID=None;dateClosed=None;startDate=None;list_selected_officeName=None
        """取出筛选信息"""
        UseCase_number = self.useCase["用例编号"];           testPoint_spreadsheet = self.useCase["测试点"]
        appletName = self.useCase["平台名称"];               Their_module = self.useCase["所属模块"]
        userRight = self.useCase["用户权限"];                user_type = self.useCase["用户类型"]
        office_name = self.useCase["用户所在单位"];          selected_officeName = self.useCase["所选单位"]
        dateRange = self.useCase["日期范围"]           ;         Subordinate = self.useCase["所属接口"]
        """根据筛选条件列表取出用户信息"""
        initial_userinfo = {"用户权限": userRight, "用户所在单位": office_name}
        list_dicti_userinfo = userinfo_acquire_And_Dispose(initial_userinfo).UserDetails() # 获取用户信息
        dicti_userinfo = list_dicti_userinfo[0]  # 用户打包信息
        loginName = dicti_userinfo["登录名"];roleName = dicti_userinfo["用户权限"];userid = dicti_userinfo["用户ID"];phone = dicti_userinfo["用户联系电话"]
        """编译日期范围"""
        if dateRange != "空":
            dict_date = TimeFormat(dateRange).dateParameter_actualDate()  # 根据日期范围获取具体的日期（开始日期和结束日期）
            startDate = dict_date["开始日期"][0];dateClosed = dict_date["结束日期"][0]  # 获取开始日期和结束日期
        """获取所选单位ID"""
        list_selected_officeID=[]
        if user_type == "外部":  # 获取测试报告登录用户信息 ；
            userinfo = "用户登录名：%r；用户权限：%r；用户ID：%r" % (loginName, roleName, userid)
        else:
            userinfo = "用户登录名：%r；用户权限：%r；用户ID：%r" % (loginName, roleName, userid)
        if selected_officeName != "空": # 单位名称转化成单位ID
            list_selected_officeName = selected_officeName.split(',')  # 把所选单位从字符串转化成列表
            for selected_officeName in list_selected_officeName:
                selected_officeID = dataProcessing("officeName_officeID").user_name(selected_officeName) # 单位名称转化成单位ID
                selected_officeID = selected_officeID[0][0]["单位ID"]
                list_selected_officeID.append(selected_officeID)
        else:
            list_selected_officeID = None
        """获取测试报告参数"""
        dictionaryKeys = self.tableName + UseCase_number  # 获取字典的键
        testResult = "实际工单数不等于预期工单数，测试失败"  # 获取结果
        # 打包参数包
        parameter_packet = {"所属接口": Subordinate, "平台名称": appletName, "所属模块": Their_module, "检查登录用户信息": userinfo,"用例名称": self.UseCaseName,
                            "测试结果": testResult, "测试点": testPoint_spreadsheet,"字典的键": dictionaryKeys, "重复筛选参数": Their_module,
                            "所选单位名称": list_selected_officeName,"所选单位ID": list_selected_officeID,"开始日期":startDate,"结束日期":dateClosed}
        """合并用户信息参数包，生成新的参数包"""
        self.parameterPacket = dict(dicti_userinfo, **parameter_packet)
        print("\033[1;34;40m获取用例“%r”，用例编号“%r”的参数包：\033[0m\033[4;35;40m%r" % (self.UseCaseName, UseCase_number, self.parameterPacket))
        return self.parameterPacket



    def ListOfComplaints(self):
        """
        投诉清单模块，初始化参数包（针对电子表格）
        :return:
        """
        Their_module = None;office_name = None;selected_officeName = None;appletName = None;userRight = None;Subordinate = None
        selected_officeID=None;dateClosed=None;startDate=None;dateParameter=None;titleAndcontent=None
        """取出筛选信息"""
        UseCase_number = self.useCase["用例编号"];           testPoint_spreadsheet = self.useCase["测试点"]
        appletName = self.useCase["平台名称"];               Their_module = self.useCase["所属模块"]
        userRight = self.useCase["用户权限"];                user_type = self.useCase["用户类型"]
        office_name = self.useCase["用户所在单位"];          selected_officeName = self.useCase["所选单位"]
        dateRange = self.useCase["日期范围"]           ;         Subordinate = self.useCase["所属接口"]
        titleAndcontent=self.useCase["标题或内容"]
        """根据筛选条件列表取出用户信息"""
        initial_userinfo = {"用户权限": userRight, "用户所在单位": office_name}
        list_dicti_userinfo = userinfo_acquire_And_Dispose(initial_userinfo).UserDetails()  # 获取用户信息
        dicti_userinfo = list_dicti_userinfo[0]  # 用户打包信息
        loginName = dicti_userinfo["登录名"];roleName = dicti_userinfo["用户权限"];userid = dicti_userinfo["用户ID"];phone = dicti_userinfo["用户联系电话"]
        """编译日期范围"""
        dict_date =TimeFormat(dateRange).dateParameter_actualDate()  # 根据日期范围获取具体的日期（开始日期和结束日期）
        startDate = dict_date["开始日期"][0];dateClosed = dict_date["结束日期"][0]  # 获取开始日期和结束日期
        # 获取日期参数筛选条件,None:本月；1：上月；3：近三月；6：近半年；7：本年度
        if dateRange =="本月":
            dateParameter = None
        elif dateRange =="上月":
            dateParameter = 1
        elif dateRange =="近三月":
            dateParameter = 3
        elif dateRange =="近半年":
            dateParameter = 6
        elif dateRange =="本年度":
            dateParameter = 7
        """获取所选单位ID"""
        if user_type == "外部":  # 获取测试报告登录用户信息
            userinfo = "用户登录名：%r；用户权限：%r；用户ID：%r" % (loginName, roleName, userid)
        else:
            userinfo = "用户登录名：%r；用户权限：%r；用户ID：%r" % (loginName, roleName, userid)
        if selected_officeName != "空":   # 单位名称转化成单位ID
            # 单位名称转化成单位ID
            selected_officeID = dataProcessing("officeName_officeID").user_name(selected_officeName)
            selected_officeID = selected_officeID[0][0]["单位ID"]
        else:
            selected_officeName = None
        if titleAndcontent=="空": # 转化筛选条件内容或者标题
            titleAndcontent=None
        """获取测试报告参数"""
        dictionaryKeys = self.tableName + UseCase_number  # 获取字典的键
        testPoint=testPoint_spreadsheet+"\n"+"4、实际筛选条件:“"+"开始日期："+startDate+"；"+"结束日期："+dateClosed
        testResult = "返回投诉模块清单页面数据，实际值不等于预期值，测试失败"  # 获取结果
        # 打包参数包
        parameter_packet = {"所属接口": Subordinate, "平台名称": appletName, "所属模块": Their_module, "检查登录用户信息": userinfo,"用例名称": self.UseCaseName,
                            "测试结果": testResult, "测试点": testPoint,"字典的键": dictionaryKeys, "重复筛选参数": Their_module,
                            "所选单位名称": selected_officeName,"所选单位ID": selected_officeID,"开始日期":startDate,"结束日期":dateClosed,"日期参数":dateParameter,
                            "筛选条件内容或者标题":titleAndcontent}
        """合并用户信息参数包，生成新的参数包"""
        self.parameterPacket = dict(dicti_userinfo, **parameter_packet)
        print("\033[1;34;40m获取用例“%r”，用例编号“%r”的参数包：\033[0m\033[4;35;40m%r" % (self.UseCaseName, UseCase_number, self.parameterPacket))
        return self.parameterPacket




    def ListOfComplaintsProcess(self,cache_parameterPacket):
        """
        投诉流程，初始化参数包（针对电子表格）
        :return:
        """
        Their_module = None;office_name = None;appletName = None;userRight = None;Subordinate = None
        selected_officeID=None;dateClosed=None;startDate=None;dateParameter=None;titleAndcontent=None
        Subordinate_procedure=None;initial_userinfo=None;complaint_Title=None;complaint_content=None
        complaintID=None;complainantID=None;By_complainantID=None;dateCreated=None;updatedDate=None
        complaintStatus=None;phone=None;dispose=None;level=None;processing_Scheme=None
        """取出筛选信息"""
        UseCase_number = self.useCase["用例编号"];           testPoint_spreadsheet = self.useCase["测试点"]
        appletName = self.useCase["平台名称"];               Their_module = self.useCase["所属模块"]
        userRight = self.useCase["用户权限"];                user_type = self.useCase["用户类型"]
        office_name = self.useCase["用户所在单位"];          Subordinate_procedure = self.useCase["所属步骤"]
        dateRange = self.useCase["日期范围"]       ;         Subordinate_port = self.useCase["所属接口"]
        # dateCreated = passShh_connectToServer("%Y-%m-%d").Get_server_time()   # 获取创建日期
        dateCreated =time.strftime("%Y-%m-%d")
        if Subordinate_procedure=="普通用户手动新增投诉" or Subordinate_procedure=="用户管理员手动新增投诉":
            complaint_Title = professionalWork_data_dispose("投诉标题新增投诉").GenerateUnrepeatedTitles("投诉模块", "新增投诉标题") # 获取投诉标题
            complaint_content ="投诉内容,%r在内蒙古自治区包头市的大青山深处，五当召坐落于此。"%complaint_Title   # 获取投诉内容
        elif Subordinate_procedure=="服务台受理投诉，指派被投诉人：运维工程师（四组）" or Subordinate_procedure == "服务台受理投诉，指派被投诉人：运维组长（四组）":
            complaint_Title = professionalWork_data_dispose("服务台用受理投诉").GenerateUnrepeatedTitles("投诉模块", "受理投诉标题")  # 获取投诉标题
            # 获取被投诉人信息
            if Subordinate_procedure == "服务台受理投诉，指派被投诉人：运维组长（四组）":
                By_complainant = {"用户权限": "运维组长", "用户所在单位": "四组"}  # 获取被投诉人参数
            else:
                By_complainant={"用户权限": "运维工程师", "用户所在单位": "四组"}     # 获取被投诉人参数
            By_list_dicti_userinfo = userinfo_acquire_And_Dispose(By_complainant).UserDetails() # 获取被投诉人信息
            cache_parameterPacket["被投诉人ID"] = By_list_dicti_userinfo[0]["用户ID"] # 获取被投诉人ID
            cache_parameterPacket["投诉内容"] = "投诉内容,%r没有解决问题，维修工程师没有服务器账号密码，无法解决问题，走了，然后就没人来了。" % complaint_Title  # 获取投诉内容
            cache_parameterPacket["更新日期"]=dateCreated      # 投诉更新日期
            cache_parameterPacket["处理方案"]= "处理方案,%r已和老师沟通，有其他单位的人去处理过他们知道服务器账号密码，以为是我们的人处理的，下次那个单位的人在去学校让学校找他们要账号密码我再过去处理。" % complaint_Title  # 获取投诉处理方案
            cache_parameterPacket["投诉级别"]= "2"    # 投诉级别
            cache_parameterPacket["操作"] = "1"  # 操作
        elif Subordinate_procedure == "运维工程师填写处理结果" or Subordinate_procedure == "运维组长填写处理结果":
            cache_parameterPacket["更新日期"] = dateCreated
            cache_parameterPacket["处理结果"]= "处理结果,%r那个高拍仪摄像头有问题，我去后勤问了廖老师，他那边没有好的可以换了，廖老师自己也去教室看了情况。" % complaint_Title  # 获取投诉处理方案
            cache_parameterPacket["操作"] = "2"  # 操作
        elif Subordinate_procedure == "服务台再次受理投诉，指派被投诉人：运维工程师（四组）" or Subordinate_procedure == "服务台再次受理投诉，指派被投诉人：运维组长（四组）":
            By_complainant = {"用户权限": "运维工程师", "用户所在单位": "四组"}  # 获取被投诉人参数
            By_list_dicti_userinfo = userinfo_acquire_And_Dispose(By_complainant).UserDetails() #  # 获取被投诉人信息
            cache_parameterPacket["被投诉人ID"] = By_list_dicti_userinfo[0]["用户ID"]  # 获取被投诉人ID
            cache_parameterPacket["更新日期"] = dateCreated
            cache_parameterPacket["操作"] = "1"  # 操作
            cache_parameterPacket["处理方案"] = "再次填写处理方案,%r已跟老师和工程师了解清楚情况，工程师过去的时候学校有人在维修电路，工程师和老师打过电话说学校的人电路弄好了在过去处理电脑故障，现在工程师回学校处理了。" % complaint_Title  # 获取投诉处理方案
        elif Subordinate_procedure == "运维工程师修改处理结果" or Subordinate_procedure == "运维组长修改处理结果":
            cache_parameterPacket["更新日期"] = dateCreated
            cache_parameterPacket["处理结果"] = "再次填写处理结果,%r这病毒感染引起电脑C盘满无法正常使，已把电脑杀毒处理，清除c盘垃圾文件，电脑正常使用，并培训老师如果杀毒。正确使用设备。" % complaint_Title  # 获取投诉处理方案
            cache_parameterPacket["操作"] = "2"  # 操作
        elif Subordinate_procedure == "普通用户确认处理结果：未解决" or Subordinate_procedure == "用户管理员确认处理结果：未解决":
            cache_parameterPacket["更新日期"] = dateCreated
            cache_parameterPacket["操作"] = "4"  # 操作
        elif Subordinate_procedure == "普通用户再次确认处理结果：已解决" or Subordinate_procedure == "用户管理员确认处理结果：已解决":
            cache_parameterPacket["更新日期"] = dateCreated
            cache_parameterPacket["操作"] = "3"  # 操作
        """根据筛选条件列表取出用户信息"""
        initial_userinfo = {"用户权限": userRight, "用户所在单位": office_name}
        list_dicti_userinfo = userinfo_acquire_And_Dispose(initial_userinfo).UserDetails() # 获取被投诉人信息 # 获取用户信息
        dicti_userinfo = list_dicti_userinfo[0]  # 用户打包信息
        loginName = dicti_userinfo["登录名"];roleName = dicti_userinfo["用户权限"];userid = dicti_userinfo["用户ID"]
        """编译日期范围"""
        if dateRange != "空":
            dict_date =TimeFormat(dateRange).dateParameter_actualDate()  # 根据日期范围获取具体的日期（开始日期和结束日期）
            startDate = dict_date["开始日期"][0];dateClosed = dict_date["结束日期"][0]  # 获取开始日期和结束日期
        """获取所选单位ID"""
        if user_type == "外部":  # 获取测试报告登录用户信息 ；# 单位名称转化成单位ID
            userinfo = "用户登录名：%r；用户权限：%r；用户ID：%r" % (loginName, roleName, userid)
        else:
            userinfo = "用户登录名：%r；用户权限：%r；用户ID：%r" % (loginName, roleName, userid)

        """获取测试报告参数"""
        dictionaryKeys = self.tableName + UseCase_number  # 获取字典的键
        testResult = "返回投诉模块清单页面数据，实际值不等于预期值，测试失败"  # 获取结果

        """获取新增或者修改接口的参数"""
        if Subordinate_procedure == "普通用户手动新增投诉" or Subordinate_procedure == "用户管理员手动新增投诉":  # 打包新增投诉的参数包
            cache_parameterPacket = {"所属接口": Subordinate_port, "平台名称": appletName, "所属模块": Their_module, "检查登录用户信息": userinfo,"用例名称": self.UseCaseName,
                                "测试结果": testResult, "测试点": testPoint_spreadsheet,"字典的键": dictionaryKeys, "重复筛选参数": Their_module,
                                "开始日期":startDate,"结束日期":dateClosed,"投诉标题":complaint_Title,"投诉内容":complaint_content,"投诉单ID":complaintID,
                                "投诉人ID":complainantID,"被投诉人ID":By_complainantID,"创建日期":dateCreated,"更新日期":updatedDate,"投诉状态":complaintStatus,
                                "投诉级别":level,"处理方案":processing_Scheme,"投诉人电话":phone,"处理结果":None,"操作":dispose}
        """合并用户信息参数包，生成新的参数包"""
        self.parameterPacket = dict(dicti_userinfo, **cache_parameterPacket)
        print("\033[1;34;40m获取用例“%r”，用例编号“%r”的参数包：\033[0m\033[4;35;40m%r" % (self.UseCaseName, UseCase_number, self.parameterPacket))
        return self.parameterPacket


    def WorkOrderProcess(self,cache_parameterPacket):
        """
        工单流程，初始化参数包（针对电子表格）
        :return:
        """
        Their_module = None;office_name = None;appletName = None;userRight = None
        dateClosed=None;startDate=None;Subordinate_procedure=None;initial_userinfo=None;dateCreated=None
        workOrder_Title=None;faultTypeName=None;faultTypeID=None;AppointmentTime=None;describe=None;UseCase_number=None
        ticketServeType=None;fficeNumber=None;inOutTicket=None;TaskToDealWith=None;list_dicti_handler=None
        """取出筛选信息"""
        UseCase_number = self.useCase["用例编号"];           testPoint_spreadsheet = self.useCase["测试点"]
        appletName = self.useCase["平台名称"];               Their_module = self.useCase["所属模块"]
        userRight = self.useCase["用户权限"];                user_type = self.useCase["用户类型"]
        office_name = self.useCase["用户所在单位"];          Subordinate_procedure = self.useCase["所属步骤"]
        dateRange = self.useCase["日期范围"]       ;         Subordinate_port = self.useCase["所属接口"]
        # dateCreated = passShh_connectToServer("%Y-%m-%d").Get_server_time()  # 获取服务器日期
        dateCreated=time.strftime("%Y-%m-%d")
        """根据筛选条件列表取出用户信息"""
        initial_userinfo = {"用户权限": userRight, "用户所在单位": office_name}
        list_dicti_userinfo =  userinfo_acquire_And_Dispose(initial_userinfo).UserDetails() # 获取用户信息
        dicti_userinfo = list_dicti_userinfo[0]  # 用户打包信息
        loginName = dicti_userinfo["登录名"];roleName = dicti_userinfo["用户权限"];userid = dicti_userinfo["用户ID"];JSESSIONID = dicti_userinfo["登录用户JSESSIONID"]
        """获取工作流参数"""
        if Subordinate_procedure!= "普通用户-一键报修" :
            cache_parameterPacket_userinfo = dict(dicti_userinfo, **cache_parameterPacket)  # 合并（替换参数包里的登录用户信息）
            TransferRecord, post_Parameter = excessive_parameter(Subordinate_procedure).acquire_TransferRecord(cache_parameterPacket_userinfo)  # 获取工单列表工作流参数
            cache_parameterPacket = dict(TransferRecord, **cache_parameterPacket)  # 合并（替换参数包关于工作流的参数信息）
        """根据步骤获取参数"""
        if Subordinate_procedure=="普通用户-一键报修" or Subordinate_procedure=="":
            workOrder_Title = professionalWork_data_dispose( "用户工单标题").GenerateUnrepeatedTitles("工单流程模块", "新增工单标题")  # 获取工单标题
            list_dicti_fault, sql = dataProcessing("inquire_faultTypeID").user_name(None);faultType = random.choice(list_dicti_fault)
            faultTypeID = faultType["故障类型ID"];faultTypeName = faultType["故障类型名称"]   # 获取故障类型ID和故障类型名称
            AppointmentTimeList = TimeFormat(dateCreated).workOrderRepairs_AppointmentTime()
            AppointmentTime = random.choice(AppointmentTimeList)  # 获取预约时间段
            describe = "工单描述,“%r”108展台照明灯接触不良，试卷投影后，大屏幕一直晃动。" % workOrder_Title  # 获取工单描述
            ticketServeType = "0"     #工单服务类型
            fficeNumber = professionalWork_data_dispose().Generate_the_workOrderNumber(dicti_userinfo) # 生成预期的工单编号
            inOutTicket="1"     # 工单范围
        elif Subordinate_procedure == "用户管理员-内部处理":
            cache_parameterPacket["处理类型"] = "SigningAndProcess"  # sjTicketFlow接口：处理类型processType=SigningAndProcess
            cache_parameterPacket["工单状态"] = "0"  # 工单状态
            cache_parameterPacket["工单处理人ID"] = None  # 工单处理人ID
            cache_parameterPacket["工单改派人ID"] = None  # 工单改派人ID
            cache_parameterPacket["预约开始时间"] = cache_parameterPacket["预约日期"]+" " + "00:00:00"
            cache_parameterPacket["预约结束时间"] = None  # 预约结束时间
            cache_parameterPacket["确认开始服务时间"] = None  # 确认开始服务时间
            cache_parameterPacket["确认结束服务时间"] = None  # 确认结束服务时间
            cache_parameterPacket["工单范围"] = "1"  # 工单范围(外部工单：0;内部工单：1;)
            cache_parameterPacket["意见状态"] = "no"  # 意见状态(yes/no)
            cache_parameterPacket["任务意见"] = None  # 任务意见
            cache_parameterPacket["内部处理结果"] =  "内部处理结果,%r插头没有插。" % workOrder_Title  # 获取内部处理结果
            cache_parameterPacket["评级"] = None  # 评级
            cache_parameterPacket["用户评价"]  = None  # 用户评价
            cache_parameterPacket["事件解决方案"]  = None  # 事件解决方案
            cache_parameterPacket["挂起下拉框理由"]  = None  # 挂起下拉框理由
            cache_parameterPacket["挂起状态字段"] = None  # 挂起状态字段(记录它挂起之前的状态，用于解挂跳转之前的节点用,(有值时true))
            cache_parameterPacket["改派人群组ID"] = None  # 获取用户的群组ID
            cache_parameterPacket["外协处理描述"]=None
        elif Subordinate_procedure=="用户管理员-外协处理":
            cache_parameterPacket["处理类型"] = "SigningAndProcess"  # sjTicketFlow接口：处理类型processType=SigningAndProcess
            cache_parameterPacket["工单状态"] = "0"  # 工单状态
            cache_parameterPacket["工单处理人ID"] = None  # 工单处理人ID
            cache_parameterPacket["工单改派人ID"] = None  # 工单改派人ID
            cache_parameterPacket["预约开始时间"] = cache_parameterPacket["预约日期"] + " " + "00:00:00"
            cache_parameterPacket["预约结束时间"] = None  # 预约结束时间
            cache_parameterPacket["确认开始服务时间"] = None  # 确认开始服务时间
            cache_parameterPacket["确认结束服务时间"] = None  # 确认结束服务时间
            cache_parameterPacket["工单范围"] = "1"  # 工单范围(外部工单：0;内部工单：1;)
            cache_parameterPacket["意见状态"] = "yes"  # 意见状态(yes/no)
            cache_parameterPacket["任务意见"] = None  # 任务意见
            cache_parameterPacket["内部处理结果"] = None
            cache_parameterPacket["评级"] = None  # 评级
            cache_parameterPacket["用户评价"] = None  # 用户评价
            cache_parameterPacket["事件解决方案"] = None  # 事件解决方案
            cache_parameterPacket["挂起下拉框理由"] = None  # 挂起下拉框理由
            cache_parameterPacket["挂起状态字段"] = None  # 挂起状态字段(记录它挂起之前的状态，用于解挂跳转之前的节点用,(有值时true))
            cache_parameterPacket["改派人群组ID"] = None  # 获取用户的群组ID
            cache_parameterPacket["外协处理描述"]= "外协处理描述,%r无法处理，只有申请外协。" % workOrder_Title  # 获取外协处理描述
        elif Subordinate_procedure=="组长(四组)-待响应-改派-工程师(四组)":
            # 获取工单改派人ID
            initial_handler = {"用户权限": "运维工程师", "用户所在单位": "四组"}
            list_dicti_handler = userinfo_acquire_And_Dispose(initial_handler).UserDetails() # 获取用户信息
            cache_parameterPacket["处理类型"] = None  # sjTicketFlow接口：处理类型processType=SigningAndProcess
            cache_parameterPacket["工单状态"] = "2"  # 工单状态
            cache_parameterPacket["工单处理人ID"] = None  # 工单处理人ID
            cache_parameterPacket["工单改派人ID"] = list_dicti_handler[0]["用户ID"]  # 获取工单改派人ID
            cache_parameterPacket["预约开始时间"] = cache_parameterPacket["预约日期"] + " " + "00:00:00"
            cache_parameterPacket["预约结束时间"] = None  # 预约结束时间
            cache_parameterPacket["确认开始服务时间"] = dateCreated  # 确认开始服务时间
            cache_parameterPacket["确认结束服务时间"] = random.choice(["0", "1", "2"])  # 确认结束服务时间
            cache_parameterPacket["工单范围"] = "0"  # 工单范围(外部工单：0;内部工单：1;)
            cache_parameterPacket["意见状态"] = "yes"  # 意见状态(yes/no)
            cache_parameterPacket["任务意见"] =  "改派说明,%r设备又坏了，与之前一样的问题。" % workOrder_Title   # 任务意见
            cache_parameterPacket["内部处理结果"] = None
            cache_parameterPacket["评级"] = None  # 评级
            cache_parameterPacket["用户评价"] = None  # 用户评价
            cache_parameterPacket["事件解决方案"] = None  # 事件解决方案
            cache_parameterPacket["挂起下拉框理由"] = None  # 挂起下拉框理由
            cache_parameterPacket["挂起状态字段"] = None  # 挂起状态字段(记录它挂起之前的状态，用于解挂跳转之前的节点用,(有值时true))
            cache_parameterPacket["改派人群组ID"] = None  # 获取用户的群组ID
            cache_parameterPacket["外协处理描述"] = None  # 获取外协处理描述
        elif Subordinate_procedure == "组长（四组）-待响应-接单":
            cache_parameterPacket["处理类型"] = None  # sjTicketFlow接口：处理类型processType=SigningAndProcess
            cache_parameterPacket["工单状态"] = "2"  # 工单状态
            cache_parameterPacket["工单处理人ID"] = None  # 工单处理人ID
            cache_parameterPacket["工单改派人ID"] = None  # 获取工单改派人ID
            cache_parameterPacket["预约开始时间"] = cache_parameterPacket["预约日期"] + " " + "00:00:00"
            cache_parameterPacket["预约结束时间"] = None  # 预约结束时间
            cache_parameterPacket["确认开始服务时间"] = dateCreated  # 确认开始服务时间
            cache_parameterPacket["确认结束服务时间"] = random.choice(["0", "1", "2"])  # 确认结束服务时间
            cache_parameterPacket["工单范围"] = "0"  # 工单范围(外部工单：0;内部工单：1;)
            cache_parameterPacket["意见状态"] = "no"  # 意见状态(yes/no)
            cache_parameterPacket["任务意见"] = None  # 任务意见
            cache_parameterPacket["内部处理结果"] = None
            cache_parameterPacket["评级"] = None  # 评级
            cache_parameterPacket["用户评价"] = None  # 用户评价
            cache_parameterPacket["事件解决方案"] = None  # 事件解决方案
            cache_parameterPacket["挂起下拉框理由"] = None  # 挂起下拉框理由
            cache_parameterPacket["挂起状态字段"] = None  # 挂起状态字段(记录它挂起之前的状态，用于解挂跳转之前的节点用,(有值时true))
            cache_parameterPacket["改派人群组ID"] = None  # 获取用户的群组ID
            cache_parameterPacket["外协处理描述"] = None  # 获取外协处理描述
        elif  Subordinate_procedure == "工程师（四组）-预约中-到达现场" or Subordinate_procedure == "组长（四组）-预约中-到达现场" or \
                Subordinate_procedure == "工程师（五组）-预约中-到达现场":
            cache_parameterPacket["处理类型"] = None  # sjTicketFlow接口：处理类型processType=SigningAndProcess
            cache_parameterPacket["工单状态"] = "3"  # 工单状态
            cache_parameterPacket["工单改派人ID"] = None  # 获取工单改派人ID
            cache_parameterPacket["预约开始时间"] = cache_parameterPacket["预约日期"] + " " + "00:00:00"
            cache_parameterPacket["预约结束时间"] = None  # 预约结束时间
            cache_parameterPacket["工单范围"] = "0"  # 工单范围(外部工单：0;内部工单：1;)
            cache_parameterPacket["意见状态"] = "yes"  # 意见状态(yes/no)
            cache_parameterPacket["任务意见"] = None  # 任务意见
            cache_parameterPacket["内部处理结果"] = None
            cache_parameterPacket["评级"] = None  # 评级
            cache_parameterPacket["用户评价"] = None  # 用户评价
            cache_parameterPacket["事件解决方案"] = None  # 事件解决方案
            cache_parameterPacket["挂起下拉框理由"] = None  # 挂起下拉框理由
            cache_parameterPacket["挂起状态字段"] = None  # 挂起状态字段(记录它挂起之前的状态，用于解挂跳转之前的节点用,(有值时true))
            cache_parameterPacket["改派人群组ID"] = None  # 获取用户的群组ID
            cache_parameterPacket["外协处理描述"] = None  # 获取外协处理描述
        elif Subordinate_procedure == "工程师(四组)-处理中-完成工单" or Subordinate_procedure == "组长(四组)-处理中-完成工单" or Subordinate_procedure == "工程师(五组)-处理中-完成工单":
            cache_parameterPacket["处理类型"] = None  # sjTicketFlow接口：处理类型processType=SigningAndProcess
            cache_parameterPacket["工单状态"] = "5"  # 工单状态
            cache_parameterPacket["工单改派人ID"] = None  # 获取工单改派人ID
            cache_parameterPacket["预约开始时间"] = cache_parameterPacket["预约日期"] + " " + "00:00:00"
            cache_parameterPacket["预约结束时间"] = None  # 预约结束时间
            cache_parameterPacket["工单范围"] = "0"  # 工单范围(外部工单：0;内部工单：1;)
            cache_parameterPacket["意见状态"] = "yes"  # 意见状态(yes/no)
            cache_parameterPacket["任务意见"] = None  # 任务意见
            cache_parameterPacket["内部处理结果"] = None
            cache_parameterPacket["评级"] = None  # 评级
            cache_parameterPacket["用户评价"] = None  # 用户评价
            cache_parameterPacket["事件解决方案"] ="事件解决方案,%r卸载不常用软件调整一体机信号源接口，两个班级设备正常使用。" % workOrder_Title   # 事件解决方案
            cache_parameterPacket["挂起下拉框理由"] = None  # 挂起下拉框理由
            cache_parameterPacket["挂起状态字段"] = None  # 挂起状态字段(记录它挂起之前的状态，用于解挂跳转之前的节点用,(有值时true))
            cache_parameterPacket["改派人群组ID"] = None  # 获取用户的群组ID
            cache_parameterPacket["外协处理描述"] = None  # 获取外协处理描述
        elif Subordinate_procedure == "工程师(四组)-预约中-申请挂起" or Subordinate_procedure == "工程师(五组)-预约中-申请挂起" or Subordinate_procedure == "组长(四组)-预约中-申请挂起" or \
             Subordinate_procedure == "工程师(四组)-处理中-申请挂起" or Subordinate_procedure == "组长(四组)-处理中-申请挂起" or Subordinate_procedure == "工程师(五组)-处理中-申请挂起":
            # 生成挂起下拉框理由,调用接口获取数据库挂起下拉框理由参数
            list_hang_up = TheRepairOrderInterface(JSESSIONID, None).getDictByKey()
            list_hangUpComment = []
            for hang_up in list_hang_up:
                hang = hang_up["value"]
                list_hangUpComment.append(hang)
            cache_parameterPacket["处理类型"] = None  # sjTicketFlow接口：处理类型processType=SigningAndProcess
            cache_parameterPacket["工单改派人ID"] = None  # 获取工单改派人ID
            cache_parameterPacket["预约开始时间"] = cache_parameterPacket["预约日期"] + " " + "00:00:00"
            cache_parameterPacket["预约结束时间"] = None  # 预约结束时间
            cache_parameterPacket["工单范围"] = "0"  # 工单范围(外部工单：0;内部工单：1;)
            cache_parameterPacket["意见状态"] = "no"  # 意见状态(yes/no)
            cache_parameterPacket["任务意见"] = "申请挂起描述:,%r没有带工具，所有今天无法解决。" % workOrder_Title     # 任务意见
            cache_parameterPacket["内部处理结果"] = None
            cache_parameterPacket["评级"] = None  # 评级
            cache_parameterPacket["用户评价"] = None  # 用户评价
            cache_parameterPacket["事件解决方案"] = None  # 事件解决方案
            cache_parameterPacket["挂起下拉框理由"] = random.choice(list_hangUpComment)  # 挂起下拉框理由
            cache_parameterPacket["挂起状态字段"] = None  # 挂起状态字段(记录它挂起之前的状态，用于解挂跳转之前的节点用,(有值时true))
            cache_parameterPacket["改派人群组ID"] = None  # 获取用户的群组ID
            cache_parameterPacket["外协处理描述"] = None  # 获取外协处理描述
        elif Subordinate_procedure == "组长(四组)-预约中-审核挂起-不通过" or Subordinate_procedure == "服务台-预约中-审核挂起-不通过" or Subordinate_procedure == "组长(四组)-处理中-审核挂起-不通过" \
                or Subordinate_procedure == "服务台-处理中-审核挂起-不通过" or  Subordinate_procedure == "组长(五组)-处理中-审核挂起-不通过":
            cache_parameterPacket["处理类型"] = "SigningAndProcess"  # sjTicketFlow接口：处理类型processType=SigningAndProcess
            cache_parameterPacket["工单改派人ID"] = None  # 获取工单改派人ID
            cache_parameterPacket["预约开始时间"] = cache_parameterPacket["预约日期"] + " " + "00:00:00"
            cache_parameterPacket["预约结束时间"] = None  # 预约结束时间
            cache_parameterPacket["工单范围"] = "0"  # 工单范围(外部工单：0;内部工单：1;)
            cache_parameterPacket["意见状态"] = "no"  # 意见状态(yes/no)
            cache_parameterPacket["任务意见"] = "审核挂起描述:,%r确认所述为不实，不同意挂起。" % workOrder_Title     # 任务意见
            cache_parameterPacket["内部处理结果"] = None
            cache_parameterPacket["评级"] = None  # 评级
            cache_parameterPacket["用户评价"] = None  # 用户评价
            cache_parameterPacket["事件解决方案"] = None  # 事件解决方案
            cache_parameterPacket["挂起下拉框理由"] = None  # 挂起下拉框理由
            cache_parameterPacket["挂起状态字段"] = "0"  # 挂起状态字段(记录它挂起之前的状态，用于解挂跳转之前的节点用,(有值时true))
            cache_parameterPacket["改派人群组ID"] = None  # 获取用户的群组ID
            cache_parameterPacket["外协处理描述"] = None  # 获取外协处理描述
        elif Subordinate_procedure == "组长(四组)-预约中-审核挂起-通过" or Subordinate_procedure == "服务台-预约中-审核挂起-通过" or Subordinate_procedure == "组长(四组)-处理中-审核挂起-通过" or \
             Subordinate_procedure == "服务台-处理中-审核挂起-通过" :
            cache_parameterPacket["处理类型"] = "SigningAndProcess"  # sjTicketFlow接口：处理类型processType=SigningAndProcess
            cache_parameterPacket["工单改派人ID"] = None  # 获取工单改派人ID
            cache_parameterPacket["预约开始时间"] = cache_parameterPacket["预约日期"] + " " + "00:00:00"
            cache_parameterPacket["预约结束时间"] = None  # 预约结束时间
            cache_parameterPacket["工单范围"] = "0"  # 工单范围(外部工单：0;内部工单：1;)
            cache_parameterPacket["意见状态"] = "yes"  # 意见状态(yes/no)
            cache_parameterPacket["任务意见"] = "审核挂起描述:,“%r”确认所述为实时，同意挂起。" % workOrder_Title  # 任务意见
            cache_parameterPacket["内部处理结果"] = None
            cache_parameterPacket["评级"] = None  # 评级
            cache_parameterPacket["用户评价"] = None  # 用户评价
            cache_parameterPacket["事件解决方案"] = None  # 事件解决方案
            cache_parameterPacket["挂起下拉框理由"] = None  # 挂起下拉框理由
            cache_parameterPacket["挂起状态字段"] = "0"  # 挂起状态字段(记录它挂起之前的状态，用于解挂跳转之前的节点用,(有值时true))
            cache_parameterPacket["改派人群组ID"] = None  # 获取用户的群组ID
            cache_parameterPacket["外协处理描述"] = None  # 获取外协处理描述
        elif Subordinate_procedure == "服务台-已挂起-解挂":
            cache_parameterPacket["处理类型"] = "SigningAndProcess"  # sjTicketFlow接口：处理类型processType=SigningAndProcess
            cache_parameterPacket["工单状态"] = "6"  # 工单状态
            cache_parameterPacket["工单改派人ID"] = None  # 获取工单改派人ID
            cache_parameterPacket["预约开始时间"] = cache_parameterPacket["预约日期"] + " " + "00:00:00"
            cache_parameterPacket["预约结束时间"] = None  # 预约结束时间
            cache_parameterPacket["工单范围"] = "0"  # 工单范围(外部工单：0;内部工单：1;)
            cache_parameterPacket["意见状态"] = "yes"  # 意见状态(yes/no)
            cache_parameterPacket["任务意见"] = "解挂描述,%r今天可以解决问题。" % workOrder_Title  # 任务意见
            cache_parameterPacket["内部处理结果"] = None
            cache_parameterPacket["评级"] = None  # 评级
            cache_parameterPacket["用户评价"] = None  # 用户评价
            cache_parameterPacket["事件解决方案"] = None  # 事件解决方案
            cache_parameterPacket["挂起下拉框理由"] = None  # 挂起下拉框理由
            cache_parameterPacket["挂起状态字段"] = cache_parameterPacket["工单在挂起前的状态"]  # 挂起状态字段(记录它挂起之前的状态，用于解挂跳转之前的节点用,(有值时true))
            cache_parameterPacket["改派人群组ID"] = None  # 获取用户的群组ID
            cache_parameterPacket["外协处理描述"] = None  # 获取外协处理描述
        elif Subordinate_procedure == "服务台(一号)-已挂起-改派-工程师(四组)" :
            # 获取工单改派人ID
            initial_handler = {"用户权限": "运维工程师", "用户所在单位": "四组"}
            list_dicti_handler = userinfo_acquire_And_Dispose(initial_handler).UserDetails()# 获取用户信息
            # 获取群组ID，根据处理人用户ID获取群组ID或者根据单位ID获取群组ID
            list_dicti_handler_ID, sql = dataProcessing("userID_groupID_sort").user_name(list_dicti_handler[0]["用户ID"])
            cache_parameterPacket["处理类型"] = "SigningAndProcess"  # sjTicketFlow接口：处理类型processType=SigningAndProcess
            cache_parameterPacket["工单状态"] = "6"  # 工单状态
            cache_parameterPacket["工单改派人ID"] = list_dicti_handler  # 获取工单改派人ID
            cache_parameterPacket["预约开始时间"] = cache_parameterPacket["预约日期"] + " " + "00:00:00"
            cache_parameterPacket["预约结束时间"] = None  # 预约结束时间
            cache_parameterPacket["工单范围"] = "0"  # 工单范围(外部工单：0;内部工单：1;)
            cache_parameterPacket["意见状态"] = "no"  # 意见状态(yes/no)
            cache_parameterPacket["任务意见"] = "服务台改派描述,“%r”之前的工程师请假。" % workOrder_Title  # 任务意见
            cache_parameterPacket["内部处理结果"] = None
            cache_parameterPacket["评级"] = None  # 评级
            cache_parameterPacket["用户评价"] = None  # 用户评价
            cache_parameterPacket["事件解决方案"] = None  # 事件解决方案
            cache_parameterPacket["挂起下拉框理由"] = None  # 挂起下拉框理由
            cache_parameterPacket["挂起状态字段"] = cache_parameterPacket["工单在挂起前的状态"]   # 挂起状态字段(记录它挂起之前的状态，用于解挂跳转之前的节点用,(有值时true))
            cache_parameterPacket["改派人群组ID"] = list_dicti_handler_ID[0]["群组ID"]  # 获取用户的群组ID
            cache_parameterPacket["外协处理描述"] = None  # 获取外协处理描述
        elif Subordinate_procedure == "服务台(一号)-已挂起-改派-工程师(五组)":
            # 获取工单改派人ID
            initial_handler = {"用户权限": "运维工程师", "用户所在单位": "五组"}
            list_dicti_handler = userinfo_acquire_And_Dispose(initial_handler).UserDetails()# 获取用户信息
            # 获取群组ID，根据处理人用户ID获取群组ID或者根据单位ID获取群组ID
            list_dicti_handler_ID, sql = dataProcessing("userID_groupID_sort").user_name(list_dicti_handler)
            cache_parameterPacket["处理类型"] = "SigningAndProcess"  # sjTicketFlow接口：处理类型processType=SigningAndProcess
            cache_parameterPacket["工单状态"] = "6"  # 工单状态
            cache_parameterPacket["工单改派人ID"] = list_dicti_handler  # 获取工单改派人ID
            cache_parameterPacket["预约开始时间"] = cache_parameterPacket["预约日期"] + " " + "00:00:00"
            cache_parameterPacket["预约结束时间"] = None  # 预约结束时间
            cache_parameterPacket["工单范围"] = "0"  # 工单范围(外部工单：0;内部工单：1;)
            cache_parameterPacket["意见状态"] = "no"  # 意见状态(yes/no)
            cache_parameterPacket["任务意见"] = "服务台改派描述,“%r”之前的工程师请假。" % workOrder_Title  # 任务意见
            cache_parameterPacket["内部处理结果"] = None
            cache_parameterPacket["评级"] = None  # 评级
            cache_parameterPacket["用户评价"] = None  # 用户评价
            cache_parameterPacket["事件解决方案"] = None  # 事件解决方案
            cache_parameterPacket["挂起下拉框理由"] = None  # 挂起下拉框理由
            cache_parameterPacket["挂起状态字段"] = cache_parameterPacket["工单在挂起前的状态"]  # 挂起状态字段(记录它挂起之前的状态，用于解挂跳转之前的节点用,(有值时true))
            cache_parameterPacket["改派人群组ID"] = list_dicti_handler_ID[0]["群组ID"]  # 获取用户的群组ID
            cache_parameterPacket["外协处理描述"] = None  # 获取外协处理描述
        elif Subordinate_procedure == "普通用户-内部-评论":
            cache_parameterPacket["处理类型"] = None  # sjTicketFlow接口：处理类型processType=SigningAndProcess
            cache_parameterPacket["工单状态"] = "1"  # 工单状态
            cache_parameterPacket["工单处理人ID"] = None  # 工单处理人ID
            cache_parameterPacket["工单改派人ID"] = None  # 获取工单改派人ID
            cache_parameterPacket["预约开始时间"] = None
            cache_parameterPacket["预约结束时间"] = None  # 预约结束时间
            cache_parameterPacket["确认开始服务时间"] = None  # 确认开始服务时间
            cache_parameterPacket["确认结束服务时间"] = None # 确认结束服务时间
            cache_parameterPacket["工单范围"] = "1"  # 工单范围(外部工单：0;内部工单：1;)
            cache_parameterPacket["意见状态"] = "yes"  # 意见状态(yes/no)
            cache_parameterPacket["任务意见"] = None  # 任务意见
            cache_parameterPacket["内部处理结果"] = None
            cache_parameterPacket["评级"] = random.choice(["3", "4", "5"])   # 评级
            cache_parameterPacket["用户评价"] = "用户评价,内部，“%r”问题解决。" % workOrder_Title   # 用户评价
            cache_parameterPacket["事件解决方案"] = None  # 事件解决方案
            cache_parameterPacket["挂起下拉框理由"] = None  # 挂起下拉框理由
            cache_parameterPacket["挂起状态字段"] = None  # 挂起状态字段(记录它挂起之前的状态，用于解挂跳转之前的节点用,(有值时true))
            cache_parameterPacket["改派人群组ID"] = None  # 获取用户的群组ID
            cache_parameterPacket["外协处理描述"] = None  # 获取外协处理描述
        elif Subordinate_procedure == "普通用户-外部-评论":
            cache_parameterPacket["处理类型"] = None  # sjTicketFlow接口：处理类型processType=SigningAndProcess
            cache_parameterPacket["工单状态"] = "7"  # 工单状态
            cache_parameterPacket["工单改派人ID"] = None  # 获取工单改派人ID
            cache_parameterPacket["预约开始时间"] = None  # 预约开始时间
            cache_parameterPacket["预约结束时间"] = None  # 预约结束时间
            cache_parameterPacket["确认开始服务时间"] = None  # 确认开始服务时间
            cache_parameterPacket["确认结束服务时间"] = None  # 确认结束服务时间
            cache_parameterPacket["工单范围"] = "0"  # 工单范围(外部工单：0;内部工单：1;)
            cache_parameterPacket["意见状态"] = "yes"  # 意见状态(yes/no)
            cache_parameterPacket["任务意见"] = None  # 任务意见
            cache_parameterPacket["内部处理结果"] = None
            cache_parameterPacket["评级"] = random.choice(["3", "4", "5"])  # 评级
            cache_parameterPacket["用户评价"] ="用户评价,外协“%r”问题解决。" % workOrder_Title   # 用户评价
            cache_parameterPacket["事件解决方案"] = None  # 事件解决方案
            cache_parameterPacket["挂起下拉框理由"] = None  # 挂起下拉框理由
            cache_parameterPacket["挂起状态字段"] = None  # 挂起状态字段(记录它挂起之前的状态，用于解挂跳转之前的节点用,(有值时true))
            cache_parameterPacket["改派人群组ID"] = None  # 获取用户的群组ID
            cache_parameterPacket["外协处理描述"] = None  # 获取外协处理描述
        """编译日期范围"""
        if dateRange != "空":
            dict_date =TimeFormat(dateRange).dateParameter_actualDate()  # 根据日期范围获取具体的日期（开始日期和结束日期）
            startDate = dict_date["开始日期"][0];dateClosed = dict_date["结束日期"][0]  # 获取开始日期和结束日期
        """获取所选单位ID"""
        if user_type == "外部":  # 获取测试报告登录用户信息 ；# 单位名称转化成单位ID
            userinfo = "用户登录名：%r；用户权限：%r；用户ID：%r" % (loginName, roleName, userid)
        else:
            userinfo = "用户登录名：%r；用户权限：%r；用户ID：%r" % (loginName, roleName, userid)
        """获取测试报告参数"""
        dictionaryKeys = self.tableName + UseCase_number  # 获取字典的键
        testResult = "步骤“%r”操作失败，测试失败"%Subordinate_procedure  # 获取结果
        """获取新增或者修改接口的参数"""
        if Subordinate_procedure=="普通用户-一键报修" or Subordinate_procedure=="":  # 打包新增投诉的参数包
            cache_parameterPacket = {"所属接口": Subordinate_port, "平台名称": appletName, "所属模块": Their_module, "检查登录用户信息": userinfo,"用例名称": self.UseCaseName,
                                     "测试结果": testResult, "测试点": testPoint_spreadsheet,"字典的键": dictionaryKeys, "重复筛选参数": Their_module, "开始日期":startDate,"结束日期":dateClosed,
                                     "工单标题":workOrder_Title,"故障类型ID": faultTypeID,"预约日期": dateCreated,"工单报修描述": describe,"工单创建日期": dateCreated,"资产设备id": None,
                                     "任务id":None,"任务名称":None,"任务定义Key": None,"流程实例id": None,"流程定义id": None,"任务状态": None,"处理类型": None,"故障类型名称": faultTypeName,
                                     "工单ID": None,"工单编号": fficeNumber,"工单报修人ID": None,"工单状态": None,"工单改派人ID": None,"工单处理人ID": None,"报修人电话": None,
                                     "预约开始时间": None,"预约结束时间": None,"确认开始服务时间": None,"确认结束服务时间": None,"工单范围": inOutTicket,"意见状态": None,
                                     "工单服务类型": ticketServeType,"任务意见": None,"事件解决方案": None,"预约时间段": AppointmentTime,"内部处理结果": None,"评级": None,
                                     "用户评价": None,"挂起下拉框理由": None,"挂起状态字段": None,"改派人群组ID": None,"外协处理描述":None,"工单在挂起前的状态":None,
                                     "任务办理":TaskToDealWith}
        else:
            cache_parameterPacket["检查登录用户信息"]=userinfo   ; cache_parameterPacket["测试结果"]=testResult
            cache_parameterPacket["字典的键"] = dictionaryKeys   ; cache_parameterPacket["测试点"]=testPoint_spreadsheet
            cache_parameterPacket["所属接口"] = Subordinate_port ; cache_parameterPacket["平台名称"] = appletName
            cache_parameterPacket["所属模块"] = Their_module     ;  cache_parameterPacket["重复筛选参数"] = Their_module
            cache_parameterPacket["开始日期"] = startDate        ;  cache_parameterPacket["结束日期"] = dateClosed
            cache_parameterPacket["用例名称"] = self.UseCaseName
        """合并用户信息参数包，生成新的参数包"""
        self.parameterPacket = dict(dicti_userinfo, **cache_parameterPacket)
        print("\033[1;34;40m获取用例“%r”，用例编号“%r”的参数包：\033[0m\033[4;35;40m%r" % (self.UseCaseName, UseCase_number, self.parameterPacket))
        return self.parameterPacket














