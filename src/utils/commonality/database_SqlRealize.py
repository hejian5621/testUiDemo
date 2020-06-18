# SQL实现

from utils.commonality.database_sql import data_sql,AssetManagementLibrarySQL,WorkOrder_quantity_statistics,ComplaintsModule,\
    complaintSQL,authorityManagement_SQL,EventModules,WorkOrderProcess_database,elseSQL
from utils.commonality.database_connect import ReadDatabase
import re
from log import log
import sys
import os




class  dataProcessing:

    def __init__(self,Filter_parameters,fields_parameters=None,StandbyParameter=None,parameter1=None):
        self.Filter_parameters = Filter_parameters
        self.fields_parameters = fields_parameters
        self.StandbyParameter = StandbyParameter
        self.parameter1 = parameter1
        self.userID = None
        self.list_groupID = []
        self.groupID = None
        self.list_officeName = []
        self.officeName = None
        self.information = None
        self.list_officeName_sorts = []
        self.list_userID = None







    def user_name(self,fields,variate=None,variable = None):
        """
        单表查询
        :param fields: 属性
        :param variate: 查询实际参数
        :param variable: 工单库
        :return: 用户名称
        """
        sql =None
        # userID_username：根据用户ID查找用户名称
        if self.Filter_parameters == "userID_username":
            sql = data_sql(self.fields_parameters).userID_username(fields)  # 获取sql语句
        # userName_userID：根据用户名查找用户ID
        elif self.Filter_parameters == "userName_userID":
            sql = data_sql(self.fields_parameters).userName_userID(fields)  # 获取sql语句
        #  loginName_userID：根据用户名称查找用户ID
        elif self.Filter_parameters == "loginName_userID":
            sql = data_sql(self.fields_parameters).loginName_userID(fields)  # 获取sql语句
        # loginName_username：根据登陆名查找用户名称
        elif self.Filter_parameters == "loginName_username":
            sql = data_sql(self.fields_parameters).loginName_username(fields)  # 获取sql语句
        # loginName_officeID：根据外部用户登陆名查找单位ID
        elif self.Filter_parameters == "loginName_officeID":
            sql = data_sql(self.fields_parameters).loginName_officeID(fields)  # 获取sql语句
        elif self.Filter_parameters == "loginName_officeName":
            sql = data_sql(self.fields_parameters).loginName_officeName(fields)  # 获取sql语句
        elif self.Filter_parameters == "loginName_officeNumber":
            sql = data_sql(self.fields_parameters).loginName_officeNumber(fields)  # 获取sql语句
        #  loginName_phone：根据登录名查找用户电话号码
        elif self.Filter_parameters == "loginName_phone":
            sql = data_sql(self.fields_parameters).loginName_phone(fields)  # 获取sql语句
        #  loginName_phone：根据登录名获取群组ID列表
        elif self.Filter_parameters == "loginName_groupID":
            sql = data_sql(self.fields_parameters).loginName_groupID(fields)  # 获取sql语句
        #  workOrderNumber_groupID：根据工单编号获取群组ID
        elif self.Filter_parameters == "workOrderNumber_groupID":
            sql = data_sql(self.fields_parameters).workOrderNumber_groupID(fields)  # 获取sql语句
        #  workOrderNumber_loginName_sort： 根据工单编号和登录名获用户权限
        elif self.Filter_parameters == "workOrderNumber_loginName_sort":
            sql = data_sql(self.fields_parameters).workOrderNumber_loginName_sort(fields)  # 获取sql语句
        elif self.Filter_parameters == "repairsUserID_officeID_groupID":
            sql = data_sql(self.fields_parameters).repairsUserID_officeID_groupID(fields)  # 获取sql语句
        # userID_group：根据userID查询群组
        elif self.Filter_parameters == "userID_groupID_sort":
            sql = data_sql(self.fields_parameters).userID_groupID_sort(fields)  # 获取sql语句
        elif self.Filter_parameters == "groupID_userID_usernameAndId":
            sql = data_sql(self.fields_parameters).groupID_userID_usernameAndId(fields)  # 获取sql语句
        elif self.Filter_parameters == "groupIDuserID_Sort":
            sql = data_sql(self.fields_parameters).groupIDuserID_Sort(fields,variate)  # 获取sql语句
        # userID_group：根据userID查询群组
        elif self.Filter_parameters == "groupID_officeName":
            sql = data_sql(self.fields_parameters).groupID_office(fields)  # 获取sql语句
        # groupID_user_id__officeName_sort：根据群组ID和userId查询群组名称和群组权限字段
        elif self.Filter_parameters == "groupID_userId__officeName_sort":
            sql = data_sql(self.fields_parameters).groupID_userId__officeName_sort(fields,variate)  # 获取sql语句
        elif self.Filter_parameters == "officeID_officeName":
            sql = data_sql(self.fields_parameters).officeID_officeName(fields)  # 获取sql语句
        elif self.Filter_parameters == "officeName_officeID":
            sql = data_sql(self.fields_parameters).officeName_officeID(fields)  # 获取sql语句
        # 根据工单编号查询工单ID
        elif self.Filter_parameters == "WorkOrderNumber_WorkOrderID":
            sql = data_sql(self.fields_parameters).WorkOrderNumber_WorkOrderID(fields)  # 获取sql语句
        # 根据工单ID查询工单日志（历史操作记录）
        elif self.Filter_parameters == "WorkOrderID_WorkOrderLog":
            sql = data_sql(self.fields_parameters).WorkOrderID_WorkOrderLog(fields)  # 获取sql语句
        # 根据用户ID获取角色ID
        elif self.Filter_parameters == "userID_roleID":
            sql = data_sql(self.fields_parameters).userID_roleID(fields)  # 获取sql语句
        # 根据角色ID获取角色名称
        elif self.Filter_parameters == "roleID_roleName":
            sql = data_sql(self.fields_parameters).roleID_roleNam(fields)  # 获取sql语句
        # AreaManager_underling_office：查询出区域管理员的下属单位（包括本单位）
        elif self.Filter_parameters == "AreaManager_underling_office":
            sql =data_sql(self.fields_parameters).AreaManager_underling_office(fields)  # 获取sql语句
        elif self.Filter_parameters == "inquire_faultTypeID":
            sql = data_sql(self.fields_parameters).inquire_faultTypeID(fields)  # 获取sql语句
        elif self.Filter_parameters == "loginName_company_type":
            sql = data_sql(self.fields_parameters).loginName_company_type(fields)  # 获取sql语句
        # officeID_government_officeIdAndgroupId:根据单位ID获取所管辖的单位ID和群组ID
        elif self.Filter_parameters == "officeID_government_officeIdAndgroupId":
            sql = data_sql(self.fields_parameters).officeID_government_officeIdAndgroupId(fields)  # 获取sql语句
        # external_AreaManager_StateNumber：外部用户首页工单数量统计
        elif self.Filter_parameters == "external_AreaManager_StateNumber":
            sql = WorkOrder_quantity_statistics(self.fields_parameters,self.StandbyParameter).external_AreaManager_StateNumber(fields)  # 获取sql语句
        # ReportStatistics_quantityStatistics：报修统计--报修数量统计
        elif self.Filter_parameters == "ReportStatistics_quantityStatistics":
            sql = WorkOrder_quantity_statistics(self.fields_parameters).ReportStatistics_quantityStatistics(fields)  # 获取sql语句
        # ListOfComplaints：投诉模块--投诉清单，self.fields_parameters：用户权限，self.StandbyParameter：筛选条件，fields：筛选参数
        elif self.Filter_parameters == "ListOfComplaints":
            sql = ComplaintsModule(self.fields_parameters,self.StandbyParameter).ListOfComplaints(fields)  # 获取sql语句
        # add_database：用户新增投诉信息，检查数据是否增加
        elif self.Filter_parameters == "add_database":
            sql = complaintSQL(self.fields_parameters).add_database(fields)  # 获取sql语句
        # QueryComplaintID：
        elif self.Filter_parameters == "QueryComplaintID":
            sql = complaintSQL(self.fields_parameters).QueryComplaintID(fields)  # 获取sql语句
        # QueryComplaintID：
        elif self.Filter_parameters == "accept_complaint_databaseQuery":
            sql = complaintSQL(self.fields_parameters).accept_complaint_databaseQuery(fields)  # 获取sql语句
        elif self.Filter_parameters == "ticket_serve_cd_number":
            sql = WorkOrderProcess_database(self.fields_parameters).ticket_serve_cd_number(fields)  # 获取sql语句
        elif self.Filter_parameters == "add_WorkOrder_databaseQuery":
            sql = WorkOrderProcess_database(self.fields_parameters).add_WorkOrder_databaseQuery(fields)  # 获取sql语句
        elif self.Filter_parameters == "alter_WorkOrder_database_DataChanges":
            sql = WorkOrderProcess_database(self.fields_parameters).alter_WorkOrder_database_DataChanges(fields)  # 获取sql语句
        elif self.Filter_parameters == "AreaManager_loginName_officeIDAadofficename":
            sql = authorityManagement_SQL(self.fields_parameters).AreaManager_loginName_officeIDAadofficename(fields)  # 获取sql语句
        elif self.Filter_parameters == "AreaManager_loginName_useridAedUsername":
            sql = authorityManagement_SQL(self.fields_parameters).AreaManager_loginName_useridAedUsername(fields)
        elif self.Filter_parameters == "UserAdministrator_loginName_userid":
            sql = authorityManagement_SQL(self.fields_parameters).UserAdministrator_loginName_userid(fields)
        elif self.Filter_parameters == "UserAdministrator_loginName_officeID":
            sql = authorityManagement_SQL(self.fields_parameters).UserAdministrator_loginName_officeID(fields)
        elif self.Filter_parameters == "opsGroup_loginName_membersUserID":
            sql = authorityManagement_SQL(self.fields_parameters).opsGroup_loginName_membersUserID(fields)
        elif self.Filter_parameters == "opsGroup_loginName_officeID":
            sql = authorityManagement_SQL(self.fields_parameters).opsGroup_loginName_officeID(fields)
        elif self.Filter_parameters == "opsEngineer_loginName_membersUserID":
            sql = authorityManagement_SQL(self.fields_parameters).opsEngineer_loginName_membersUserID(fields)
        elif self.Filter_parameters == "opsEngineer_loginName_officeID":
            sql = authorityManagement_SQL(self.fields_parameters).opsEngineer_loginName_officeID(fields)
        elif self.Filter_parameters == "internalUser_loginName_officeID":
            sql = authorityManagement_SQL(self.fields_parameters).internalUser_loginName_officeID(fields)
        elif self.Filter_parameters == "internalUser_loginName_UserID":
            sql = authorityManagement_SQL(self.fields_parameters).internalUser_loginName_UserID(fields)
        elif self.Filter_parameters == "outsource_ToRespondTo":
            sql = EventModules(self.fields_parameters).outsource_ToRespondTo(fields)
        elif self.Filter_parameters == "noOffTicketListData_WorkOrderList":
            sql = EventModules(self.fields_parameters).noOffTicketListData_WorkOrderList(fields,variate)
        elif self.Filter_parameters == "InsideRepairListData_WorkOrderList":
            sql = EventModules(self.fields_parameters).InsideRepairListData_WorkOrderList(fields,variate)
        elif self.Filter_parameters == "ExternalRepairListData_WorkOrderList":
            sql = EventModules(self.fields_parameters).ExternalRepairListData_WorkOrderList(fields,variate)
        elif self.Filter_parameters == "MyRepairListData_WorkOrderList":
            sql = EventModules(self.fields_parameters).MyRepairListData_WorkOrderList(fields)
        elif self.Filter_parameters == "allListData_WorkOrderList":
            sql = EventModules(self.fields_parameters).allListData_WorkOrderList(fields)
        elif self.Filter_parameters == "sjTicketServe_details":
            sql = EventModules(self.fields_parameters).sjTicketServe_details(fields,variate)
        elif self.Filter_parameters == "AllGroups":
            sql = elseSQL(self.fields_parameters).AllGroups(fields)
            # 获取sql语句
        # 获取查询到的数据
        nickname = ReadDatabase(sql).ConnectToDatabase()
        n = len(nickname)
        try:
            n !=1
        except:
            print("表sys_user中用户ID不是唯一，需求用户ID必须是唯一")
            print("没有找到“新增的工单”程序停止", __file__, sys._getframe().f_lineno)
        if nickname == None:
            print("没有找到“新增的工单”程序停止", __file__, sys._getframe().f_lineno)
            os._exit(0)
        return nickname,sql










    def database_userinfo(self,parameter):
        """
        内部用户
        attribute：查询实际参数
        :param userinfo:用户信息（实际参数）
        :param parameter：参数属性（用户名、用户名称）
        :param data_type：需要返回的数据
        :return: information
        """
        attribute =None
        #######################################################################################################
        # 登陆名查询user_id参数
        if self.Filter_parameters == "LoginName":
            attribute = "loginName_userID"
        # 用户名称查询user_id参数
        elif self.Filter_parameters == "username":
            attribute = "userName_userID"
        # userID参数
        if self.Filter_parameters == "userID":
            self.userID = parameter
        else:
            self.list_userID,sql = dataProcessing(attribute).user_name(parameter)
            userID_dictionaries = self.list_userID[0]
            self.userID = userID_dictionaries["id"]
        ###########################################################################################################
        # 根据userID查询群组ID，群组ID可能有多个
        list_groupID_sort,sql = dataProcessing("userID_groupID_sort").user_name(self.userID)
        # 根据组群找到跟该组群关联的单位名称列表
        for groupID_sort in list_groupID_sort:
            # 取出groupID
            self.groupID = groupID_sort["群组ID"]
            # 把groupID存入列表
            self.list_groupID.append(self.groupID)
            # 根据取出groupID获取单位名
            self.officeName,sql = dataProcessing("groupID_officeName").user_name(self.groupID)
            # 把单位名称存入列表
            self.list_officeName.append(self.officeName)
        # 根据用户ID获取角色ID
        list_roleID,sql = dataProcessing("userID_roleID").user_name(self.userID)
        roleID_dictionaries = list_roleID[0]
        roleID = roleID_dictionaries["role_id"]
        # 根据角色ID获取角色名称
        list_roleName,sql = dataProcessing("roleID_roleName").user_name(roleID)
        # 根据群组ID和用户ID获取单位名称
        for groupid in self.list_groupID:
            list_officeName_sort,sql = dataProcessing("groupID_userId__officeName_sort").user_name(groupid,self.userID)
            self.list_officeName_sorts.append(list_officeName_sort)
        ###########################################################################################################
        if self.fields_parameters == "userID":
            # 返回userID数据类型：'ded528a57c274178b6bd4628fa731c82'
            self.information = self.list_userID
        # 根据userID查询群组ID，群组ID可能有多个
        elif self.fields_parameters == "groupID":
            # 返回列表群组ID,数据类型：[{'id': 'ded528a57c274178b6bd4628fa731c82'}]
            self.information = self.list_groupID
        elif self.fields_parameters == "groupID_sort":
            # 返回列表群组ID,数据类型：{'群组ID': '13d47146917b4d2ca67caec215d5f3f0', '判断组长字段': '1'}
            self.information = list_groupID_sort
        # 根据组群找到跟该组群关联的单位名称
        elif self.fields_parameters == "officeName":
            # 返回单位名称列表，数据类型：如果用户有多个组[[], [{'NAME': '生物城第二级中学分校'}], [{'NAME': '生物城区域'}], [{'NAME': '生物城第二级中学'}]]
            self.information = self.list_officeName
        elif self.fields_parameters == "officeName_sort":
            # [[], [{'name': '生物城第二级中学分校', 'sort': '1'}], [{'name': '生物城区域', 'sort': '1'}], [{'name': '生物城第二级中学', 'sort': None}]]
            # 返回单位名称列表，数据类型：如果用户有多个组
            self.information = self.list_officeName_sorts
        elif self.fields_parameters == "roleName":
            # 返回角色名称数据类型： [{'name': '运维经理'}]
            self.information = list_roleName
        log.log("根据：%r，数据属性：%r，返回的数据类型：%r，返回的数据："%(parameter, parameter, self.fields_parameters),self.information)
        return self.information




    def database_WorkOrderNumber(self,WorkOrderNumber):
        """
        根据工单ID查询该工单对应的操作历史记录
        :param WorkOrderNumber: 工单编号
        :param parameter: 那个模块，事件或者服务
        :return:
        [{'用户ID': '7e15c22f331843dd9134b68c38dfb446', '操作': '申请外协', '修改内容': '将报修人联系电话“13250505053”修改为“”，将工单服务类型修改为“一般事件”',
         '操作时间': datetime.datetime(2019, 6, 14, 14, 3, 31)},
        {'用户ID': '9d62886934e2444d9ba8168d8d8e958c', '操作': '新增工单', '修改内容': '新增工单', '操作时间': datetime.datetime(2019, 6, 9, 21, 27, 55)}]
        """
        # 根据工单编号查询出工单ID
        WorkOrderID,sql = dataProcessing("WorkOrderNumber_WorkOrderID",self.Filter_parameters).user_name(WorkOrderNumber)
        WorkOrderID = WorkOrderID[0]
        WorkOrderID = WorkOrderID["工单ID"]
        # 根据工单ID查询关联工单的日子（历史记录）
        WorkOrderLog,sql = dataProcessing("WorkOrderID_WorkOrderLog").user_name(WorkOrderID)
        return WorkOrderLog


    def loginName_officeID(self,loginName):
        """
        外部用户根据登陆名查找所在单位名称
        :return:
        """
        # 根据登陆名获取单位ID
        officeID,sql = dataProcessing("loginName_officeID").user_name(loginName)
        return officeID





class AssetManagementDataQuery():
    """资产管理数据查询"""


    def __init__(self,instantiation,parameter=None,defaultParameters=None,defaultParameters2=None):
        # 实际存传入的参数
        self.instantiation = instantiation
        # 判断输入参数类型和输出参数类型
        self.parameter=parameter
        # 备用参数
        self.defaultParameters = defaultParameters
        # 备用参数2
        self.defaultParameters2 = defaultParameters2
        # SQL语句
        self.sql = None
        # 数据库查询返回的数据列表
        self.nickname =[]
        # 单位名称
        self.officeName=None
        # 单位ID
        self.officeID =None
        self.list_officeName = []
        self.officeName =None






    def independentSQL(self,Parameters=None):
        """
          单表查询
          :param sys_user: 查询实际参数
          :param fields: 属性
          :param parameter: 工单库
          :return: 用户名称
          """
        # NotDelete_property：在资产列表中取出没有逻辑删除的资产
        if self.parameter == "NotDelete_property":
            self.sql = AssetManagementLibrarySQL().NotDelete_property()  # 获取sql语句
        # locationID_office：根据位置ID获取单位结构
        elif self.parameter == "locationID_officeID":
            self.sql = AssetManagementLibrarySQL(self.instantiation).locationID_office()  # 获取sql语句
        #  officeID_officeName：根据单位ID获取单位名称
        elif self.parameter == "officeID_officeName":
            self.sql = AssetManagementLibrarySQL(self.instantiation).officeID_officeName()  # 获取sql语句
        # ListOfAssets_screeningCondition：根据筛选条件判断设备清单
        elif self.parameter == "ListOfAssets_screeningCondition":
            self.sql = AssetManagementLibrarySQL(self.instantiation,self.defaultParameters,self.defaultParameters2).ListOfAssets_screeningCondition(Parameters)  # 获取sql语句
        #  OfficeID_locationID：根据单位ID获取位置ID
        elif self.parameter == "OfficeID_locationID":
            self.sql = AssetManagementLibrarySQL(self.instantiation).OfficeID_locationID() # 获取sql语句
        # 获取查询到的数据
        self.nickname = ReadDatabase(self.sql).AssetManagementLibrary()
        n = len(self.nickname)
        try:
            n != 1
        except:
            print("表sys_user中用户ID不是唯一，需求用户ID必须是唯一")
            log.log("没有找到“新增的工单”程序停止", __file__, sys._getframe().f_lineno)
            print("没有找到“新增的工单”程序停止", __file__, sys._getframe().f_lineno)
        if self.nickname == None:
            log.log("没有找到“新增的工单”程序停止", __file__, sys._getframe().f_lineno)
            print("没有找到“新增的工单”程序停止", __file__, sys._getframe().f_lineno)
            os._exit(0)
        return self.nickname





    def locationID_officeID(self):
        """
        根据位置ID获取单位根节点的单位名称
        self.instantiation:实际参数，单位ID
        :return:
        """
        for locationID in self.instantiation:
            self.officeName = AssetManagementDataQuery(locationID).location_officename()
            self.list_officeName.append(self.officeName)
        # 去掉重复的单位名称
        self.list_officeName=list(set(self.list_officeName))
        return self.list_officeName



    def location_officename(self):
        """
        根据位置ID获取关联的单位名称（位置的根节点）
        :param self.parameter: 位置ID
        :return:
        """
        # 根据位置ID获取单位结构
        officeID = AssetManagementDataQuery(self.instantiation, "locationID_officeID").independentSQL()
        officeID = officeID[0]
        officeID = officeID["单位结构"]
        """
        根据单位结构字段来判断该位置是不是跟节点；
        如果是根节点根据位置ID获取单位名称，如果不是根节点就截取0后面的ID来获取单位名称；
        """
        # 根据正则表达式，截取逗号前面的字段，来生成一个列表
        patt = re.compile(r"(.*?),", re.S)
        history = patt.findall(officeID)
        # 如果列表里面的数据少于2个，就说明该位置是根节点的单位；
        # 如果列表里面的数据大于等于2个，就说明位置不是根节点，就取0后面的id编译成单位名称
        if len(history) < 2:
            officeName = AssetManagementDataQuery(self.instantiation, "officeID_officeName").independentSQL()
            officeName = officeName[0]
            self.officeName = officeName["单位名称"]
        else:
            # 取出0后面的单位ID
            officeID = history[1]
            officeName = AssetManagementDataQuery(officeID, "officeID_officeName").independentSQL()
            officeName = officeName[0]
            self.officeName = officeName["单位名称"]
        return  self.officeName


    def loginName_officeID(self):
        """
        根据登陆名获取区域管理员所管辖的单位
        self.instantiation：登陆名
        government：[{'单位ID': '4e9d5a781177449bb0b74dbc6d75a9fe', '群组ID': '13d47146917b4d2ca67caec215d5f3f0'},
        {'单位ID': '8c970aecfe6a478ebdd2be43b4b670e8', '群组ID': '13d47146917b4d2ca67caec215d5f3f0'}, ]
        :return:
        """
        # 根据用户名获取单位ID
        officeID,sql = dataProcessing("loginName_officeID").user_name(self.instantiation)
        officeID = officeID[0]
        officeID = officeID['单位ID']
        # 根据单位ID获取所管辖的所以单位ID和群组ID
        government,sql = dataProcessing("officeID_government_officeIdAndgroupId").user_name(officeID)
        return government



































