#  电子表格
#coding:utf-8
from log import log
import sys,xlwt,os,time,xlrd
from xlrd import open_workbook
from xlutils.copy import copy
from relative_location import relative_site
from config.readconfig import ProfileDataProcessing
from utils.commonality.spreadsheet_tableCell_style import CellStyle



class reportTest_spreadsheet:

    """
        1、新建测试报告（电子表格）
        2、初始化样式
    """

    def __init__(self,table_name,sheet_name=None,workbook=None):
        self.table_name=table_name   # 电子表格表单名称
        self.sheet_name = sheet_name # 电子表格名称
        self.workbook = workbook


    def spreadsheet_CreateAForm(self):
        """
        新建测试报告电子表格文件
        :return:
        """
        print("开始新建测试报告表", __file__, sys._getframe().f_lineno)
        log.log("开始新建测试报告表", __file__, sys._getframe().f_lineno)
        style = xlwt.XFStyle()  # 创建样式
        self.sheet_name = "测试报告"
        workbook = xlwt.Workbook(encoding='utf-8')  # 新建工作簿
        sheet = workbook.add_sheet(self.sheet_name)  # 新建sheet
        # 设置单元格高
        tall_style = xlwt.easyxf('font:height 360')
        first_row = sheet.row(0)
        first_row.set_style(tall_style)
        first_row1 = sheet.row(1)
        first_row1.set_style(tall_style)
        # 样式：居中
        al = CellStyle().spreadsheet_CreateAForm_style_alignCenter()
        # 样式：添加边框
        borders = CellStyle().spreadsheet_CreateAForm_style_rim()
        # 把样式和边框导给样式style
        style.borders = borders
        style.alignment = al
        # 设置列表的宽
        sheet.col(0).width = 256 * 30
        sheet.col(1).width = 256 * 20
        sheet.col(2).width = 256 * 30
        sheet.col(3).width = 256 * 30
        sheet.col(4).width = 256 * 30
        sheet.col(5).width = 256 * 30
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        sheet.write_merge(0, 0, 0, 5, '%r测试报告' % t, style)   # 输入标题
        # 输入副标题
        sheet.write(1, 0, "所属接口", style)
        sheet.write(1, 1, "所属模块", style)
        sheet.write(1, 2, " 测试点", style)
        sheet.write(1, 3, "预期结果", style)
        sheet.write(1, 4, "实际结果", style)
        sheet.write(1, 5, "测试结果", style)
        relativeAddress = relative_site.location()   # 获取项目相对位置
        # 获取测试的系统
        systematicName = ProfileDataProcessing("commonality", "system").config_File()
        # 拼接测试模板位置
        fileAddress = relativeAddress +"report"+"/"+systematicName+"/"+self.table_name
        print("fileAddress", fileAddress)
        workbook.save(fileAddress)
        # 返回表单名和测试报告名称用以插入数据
        print("测试报告表新建完成", __file__, sys._getframe().f_lineno)
        log.log("开始新建测试报告表", __file__, sys._getframe().f_lineno)
        return self.sheet_name, self.table_name


    def spreadsheet_amend(self):
        """
        打开测试报告模板
        sheet_name: 表单名
        table_name: 表名
        :return:
        """
        print("打开测试报告", __file__, sys._getframe().f_lineno)
        relativeAddress = relative_site.location()   # 获取项目相对位置
        fileAddress = relativeAddress + "report\\ChangeTheValue\\testReport_template" + "\\" + self.table_name # 拼接获取测试报告模板完整的地址
        rb = open_workbook(fileAddress, formatting_info=True)         # 打开电子表格格式的测试报告模板
        workbook = copy(rb)                                           # 把测试报告内容缓存放入到测试报告模板内
        sheet = workbook.get_sheet(self.sheet_name)
        print("已打开新建的表单", __file__, sys._getframe().f_lineno)
        return workbook, sheet


    def spreadsheet_SaveCloseTable(self,table_name):
        """
        保存并关闭测试报告
        :param table_name: 测试报告名称
        :return:
        """
        relativeAddress = relative_site.location()   # 获取项目相对位置
        # 获取测试的系统
        systematicName = ProfileDataProcessing("commonality", "system").config_File()
        # 拼接地址
        fileAddress = relativeAddress + "report" + "/" +systematicName+"/"+ table_name
        self.workbook.save(fileAddress)     # 保存测试报告
        print("关闭测试报告", __file__, sys._getframe().f_lineno)


    def report_readInData(self,list,row=3):
        """
        写入测试报告
        :param list: 列
        :param row: 行
        :return:
        """
        print("向电子表格第%d行写入数据:" % row, list)
        # 样式初始化
        style = xlwt.XFStyle()
        # 列初始化
        line = 0
        # 样式居中
        al = CellStyle().spreadsheet_CreateAForm_style_alignCenter()
        # 样式：添加边框
        borders = CellStyle().spreadsheet_CreateAForm_style_rim()
        style.borders = borders
        style.alignment = al
        # 增加高
        tall_style = xlwt.easyxf('font:height 360')
        first_row = self.sheet_name.row(row)
        first_row.set_style(tall_style)
        # 把list的值输入到表单中
        for i in list:
            self.sheet_name.write(row, line, i, style)
            line = line + 1
        row = row + 1
        # 返回行数和表
        return row








class read_spreadsheet:
    """读取电子表格"""
    
    def __init__(self,dataPackage):
        self.dataPackage=dataPackage


    def ReadingSpreadsheets_listNestedDicti(self):
        """
        读取电子表格里的内容生成列表嵌套字典数据类型的值
        :param  self.dataPackage: {"详细地址":"detailedAddress","表单名称":"menu_table_name","初始行":"onset",} 需要读取电子表格的地址
        :return:
        """
        detailedAddress=self.dataPackage["详细地址"];menu_table_name=self.dataPackage["表单名称"];onset=self.dataPackage["初始行"]
        list_dicti_Excel = [] # 空的列表
        relativeAddress = relative_site.location()   # 获取项目相对位置
        if detailedAddress and menu_table_name and onset:  # 判断详细地址、表单名称和初始行都不为空的情况下
            CompleteAddress = relativeAddress + detailedAddress  # 获取完整的地址
            data = xlrd.open_workbook(CompleteAddress)  # 打开需要读取的电子表格
            table = data.sheet_by_name(menu_table_name)  # 根据表单名称获取对应表单的数据
            rowns = table.nrows  # 获取总行数
            list_row_title = table.row_values(onset - 1)  # 取出标题行一行的数据
            while rowns > onset:
                list_row_value = table.row_values(onset)  # 获取整行的值
                dicti_Excel = dict(zip(list_row_title, list_row_value))  # 标题列表跟值列表合并成字典
                onset = onset + 1
                list_dicti_Excel.append(dicti_Excel)
        else:
            print("传入的电子表格地址、表单名称和初始行数不能为空，表格地址：%r；表单名称：%r；初始行数：%r"%(detailedAddress,menu_table_name,onset), __file__, sys._getframe().f_lineno)
            os._exit(0)
        return  list_dicti_Excel


    def ReadingSpreadsheets_listNestedlist(self):
        """
        读取电子表格里的内容生成列表嵌列表数据类型的值
        :param  self.dataPackage: [[1,2],[3,4]] 需要读取电子表格的地址
        :return:
        """
        detailedAddress = self.dataPackage["详细地址"];menu_table_name = self.dataPackage["表单名称"];onset = self.dataPackage["初始行"]
        list_dicti_Excel = []  # 空的列表
        relativeAddress = relative_site.location()   # 获取项目相对位置
        if detailedAddress and menu_table_name and onset:
            CompleteAddress = relativeAddress + detailedAddress  # 获取完整的地址
            data = xlrd.open_workbook(CompleteAddress)  # 打开需要读取的电子表格
            table = data.sheet_by_name(menu_table_name)  # 根据表单名称获取对应表单的数据
            rowns = table.nrows  # 获取总行数
            while rowns > onset:
                list_row_value = table.row_values(onset)  # 获取整行的值
                list_row_value =[i for i in list_row_value if i != '']
                list_dicti_Excel.append(list_row_value)
                onset = onset + 1
        return list_dicti_Excel


