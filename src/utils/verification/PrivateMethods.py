from utils.commonality.database_SqlRealize import AssetManagementDataQuery
from commonality.database_SqlRealize import dataProcessing
from privately_owned.method import public_method,EachQuantityType_transition_CharacterString,ValueGenerationList
from appletConnector import initialize
from assertpy import assert_that
from privately_owned.method import authorityManagement
from utils.privately_owned.DataType_ParameterProcessing import DataType_processing


class useCase_check_deviceList():
    """ 私有方法类"""

    def __init__(self,parameter,argument=None,StandbyParameter=None,argument1=None,StandbyParameter1=None,argument2=None,StandbyParameter2=None):
        self.parameter=parameter
        self.argument = argument
        self.StandbyParameter = StandbyParameter
        self.argument1 = argument1
        self.StandbyParameter1 = StandbyParameter1
        self.argument2 = argument2
        self.StandbyParameter2 = StandbyParameter2
        self.expect_list_parameters =[]
        self.structure=[]
        self.structureName=None
        self.equipName=None
        self.batchNo=None
        self.str_test_result=None
        self.expect_AreaManagerUnit=None
        self.result=None
        self.str_TestResultData=None
        self.list_parameters =[]
        self.characterString=None
        self.list_equipName=None


    def check_deviceList_ExpectedAssetsList(self,roleName,list_locationID):
        """
        设备清单校验方法---预期资产列表
        list_locationID：
        :return:
        """
        self.batchNo = self.parameter;self.equipName = self.argument;self.structureName = self.StandbyParameter
        # 预期资产列表
        #1、批次为空、设备名称为空、单位id为空
        if self.batchNo == None and self.equipName == None and self.structureName == None:
            if roleName == "区域管理员"  or roleName == "普通用户"  or roleName == "用户管理员":
                for locationID in list_locationID:
                    expect_list_parameters = None
                    expect_list_parameters = AssetManagementDataQuery(locationID,"ListOfAssets_screeningCondition").independentSQL("externalAlll")
                    for parameters in expect_list_parameters:
                        self.expect_list_parameters.append(parameters)
            elif roleName == "运维经理"  or roleName == "运维工程师"  or roleName == "运维总监":
                self.expect_list_parameters = AssetManagementDataQuery(None,"ListOfAssets_screeningCondition").independentSQL("alll")
            self.characterString ="1、批次为空、设备名称为空、单位id为空"
        #2、批次不为空、设备名称为空、单位id为空
        elif self.batchNo != None and self.equipName == None and self.structureName == None:
            if roleName == "区域管理员" or roleName == "普通用户" or roleName == "用户管理员":
                for locationID in list_locationID:
                    expect_list_parameters=None
                    expect_list_parameters = AssetManagementDataQuery(self.batchNo,"ListOfAssets_screeningCondition",locationID).independentSQL("external_batchNumber")
                    for parameters in expect_list_parameters:
                        self.expect_list_parameters.append(parameters)
            elif roleName == "运维经理" or roleName == "运维工程师" or roleName == "运维总监":
                self.expect_list_parameters = AssetManagementDataQuery(self.batchNo,"ListOfAssets_screeningCondition").independentSQL("batchNumber")
            self.characterString = "2、批次不为空、设备名称为空、单位id为空"
        #3、批次为空、设备名称不为空、单位id为空
        elif self.batchNo == None and self.equipName != None and self.structureName == None:
            if roleName == "区域管理员" or roleName == "普通用户" or roleName == "用户管理员":
                for locationID in list_locationID:
                    expect_list_parameters = None
                    expect_list_parameters = AssetManagementDataQuery(self.equipName,"ListOfAssets_screeningCondition",locationID).independentSQL("external_designation")
                    for parameters in expect_list_parameters:
                        self.expect_list_parameters.append(parameters)
            elif roleName == "运维经理" or roleName == "运维工程师" or roleName == "运维总监":
                self.expect_list_parameters = AssetManagementDataQuery(self.equipName,"ListOfAssets_screeningCondition").independentSQL("designation")
            self.characterString = "3、批次为空、设备名称不为空、单位id为空"
        # 4、批次为空、设备名称为空、单位id不为空
        elif self.batchNo == None and self.equipName == None and self.structureName != None:
            for locationID in list_locationID:
                expect_list_parameters = None
                expect_list_parameters = AssetManagementDataQuery(locationID,"ListOfAssets_screeningCondition").independentSQL("location")
                for parameters in expect_list_parameters:
                    self.expect_list_parameters.append(parameters)
            self.characterString = "4、批次为空、设备名称为空、单位id不为空"
        # 5、批次不为空、设备名称不为空、单位id为空
        elif self.batchNo != None and self.equipName != None and self.structureName == None:
            if roleName == "区域管理员" or roleName == "普通用户" or roleName == "用户管理员":
                for locationID in list_locationID:
                    expect_list_parameters = None
                    expect_list_parameters = AssetManagementDataQuery(self.batchNo,"ListOfAssets_screeningCondition",self.equipName,locationID).independentSQL("external_batchNumber_designation")
                    for parameters in expect_list_parameters:
                        self.expect_list_parameters.append(parameters)
            elif roleName == "运维经理" or roleName == "运维工程师" or roleName == "运维总监":
                self.expect_list_parameters = AssetManagementDataQuery(self.batchNo, "ListOfAssets_screeningCondition",self.equipName).independentSQL("batchNumber_designation")
            self.characterString = "5、批次不为空、设备名称不为空、单位id为空"
        # 6、批次不为空、设备名称为空、单位id不为空
        elif self.batchNo != None and self.equipName == None and self.structureName != None:
            for locationID in list_locationID:
                expect_list_parameters = None
                expect_list_parameters = AssetManagementDataQuery(self.batchNo,"ListOfAssets_screeningCondition",locationID).independentSQL("batchNumber_location")
                for parameters in expect_list_parameters:
                    self.expect_list_parameters.append(parameters)
            self.characterString = "6、批次不为空、设备名称为空、单位id不为空"
        # 7、批次为空、设备名称不为空、单位id不为空
        elif self.batchNo == None and self.equipName != None and self.structureName != None:
            for locationID in list_locationID:
                expect_list_parameters = None
                expect_list_parameters = AssetManagementDataQuery(self.equipName, "ListOfAssets_screeningCondition",locationID).independentSQL("designation_location")
                for parameters in expect_list_parameters:
                    self.expect_list_parameters.append(parameters)
            self.characterString = "7、批次为空、设备名称不为空、单位id不为空"
        # 8、单位id不为空，设备名称不为空，批次不为空
        elif self.batchNo != None and self.equipName != None and self.structureName != None:
            for locationID in list_locationID:
                expect_list_parameters = None
                expect_list_parameters = AssetManagementDataQuery(self.batchNo,"ListOfAssets_screeningCondition", self.equipName,locationID).independentSQL("batchNumber_designation_location")
                for parameters in expect_list_parameters:
                    self.expect_list_parameters.append(parameters)
            self.characterString = "8、单位id不为空，设备名称不为空，批次不为空"
        return self.expect_list_parameters , self.characterString


    def check_deviceList_officeID_officeName(self):
        """
        设备清单校验方法---单位ID编译成单位名称
        :return:单位名称列表
        """
        #  传入单位（单位结构表）ID
        structureName = AssetManagementDataQuery(self.parameter,"officeID_officeName").independentSQL()
        structureName = structureName[0]
        structure = structureName["单位名称"]
        self.structure.append(structure)
        return self.structure


    # def check_deviceList_AssetListCheck_result(self):
    #     """
    #     设备清单校验方法--资产列表--测试报告--测试结果字段
    #     :return:
    #     """
    #     reality_expect =self.parameter
    #     if len(list(reality_expect.values())) == 1:
    #         lis = list(reality_expect.values())[0]
    #         str_test_result = EachQuantityType_transition_CharacterString(lis).DataTypeConversion_console()
    #     else:
    #         lis1 = list(reality_expect.values())[0]
    #         lis2 = list(reality_expect.values())[1]
    #         str_test_resul1 = EachQuantityType_transition_CharacterString(lis1).DataTypeConversion_console()
    #         str_test_resul2 = EachQuantityType_transition_CharacterString(lis2).DataTypeConversion_console()
    #         str_test_result = "在预期值中没有的实际值:" + str_test_resul1 + "\n" + "在实际值中没有的预期值：" + str_test_resul2
    #     return  str_test_result


    # def check_deviceList_userOffice(self):
    #     """
    #     外部用户获取所在单位或者所管辖的单位
    #     :return:
    #     """
    #     expect_list_officeID =None
    #     roleName= self.parameter
    #     loginName = self.argument
    #     JSESSIONID=self.StandbyParameter
    #     if roleName == "区域管理员" or roleName == "用户管理员":
    #         # 获取区域管理员所管辖的所有单位名称，预期值
    #         expect_list_officeID = initialize(JSESSIONID).officeList()
    #         # # 预期值转换为字符串
    #         # expect_list_officeID = EachQuantityType_transition_CharacterString(self.list_parameters).DataTypeConversion_console()
    #     elif roleName == "普通用户":
    #         # 根据登录名获取登录用户的所在单位，预期值
    #         officeID = dataProcessing(None).loginName_officeID( loginName)
    #         officeID = officeID[0]
    #         list_parame = officeID["单位ID"]
    #         self.list_parameters.append(list_parame)
    #         expect_list_officeID = self.list_parameters
    #     return expect_list_officeID


    # def  check_deviceList_expectReality_Str(self):
    #     """
    #     预期结果和实际结果，字典转化成字符串
    #     :return:
    #     """
    #     str_expect_list_parameters_compile ="为空"
    #     str_realAssets="为空"
    #     expect_list_parameters = self.parameter
    #     realAssets = self.argument
    #     if expect_list_parameters and realAssets:
    #         # 字典转换成列表
    #         data_list = DataType_processing(expect_list_parameters).list_nest_dict_list("批次")
    #         data_list1 = DataType_processing(realAssets).list_nest_dict_list("批次")
    #         # 列表转换成字符串
    #         str_expect_list_parameters_compile = EachQuantityType_transition_CharacterString(data_list).DataTypeConversion_console()
    #         str_realAssets = EachQuantityType_transition_CharacterString(data_list1).DataTypeConversion_console()
    #     elif expect_list_parameters:
    #         # 字典转换成列表
    #         data_list = DataType_processing(expect_list_parameters).list_nest_dict_list("批次")
    #         # 列表转换成字符串
    #         str_expect_list_parameters_compile = EachQuantityType_transition_CharacterString(data_list).DataTypeConversion_console()
    #     elif realAssets:
    #         # 字典转换成列表
    #         data_list1 = DataType_processing(realAssets).list_nest_dict_list("批次")
    #         # 列表转换成字符串
    #         str_realAssets = EachQuantityType_transition_CharacterString(data_list1).DataTypeConversion_console()
    #     return   str_expect_list_parameters_compile , str_realAssets







class useCase_verify_ReportStatistics:
    """
    工单数量统计的私有方法
    """

    def __init__(self,parameter):
        self.parameter = parameter
        self.list1=[]
        self.list2 = []
        self.list_expect_value=None
        self.dict_expect = {}
        self.list_expect = []
        self.list_expectNumber = []
        self.reality_expect=None



    def database_statistics_WorkOrderNumber(self,dicti_parameterPacket,module):
        """
       在数据库查询查询出各个状态的工单数量
        self.parameter1 : 筛选条件列表
        self.argument : sql参数
        self.argument1:登录名
        tableName:服务表
        tableName1: 事件表
       :param dicti_parameterPacket:参数集
       :param module:
       :return:
        """
        serve_stateNumber=None;incident_stateNumber=None;list_serve_stateNumber=None;list_incident_stateNumber=None;New_list_quantity =[]
        list_serve_officeID = [];list_incident_officeID = [];key_id =None;key_name=None
        ServiceWorkOrder=self.parameter["服务工单表"];incidentWorkOrder=self.parameter["事件工单表"]
        if module == "报修数量":
            key_id="单位ID";key_name="单位名称"
            # 通过sql语句查询出各个状态的工单数量
            list_serve_stateNumber,sql = dataProcessing("ReportStatistics_quantityStatistics",ServiceWorkOrder).user_name(dicti_parameterPacket)  # 统计服务工单表里的工单数
            list_incident_stateNumber,sql = dataProcessing("ReportStatistics_quantityStatistics",incidentWorkOrder).user_name(dicti_parameterPacket) # 统计事件工单表里的工单数
        elif module == "故障数量":
            key_id = "故障ID";key_name="故障名称"
            # 通过sql语句查询出各个状态的工单数量
            list_serve_stateNumber,sql = dataProcessing("ReportStatistics_quantityStatistics", ServiceWorkOrder).user_name(dicti_parameterPacket)
            list_incident_stateNumber,sql = dataProcessing("ReportStatistics_quantityStatistics",incidentWorkOrder).user_name(dicti_parameterPacket)
        """合并服务工单表和事件表"""
        # 对比服务工单表跟事件表工单ID，获取两个工单表不同的单位
        for serve_stateNumber in list_serve_stateNumber:  # 服务工单表生产单位ID列表
            serve_officeID = serve_stateNumber[key_id]  # 取出服务工单表里的单位ID
            list_serve_officeID.append(serve_officeID)
        for incident_stateNumber in list_incident_stateNumber:
            incident_officeID = incident_stateNumber[key_id]  # 取出服务工单表里的单位ID
            list_incident_officeID.append(incident_officeID)
        list_serve = [x for x in list_serve_officeID if x not in list_incident_officeID]  # 在服务工单表中而不在事件表中
        list_incident = [y for y in list_incident_officeID if y not in list_serve_officeID]  # 在事件表中而不在服务工单表中
        list_serveAndIncident = [y for y in list_incident_officeID if y in list_serve_officeID]  # 服务工单表跟事件表都存在的单位
        for serve_stateNumber in list_serve_stateNumber:  # 便利出服务工单表里的工单数字典
            serve_officeID = serve_stateNumber[key_id]  # 取出服务工单表里的单位ID
            for serve in list_serve:  # 在服务工单表中而不在事件表中单位ID
                if serve_officeID == serve:
                    New_list_quantity.append(serve_stateNumber)  # 把只在服务工单表里的工单数字典直接存入列表
        for incident_stateNumber in list_incident_stateNumber:  # 便利出事件表里的工单数字典
            incident_officeID = incident_stateNumber[key_id]  # 取出事件表里的单位ID
            for incident in list_incident:  # 在事件表中而不在服务工单表中单位ID
                if incident_officeID == incident:
                    New_list_quantity.append(incident_stateNumber)  # 把只在事件表里的工单数字典直接存入列表
        # 把服务工单表跟事件
        for serve_stateNumber in list_serve_stateNumber:
            serve_officeID = serve_stateNumber[key_id]  # 取出服务工单表里的单位ID
            if serve_officeID in list_serveAndIncident:
                for incident_stateNumber in list_incident_stateNumber:
                    incident_officeID = incident_stateNumber[key_id]  # 取出服务工单表里的单位ID
                    if incident_officeID == serve_officeID:
                        serve_Name = serve_stateNumber[key_name]  # 取出服务工单表里的单位ID
                        serve_amount = serve_stateNumber["工单数"]
                        incident_amount = incident_stateNumber["工单数"]
                        sumnumber = int(serve_amount) + int(incident_amount)
                        dict_number = {key_id: serve_officeID, key_name: serve_Name, '工单数': str(sumnumber)}
                        New_list_quantity.append(dict_number)
        # 把所有的工单数转化成整数
        ultimately_list_quantity=[]
        for quantity in New_list_quantity:
            int_Number=int(quantity["工单数"])
            quantity["工单数"]=int_Number
            ultimately_list_quantity.append(quantity)
        return ultimately_list_quantity




class ComplaintListPage:
    """
    投诉清单页面数据校验单个方法
    """
    def __init__(self,dicti_parameterPacket):
        self.dicti_parameterPacket = dicti_parameterPacket


    def Complaint_expected_initial(self):
        """
        投诉清单获取预期值
        :return:
        """
        loginName=self.dicti_parameterPacket["登录名"];roleName = self.dicti_parameterPacket["用户权限"]
        titleAndcontent = self.dicti_parameterPacket["筛选条件内容或者标题"]
        start_date=self.dicti_parameterPacket["开始日期"];finish_date=self.dicti_parameterPacket["结束日期"]
        #  根据标题或者内容筛选条件有没有参数判断需要需要要加上标题或者内容筛选条件
        if titleAndcontent == None:
            StandbyParameter = "date"
            fields = {"登录名": loginName, "起始日期": start_date, "结束日期": finish_date}
        else:
            StandbyParameter = "dateAadtitleAadContent"
            fields = {"登录名": loginName, "起始日期": start_date, "结束日期": finish_date, "标题或者内容": titleAndcontent}
        '''获取投诉清单页面数据'''
        Complaint_list_data,sql = dataProcessing("ListOfComplaints",roleName,StandbyParameter).user_name(fields)
        return Complaint_list_data























