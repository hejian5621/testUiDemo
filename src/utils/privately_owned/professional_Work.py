#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 业务数据处理方法


from config.readconfig import ProfileDataProcessing
from utils.commonality.database_SqlRealize import dataProcessing
import os,sys,json,requests,datetime,time
from utils.privately_owned.DataType_ParameterProcessing import DataType_processing




class  professionalWork_data_dispose:
    """业务类数据获取"""


    def __init__(self, parameter,argument=None):
        self.parameter = parameter
        self.argument = argument
        self.result=True

    @staticmethod
    def timeOutPeriod(JSESSIONID, UpdateTime):
        """
        获取字典里的超时时间设置，并截取出分钟
        根据工单的更新日期，加上耗时时间，返回最终预期的超时时间节点
        :param JSESSIONID:
        :param UpdateTime: 更新时间
        :return:
        """
        time_Timeout = None
        # 获取字典里的超时时间设置，并截取出分钟
        url = ProfileDataProcessing("commonality", "url").config_File()
        parameter = {"key": "continuous_time"}
        if url == "http://47.106.245.240:8081":
            url = url + "/eosp/a/app/sys/dict/getDictByKey" + "?" + JSESSIONID
        elif url == "http://47.106.245.240:8020":
            url = url + "/governEnterprise/a/app/sys/dict/getDictByKey;" + JSESSIONID
        req = requests.post(url, parameter)
        data = json.loads(req.text)
        data = data["body"]
        list1 = data["list"]
        list2 = list1[0]
        valu = list2["value"]
        valu = valu[2:]
        valu = valu[:-1]
        valu = int(valu)
        # 获取传进来的参数的类型
        data_type = DataType_processing(UpdateTime).acquire_dataType()
        if data_type == "time_type":
            time_Timeout = (UpdateTime + datetime.timedelta(minutes=valu)).strftime("%Y-%m-%d %H:%M")
        elif data_type == "str_type":
            startTime1 = datetime.datetime.strptime(UpdateTime, "%Y-%m-%d %H:%M")  # 把strTime转化为时间格式,后面的秒位自动补位的
            time_Timeout = (startTime1 + datetime.timedelta(minutes=valu)).strftime("%Y-%m-%d %H:%M")
        else:
            print("没有找到“获取耗时的时候传入的数据格式不是时间也不是str”程序停止", __file__, sys._getframe().f_lineno)
            os._exit(0)
        return time_Timeout



    @staticmethod
    def judge_loginName_groupLeader(self,userinfo,ContrastiveParameter):
        """
        判断登录的内部运维工程师是不是组长
        主要根据工单编号、登录名通过SQL语句判断；返回为空：证明不是组长，如果返回1证明是组长
        :param userinfo: 用户信息
        :param ContrastiveParameter:  参数包
        :return:
        """
        argument=None;jurisdiction=None
        loginName = userinfo["登录名"]
        jurisdiction,sql = dataProcessing("workOrderNumber_loginName_sort", loginName).user_name(ContrastiveParameter)
        if jurisdiction:
            jurisdiction = jurisdiction[0]
            jurisdiction = jurisdiction["sort"]
        if jurisdiction:
            argument ="1"
        else:
            argument = "2"
        return argument

    @staticmethod
    def Generate_the_workOrderNumber(userinfo):
        """
        生成预期的工单编号，单位编号-年-序列号
        :return:
        """
        ticket_serve_cd=None
        loginName=userinfo["登录名"]
        """获取通过用户的登录名查询出用户所在单位的单位编号"""
        fficeNumber,sql = dataProcessing("loginName_officeNumber").user_name(loginName)
        fficeNumber=fficeNumber[0]
        fficeNumber=fficeNumber["单位编号"]
        """获取当前年"""
        # systemTime = passShh_connectToServer("%Y-%m-%d %H:%M:%S").Get_server_time()
        systemTime =time.strftime("%Y-%m-%d %H:%M:%S")
        current_year = systemTime[:4]
        """拼接单位编号和当前年"""
        fragment_number=str(fficeNumber)+"-"+str(current_year)+"-"
        Number=len(fragment_number)  # 获取字符串数
        """获取数据库已有的工单编号序号"""
        # 获取数据库服务工单表跟事件库表里所有符合单位和当前年的工单编号并排序
        list_serve_fficeNumber,serve_sql = dataProcessing("ticket_serve_cd_number","服务工单").user_name(fragment_number)
        list_incident_fficeNumber, incident_sql = dataProcessing("ticket_serve_cd_number","事件").user_name(fragment_number)
        list_dicti_fficeNumber=list_serve_fficeNumber+list_incident_fficeNumber  # 合并两个列表
        if list_dicti_fficeNumber:
            list_sequenceNumber=[]
            for dicti_fficeNumber in list_dicti_fficeNumber:  # 列表嵌套字典转化成纯列表
                fficeNumber=dicti_fficeNumber["ticket_serve_cd"]
                str_sequenceNumber=fficeNumber[Number:]   # 获取str数据类型的序号
                int_sequenceNumber=int(str_sequenceNumber)   # str类型序号转化成int类型
                list_sequenceNumber.append(int_sequenceNumber)  # 把int类型的序号存入列表
            max_sequenceNumber=max(list_sequenceNumber)
            fficeNumber=int(max_sequenceNumber)+1    # 编号加一
            Places=len(str(fficeNumber))    #  把数字转成字符串，并且判断位数
            n =4-int(Places)
            if   n == 3:  ticket_serve_cd=fragment_number+"000"+str(fficeNumber)
            elif  n == 2: ticket_serve_cd = fragment_number + "00" + str(fficeNumber)
            elif  n == 1: ticket_serve_cd = fragment_number + "0" + str(fficeNumber)
            elif  n == 0: ticket_serve_cd = fragment_number + str(fficeNumber)
            else: print("工单编号生成有问题")
        else:
            ticket_serve_cd = fragment_number + "0001"
        return ticket_serve_cd


    @staticmethod
    def workOrder_whether_suspended_state(state, WorkOrderNumber):
        """
        通过历史记录判断工单是否在挂起申请状态
        :return:
        """
        result = "2"
        """获取历史记录"""
        # 判断工单在那个工单表里，主要用于工单ID
        if state == "外协_已关单" or state == "内部_已关单" or state == "内部_已撤销":
            parameter = "事件"
        else:
            parameter = "服务"
        # 取出工单编号对应的历史记录
        list_data = dataProcessing(parameter).database_WorkOrderNumber(WorkOrderNumber)
        # 按顺序取出每行历史记录
        for log_message in list_data:
            # 该行的操作列里的值
            operation = log_message["操作"]
            # 当第一行的操作列的值等于“申请挂起”时，取出操作时间列和用户ID
            if operation == "申请挂起":
                result = "1"
                break
            # 当第一行的操作列的值等于“挂起审核不通过”、"解挂"、"挂起审核通过"、"解挂改派"时，取出操作时间列
            elif operation == "挂起审核不通过" or operation == "挂起审核通过":
                result = "2"
                break
            else:
                result = "2"
        return result



    def GenerateUnrepeatedTitles(self,testModule,variable_site):
        """
        生成不重复标题
        self.parameter：标题参数
        :return:
        """
        """判断数据文件是否为空"""
        site=None
        # 获取月份和日期
        ti = time.strftime('%m%d', time.localtime(time.time()))
        # 获取文件位置
        address = ProjectFolderLocation.ToObtainPosition()
        if testModule=="投诉模块":
            if variable_site =="新增投诉标题":
                site = address + "report/ChangeTheValue/ComplaintsProcess/new_title_complaint.txt"
            elif variable_site == "受理投诉标题":
                site = address + "report/ChangeTheValue/ComplaintsProcess/acceptance__title_complaint.txt"
            elif variable_site == "投诉处理结果":
                site = address + "report/ChangeTheValue/ComplaintsProcess/resultOfHandling_title_complaint.txt"
        elif testModule=="工单流程模块":
            if variable_site =="新增工单标题":
                site = address + "report/ChangeTheValue/WorkOrderProcess/new_title_workOrder.txt"
            elif variable_site == "受理投诉标题":
                site = address + "report/ChangeTheValue/WorkOrderProcess/acceptance__title_complaint.txt"
            elif variable_site == "投诉处理结果":
                site = address + "report/ChangeTheValue/WorkOrderProcess/resultOfHandling_title_complaint.txt"
        # getsize函数：0代表文件为空；1代表文件不为空
        size = os.path.getsize(site)
        if size == 0:
            # 初始序号
            str__Order = "001"
            # 打开文件
            dr = open(site, 'a')
        # 如果储存标题文件不为空，读取所以行数，取出最后一行
        else:
            # 打开并读取文件 rb：读取
            dr = open(site, 'rb')
            with dr as f:
                # 读取所有行
                lines = f.readlines()
                # 取最后一行
                last_line = lines[-1]
            # 关闭储存工单文档
            dr.close()
            # 转码：从2进制转到10进制
            caption = last_line.decode('gbk')
            # 截取序号
            history_Order = caption[4:7]
            # 获取给出的标题参数的字符个数
            count = len(self.parameter)
            # 标题参数数加上序号数
            count=int(count)+3
            # 截取日期
            Historical_date = caption[:-count]
            # 如果获取标题最后一行的日期等于当前日期，储存的工单标题序号加1
            if int(Historical_date) == int(ti):
                # 序号加1
                create_Order = int(history_Order) + 1
                # 判断序号是否是3位数，如果不是就转化成3位数
                str__Order = str(create_Order)
                count1 = len(str__Order)
                if count1 == 1:
                    str__Order = "00" + str__Order
                elif count1 == 2:
                    str__Order = "0" + str__Order
                elif count1 == 3:
                    pass
                # 打开文件
                dr = open(site, 'a')
                # 换行
                dr.write('\n')
            # 如果获取工单标题最后一行的日期不等于当前日期，储存的工单标题序号从1开始
            else:
                # 初始序号
                str__Order = "001"
                # 打开文件
                dr = open(site, 'a')
                # 换行
                dr.write('\n')
        # 拼接标题
        VariableTitle =ti + str(str__Order)+self.parameter
        # 去掉中间的空格
        repair_order_title = ''.join(VariableTitle.split())
        # 写入标题
        dr.write(repair_order_title)
        # 关闭文档
        dr.close()
        return repair_order_title
