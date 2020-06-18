#  电子表格--读取
#coding:utf-8
from spreadsheet_dispose_method import read_spreadsheet


class resdLocation_And_SpreadsheetData:
    """
    1、获取电子表格所需的地址和表名
    2、通过地址获取电子表格数据
    """

    def __init__(self,Sheet_name,table_name=None,output_type=None):
        """
        :param Sheet_name: 表单名
        :param table_name: 电子表格名
        :param output_type: 输出数据类型
        """
        self.Sheet_name=Sheet_name
        self.table_name = table_name
        self.output_type = output_type


    def GetSpreadsheetData(self):
        """
        读取电子表格数据
        :return:
        """
        dicti_dataPackage=None;list_dicti_Excel=None
        if   self.table_name=="小程序工单流程测试用例":
            dicti_dataPackage = resdLocation_And_SpreadsheetData(self.Sheet_name).spreadsheet_WorkOrder_flow()
        elif self.table_name=="小程序工单清单测试用例":
            dicti_dataPackage = resdLocation_And_SpreadsheetData(self.Sheet_name).spreadsheet_WorkOrderList()
        elif self.table_name=="小程序登录模块测试用例":
            dicti_dataPackage = resdLocation_And_SpreadsheetData(self.Sheet_name).spreadsheet_SystemLogin()
        elif self.table_name == "设备清单列表测试用例":
            dicti_dataPackage = resdLocation_And_SpreadsheetData(self.Sheet_name).spreadsheet_AssetsEquipment()
        elif self.table_name == "小程序报修统计模块测试用例":
            dicti_dataPackage = resdLocation_And_SpreadsheetData(self.Sheet_name).spreadsheet_WorkOrderNumberStatistics()
        elif self.table_name == "投诉清单测试用例":
            dicti_dataPackage = resdLocation_And_SpreadsheetData(self.Sheet_name).spreadsheet_complaint_list()
        elif self.table_name == "投诉流程测试用例":
            dicti_dataPackage = resdLocation_And_SpreadsheetData(self.Sheet_name).spreadsheet_complaint_flow()
        if self.output_type=="列表嵌套字典":
            list_dicti_Excel = read_spreadsheet(dicti_dataPackage).ReadingSpreadsheets_listNestedDicti()  # 读取电子表格里的内容生成列表嵌套字典数据类型的值
        elif self.output_type=="列表嵌套列表":
            list_dicti_Excel = read_spreadsheet(dicti_dataPackage).ReadingSpreadsheets_listNestedlist()  # 读取电子表格里的内容生成列表嵌套字典数据类型的值
        return list_dicti_Excel


###########测试用例###################################################################################

    def spreadsheet_WorkOrder_flow(self):
        """
        获取读取电子表格的地址和表名（测试用例用）：工单页面数据对比
        :return:
        """
        dicti_dataPackage =None
        if self.Sheet_name=="工单流程测试一":
            dicti_dataPackage={"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单流程测试用例.xls", "表单名称": "工单流程测试一", "初始行": 2}
        elif self.Sheet_name=="工单流程测试二":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单流程测试用例.xls", "表单名称": "工单流程测试二","初始行": 2}
        elif self.Sheet_name == "工单流程测试三":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单流程测试用例.xls", "表单名称": "工单流程测试三","初始行": 2}
        elif self.Sheet_name == "工单流程测试四":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单流程测试用例.xls","表单名称": "工单流程测试四", "初始行": 2}
        elif self.Sheet_name == "权限检查对应模块":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单流程测试用例.xls","表单名称": "权限检查对应模块", "初始行": 1}
        elif self.Sheet_name == "全部权限用户账号":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单流程测试用例.xls","表单名称": "全部权限用户账号", "初始行": 1}
        elif self.Sheet_name == "全部权限用户账号（四组）":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单流程测试用例.xls","表单名称": "全部权限用户账号（四组）", "初始行": 1}
        elif self.Sheet_name == "全部权限用户账号（五组）":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单流程测试用例.xls","表单名称": "全部权限用户账号（五组）", "初始行": 1}
        return dicti_dataPackage


    def spreadsheet_WorkOrderList(self):
        """
        获取读取电子表格的地址和表名（测试用例用）：工单页面数据对比
        :return:
        """
        dicti_dataPackage =None
        if self.Sheet_name=="小程序首页工单":
            dicti_dataPackage={"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单清单测试用例.xls", "表单名称": "小程序首页工单", "初始行": 2}
        elif self.Sheet_name=="内部代办理工单":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单清单测试用例.xls", "表单名称": "内部代办理工单","初始行": 2}
        elif self.Sheet_name == "用户管理员区域管理员外协报修列表数据":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单清单测试用例.xls", "表单名称": "用户管理员区域管理员外协报修列表数据","初始行": 2}
        elif self.Sheet_name == "外部用户-我的报修":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单清单测试用例.xls","表单名称": "外部用户-我的报修", "初始行": 2}
        elif self.Sheet_name == "全部工单、紧急事件、驻场事件（包含已关单数据）":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单清单测试用例.xls", "表单名称": "全部工单、紧急事件、驻场事件（包含已关单数据）","初始行": 2}
        elif self.Sheet_name == "外协未关单工单列表页面":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单清单测试用例.xls", "表单名称": "外协未关单工单列表页面","初始行": 2}
        elif self.Sheet_name == "已关单列表数据":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\工单模块\\小程序工单清单测试用例.xls", "表单名称": "已关单列表数据","初始行": 2}
        return dicti_dataPackage


    def spreadsheet_SystemLogin(self):
        """
         获取电子表格需要读取的参数(系统登录模块)
        :return:
        """
        dicti_dataPackage = None
        if self.Sheet_name == "系统登录-电话号码登录":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\登录模块\\小程序登录模块测试用例.xls", "表单名称": "系统登录-电话号码登录","初始行": 2}
        return dicti_dataPackage


    def spreadsheet_AssetsEquipment(self):
        """
        获取读取电子表格的地址和表名（测试用例用）：资产设备清单页面数据对比
        :return:
        """
        dicti_dataPackage = None
        if self.Sheet_name == "设备清单页面测试":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\资产设备模块\\设备清单列表测试用例.xls", "表单名称": "设备清单页面测试", "初始行": 2}
        return dicti_dataPackage


    def spreadsheet_WorkOrderNumberStatistics(self):
        """
        获取读取电子表格的地址和表名（测试用例用）：报修数量统计
        :return:
        """
        dicti_dataPackage = None
        if self.Sheet_name == "报修数量":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\报修数量统计模块\\小程序报修统计模块测试用例.xls", "表单名称": "报修数据统计", "初始行": 2}
        elif self.Sheet_name == "故障数量":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\报修数量统计模块\\小程序报修统计模块测试用例.xls", "表单名称": "故障数量统计", "初始行": 2}
        return dicti_dataPackage


    def spreadsheet_complaint_list(self):
        """
         获取读取电子表格的地址和表名（测试用例用）：投诉模块
        :return:
        """
        dicti_dataPackage = None
        if self.Sheet_name == "投诉清单页面数据对比":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\投诉模块\\投诉清单测试用例.xls", "表单名称": "投诉清单页面测试", "初始行": 2}
        return dicti_dataPackage


    def spreadsheet_complaint_flow(self):
        """
         获取读取电子表格的地址和表名（测试用例用）：投诉模块
        :return:
        """
        dicti_dataPackage = None
        if self.Sheet_name == "投诉流程":
            dicti_dataPackage = {"详细地址": "\\data\\school\\testCase\\小程序自动化测试用例\\投诉模块\\投诉流程测试用例.xls", "表单名称": "投诉流程", "初始行": 2}
        return dicti_dataPackage


#######################################################################################################