import configparser
# from utils.appletConnector import initialize
import os
import time

class ProfileDataProcessing:

    def __init__(self,parameter,argument=None,StandbyParameter=None):
        self.parameter = parameter
        self.argument = argument
        self.StandbyParameter = StandbyParameter


    @staticmethod
    def allocation():
        # # 学校
        platform = "school_"
        # 政企
        # platform = "statecos_"
        # platform = "statecosofficial_"
        return platform


    def config_File(self):
        """
        读取配置文件config里的数据
        参数:
        self.parameter:配置文件里标签
        self.argument：标签下面的键
        :return:配置文件的值
        """
        platform=ProfileDataProcessing.allocation()
        #/////////////////////////////////////////////////////////
        self.parameter =platform+self.parameter
        # 配置文件的
        commonality = platform+"commonality"
        role =  platform+"role"
        WorkOrderStatus=platform+"WorkOrderStatus"
        EquipmentStatus = platform+"EquipmentStatus"
        TaskToDealWith = platform + "TaskToDealWith"
        typeOfService = platform + "typeOfService"
        #///////////////////////////////////////////////////////////////////
        cf = configparser.ConfigParser()
        # 获取当前位置
        curpath = os.path.dirname(os.path.realpath(__file__))
        location = os.path.join(curpath, "config.ini")
        # 找到配置文件
        cf.read(location,encoding='utf-8')
        if self.parameter == commonality: # 公共配置项
            if self.argument == "pageNo":  # 起始页
               pageNo = cf.get(commonality,"pageNo")
               print("起始页:",pageNo)
               return pageNo
            elif self.argument == "pageSize": # 每页条数
               pageSize = cf.get(commonality,"pageSize")
               print("每页条数:", pageSize)
               return pageSize
            elif self.argument == "url": # 每页条数
               url = cf.get(commonality,"url")
               return url
            elif self.argument == "system": # 每页条数
               url = cf.get(commonality,"system")
               return url
        elif self.parameter == role: # 用户角色
            if self.argument == "domesticConsumer": # 普通用户
               Identification = cf.get(role,"domesticConsumer") # 账号
               password = cf.get(role, "domesticConsumer_password")  # 密码
               role = (Identification, password)
               return role
            elif self.argument == "UserAdministrator": # 用户管理员
                Identification = cf.get(role, "UserAdministrator")  # 账号
                password = cf.get(role, "UserAdministrator_password")  # 密码
                role = (Identification, password)
                return role
            elif self.argument == "AreaManager":  #区域管理员
                Identification = cf.get(role, "AreaManager")  # 账号
                password = cf.get(role, "AreaManager_password")  # 密码
                role = (Identification, password)
                return role
            elif self.argument == "operationNndMaintenanceEngineer":   #运维工程师-四组
                Identification = cf.get(role, "operationNndMaintenanceEngineer")  # 账号
                password = cf.get(role, "operationNndMaintenanceEngineer_password")  # 密码
                role = (Identification, password)
                return role
            elif self.argument == "OPS_engineer_loginName":  # 运维工程师-五组
                Identification = cf.get(role, "OPS_engineer_loginName")  # 账号
                password = cf.get(role, "OPS_engineer_password")  # 密码
                role = (Identification, password)
                return role
            elif self.argument == "OperationsTeamLeader":    #运维组长-四组
                Identification = cf.get(role, "OperationsTeamLeader")  # 账号
                password = cf.get(role, "OperationsTeamLeader_password")  # 密码
                role = (Identification, password)
                return role
            elif self.argument == "OPS_groupLeader_loginName":    #运维组长-五组
                Identification = cf.get(role, "OPS_groupLeader_loginName")  # 账号
                password = cf.get(role, "OPS_groupLeader_password")  # 密码
                role = (Identification, password)
                return role
            elif self.argument == "DirectorOfOperations":    # 运维总监
                Identification = cf.get(role, "DirectorOfOperations")  # 账号
                password = cf.get(role, "DirectorOfOperations_password")  # 密码
                role = (Identification, password)
                return role
            elif self.argument == "receptionDesk":   # 服务台
                Identification = cf.get(role, "receptionDesk")  # 账号
                password = cf.get(role, "receptionDesk_password")  # 密码
                role = (Identification, password)
                return role
        elif self.parameter == WorkOrderStatus:  # 工单状态
            if self.argument == "ToDealWith":  #内部_待办理
                ToDealWith = cf.get(role, "ToDealWith")
                return ToDealWith
            elif self.argument == "offTheStocks":  # 内部_已完成
                offTheStocks = cf.get(role, "offTheStocks")
                return offTheStocks
            elif self.argument == "ToRespondTo":  # 外协_待响应
                ToRespondTo = cf.get(role, "ToRespondTo")
                return ToRespondTo
            elif self.argument == "ToMakeAnAppointmentIn":  # 外协_预约中
                ToMakeAnAppointmentIn = cf.get(role, "ToMakeAnAppointmentIn")
                return ToMakeAnAppointmentIn
            elif self.argument == "pending":  # 外协_待处理
                pending = cf.get(role, "pending")
                return pending
            elif self.argument == "beingProcessed":  # 外协_处理中
                beingProcessed = cf.get(role, "beingProcessed")
                return beingProcessed
            elif self.argument == "HaveToHangUp":  # 外协_已挂起
                HaveToHangUp = cf.get(role, "HaveToHangUp")
                return HaveToHangUp
            elif self.argument == "processed":  # 外协_已处理
                processed = cf.get(role, "processed")
                return processed
            elif self.argument == "outsourceAllClosedSingle":  # 外协_已关单
                outsourceAllClosedSingle = cf.get(role, "outsourceAllClosedSingle")
                return outsourceAllClosedSingle
            elif self.argument == "interiorAllClosedSingle":  # 内部_已关单
                interiorAllClosedSingle = cf.get(role, "interiorAllClosedSingle")
                return interiorAllClosedSingle
        elif self.parameter == EquipmentStatus:   # 设备状态
            if self.argument == "inUse":  # 在用
                inUse = cf.get(EquipmentStatus, "inUse")
                print("工单状态:", inUse)
                return inUse
            elif self.argument == "leaveUnused": # 闲置
                leaveUnused = cf.get(EquipmentStatus, "leaveUnused")
                print("工单状态:", leaveUnused)
                return leaveUnused
            elif self.argument == "scrap":  # 报废
                scrap = cf.get(EquipmentStatus, "scrap")
                return scrap
        elif self.parameter == typeOfService:    # 服务类型
            if self.argument == "GeneralEvents":  # 一般事件
                GeneralEvents = cf.get(typeOfService, "GeneralEvents")
                return GeneralEvents
            elif self.argument == "emergency":  # 紧急事件
                emergency = cf.get(typeOfService, "emergency")
                print("工单状态:", emergency)
                return emergency
            elif self.argument == "OnSiteEvents":  # 驻场事件
                OnSiteEvents = cf.get(typeOfService, "OnSiteEvents")
                return OnSiteEvents
        elif self.parameter == TaskToDealWith:    # 任务办理按钮
            if self.argument == "1":
                TaskToDealWith = cf.get(TaskToDealWith, "1")
                return TaskToDealWith
            elif self.argument == "2":
                TaskToDealWith = cf.get(TaskToDealWith, "2")
                return TaskToDealWith
            elif self.argument == "3":
                TaskToDealWith = cf.get(TaskToDealWith, "3")
                return TaskToDealWith
            if self.argument == "4":
                TaskToDealWith = cf.get(TaskToDealWith, "4")
                return TaskToDealWith
            elif self.argument == "5":
                TaskToDealWith = cf.get(TaskToDealWith, "5")
                return TaskToDealWith
            elif self.argument == "6":
                TaskToDealWith = cf.get(TaskToDealWith, "6")
                return TaskToDealWith
            if self.argument == "8":
                TaskToDealWith = cf.get(TaskToDealWith, "8")
                return TaskToDealWith
            elif self.argument == "9":
                TaskToDealWith = cf.get(TaskToDealWith, "9")
                return TaskToDealWith
            elif self.argument == "10":
                TaskToDealWith = cf.get(TaskToDealWith, "10")
                return TaskToDealWith
            if self.argument == "11":
                TaskToDealWith = cf.get(TaskToDealWith, "11")
                return TaskToDealWith
            elif self.argument == "12":
                TaskToDealWith = cf.get(TaskToDealWith, "12")
                return TaskToDealWith
            elif self.argument == "13":
                TaskToDealWith = cf.get(TaskToDealWith, "13")
                return TaskToDealWith
            elif self.argument == "14":
                TaskToDealWith = cf.get(TaskToDealWith, "14")
                return TaskToDealWith
            elif self.argument == "15":
                TaskToDealWith = cf.get(TaskToDealWith, "15")
                return TaskToDealWith
            elif self.argument == "16":
                TaskToDealWith = cf.get(TaskToDealWith, "16")
                return TaskToDealWith
            elif self.argument == "17":
                TaskToDealWith = cf.get(TaskToDealWith, "17")
                return TaskToDealWith
            elif self.argument == "18":
                TaskToDealWith = cf.get(TaskToDealWith, "18")
                return TaskToDealWith




