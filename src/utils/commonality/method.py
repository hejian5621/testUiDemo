from config.readconfig import ProfileDataProcessing
from utils.commonality.database_SqlRealize import dataProcessing
from place import ProjectFolderLocation
from collections import Counter
from assertpy import assert_that
import random,time,re,sys,os,datetime
from tqdm import tqdm
from utils.privately_owned.DataType_ParameterProcessing import DataType_processing

# 所有软件都可以用的公共方法

class  EachQuantityType_transition_CharacterString:
    """
    各种数量类型转换成字符串
    """

    def __init__(self, introduction , argument=None):
        self.introduction  = introduction
        self.argument = argument
        self.list1 = []
        self.Str_dict = None
        self.Str_list = None
        self.Str =None
        # 返回值
        self.ReturnString=None


    def DataTypeConversion_console(self):
        """
        数据类型转化成字符串--控制台
        :return:
        """
        type1 =None ; type2 =None ;type3 =None
        # 判断传过来的值是否是空
        if self.introduction:
            list_type=EachQuantityType_transition_CharacterString(self.introduction).gain_structure_Data_type()
            if  list_type==["str1"]:
                self.ReturnString = self.introduction
            elif list_type==["list1", "list2","str3"]:
                # 列表嵌套列表
                self.ReturnString=EachQuantityType_transition_CharacterString(self.introduction).listNestlist_Str()
            elif list_type==["list1", "dict2","str3"]:
                # 列表嵌套字典
                self.ReturnString = EachQuantityType_transition_CharacterString(self.introduction).listNestDict_Str()
            elif list_type==["dict1", "list2","str3"]:
                # 字典嵌套列表
                self.ReturnString = EachQuantityType_transition_CharacterString(self.introduction).DictNestlist_Str()
            elif list_type==["dict1", "dict2","str3"]:
                # 字典嵌套字典
                self.ReturnString = EachQuantityType_transition_CharacterString(self.introduction).DictNestDict_Str()
            else:
                # 没有嵌套
                self.ReturnString = EachQuantityType_transition_CharacterString(self.introduction).VariousCharacterTypes_change_str()
        return self.ReturnString


    def gain_structure_Data_type(self):
        """
        获取类型嵌套数据结构类型
        :return:
        """
        type1 = None;type2 = None;type3 = None;type4=None;type5=None
        list_type =[]
        # 判断传过来的值是否是空
        if self.introduction:
            # 判断传过来的值数据类型
            data_type = DataType_processing(self.introduction).acquire_dataType()
            """第一级"""
            if data_type == "str_type" or data_type == "int_type" or data_type == "float_type":
                type1 = "str1"
            elif data_type == "list_type":
                type1 = "list1"
                parameters2 = self.introduction[0]
                """第二级"""
                # 判断参数的数据类型
                data_type1 = DataType_processing(parameters2).acquire_dataType()
                if data_type1 == "str_type" or data_type1 == "int_type" or data_type1 == "float_type":
                    type2 = "str2"
                elif data_type1 == "list_type":
                    type2 = "list2"
                    parameters3 = parameters2[0]
                    """第三级"""
                    data_type2 = DataType_processing(parameters3).acquire_dataType()
                    if data_type2 == "str_type" or data_type2 == "int_type" or data_type2 == "float_type":
                        type3 = "str3"
                    elif data_type2 == "list_type":
                        type3 = "list3"
                        parameters4 = parameters3[0]
                        """第四级"""
                        data_type3 = DataType_processing(parameters4).acquire_dataType()
                        if data_type3 == "str_type" or data_type3 == "int_type" or data_type3 == "float_type":
                            type4 = "str4"
                        elif data_type3 == "list_type":
                            type4 = "list4"
                            parameters5 = parameters4[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        elif data_type3 == "dict_type":
                            type4 = "dict4"
                            parameters5 = list(parameters4.values())[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        else:
                            type4 = "null4"
                    elif data_type2 == "dict_type":
                        type3 = "dict3"
                        parameters4 = parameters3[0]
                        """第四级"""
                        data_type3 = DataType_processing(parameters4).acquire_dataType()
                        if data_type3 == "str_type" or data_type3 == "int_type" or data_type3 == "float_type":
                            type4 = "str4"
                        elif data_type3 == "list_type":
                            type4 = "list4"
                            parameters5 = parameters4[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        elif data_type3 == "dict_type":
                            type4 = "dict4"

                            parameters5 = parameters4[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        else:
                            type4 = "null4"
                    else:
                        type3 = "null3"
                elif data_type1 == "dict_type":
                    type2 = "dict2"
                    parameters3 = list(parameters2.values())[0]
                    """第三级"""
                    data_type2 = DataType_processing(parameters3).acquire_dataType()
                    if data_type2 == "str_type" or data_type2 == "int_type" or data_type2 == "float_type":
                        type3 = "str3"
                    elif data_type2 == "list_type":
                        type3 = "list3"
                        parameters4 = parameters3[0]
                        """第四级"""
                        data_type3 = DataType_processing(parameters4).acquire_dataType()
                        if data_type3 == "str_type" or data_type3 == "int_type" or data_type3 == "float_type":
                            type4 = "str4"
                        elif data_type3 == "list_type":
                            type4 = "list4"
                            parameters5 = parameters4[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        elif data_type3 == "dict_type":
                            type4 = "dict4"
                            parameters5 = parameters4[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        else:
                            type4 = "null4"
                    elif data_type2 == "dict_type":
                        type3 = "dict3"
                        parameters4 = list(parameters3.values())[0]
                        """第四级"""
                        data_type3 = DataType_processing(parameters4).acquire_dataType()
                        if data_type3 == "str_type" or data_type3 == "int_type" or data_type3 == "float_type":
                            type4 = "str4"
                        elif data_type3 == "list_type":
                            type4 = "list4"
                            parameters5 = parameters4[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        elif data_type3 == "dict_type":
                            type4 = "dict4"
                            parameters5 = list(parameters4.values())[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        else:
                            type4 = "null4"
                    else:
                        type3 = "null3"
            elif data_type == "dict_type":
                type1 = "dict1"
                parameters2 = list(self.introduction.values())[0]
                # 判断参数的数据类型
                """第二级"""
                data_type1 = DataType_processing(parameters2).acquire_dataType()
                if data_type == "str_type" or data_type == "int_type" or data_type == "float_type":
                    type2 = "str2"
                elif data_type1 == "list_type":
                    type2 = "list2"
                    parameters3 = parameters2[0]
                    """第三级"""
                    data_type2 = DataType_processing( parameters3).acquire_dataType()
                    if data_type2 == "str_type" or data_type2 == "int_type" or data_type2 == "float_type":
                        type3 = "str3"
                    elif data_type2 == "list_type":
                        type3 = "list3"
                        parameters4 = parameters3[0]
                        """第四级"""
                        data_type3 = DataType_processing(parameters4).acquire_dataType()
                        if data_type3 == "str_type" or data_type3 == "int_type" or data_type3 == "float_type":
                            type4 = "str4"
                        elif data_type3 == "list_type":
                            type4 = "list4"
                            parameters5 = parameters4[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        elif data_type3 == "dict_type":
                            type4 = "dict4"
                            parameters5 = list(parameters4.values())[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        else:
                            type4 = "null4"
                    elif data_type2 == "dict_type":
                        type3 = "dict3"
                        parameters4 = list(parameters3.values())[0]
                        """第四级"""
                        data_type3 = DataType_processing(parameters4).acquire_dataType()
                        if data_type3 == "str_type" or data_type3 == "int_type" or data_type3 == "float_type":
                            type4 = "str4"
                        elif data_type3 == "list_type":
                            type4 = "list4"
                            parameters5 = parameters4[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        elif data_type3 == "dict_type":
                            type4 = "dict4"
                            parameters5 = list(parameters4.values())[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        else:
                            type4 = "null4"
                    else:
                        type3 = "null3"
                elif data_type1 == "dict_type":
                    type2 = "dict2"
                    parameters3 = list(parameters2.values())[0]
                    """第三级"""
                    data_type2 = DataType_processing(parameters3).acquire_dataType()
                    if data_type2 == "str_type" or data_type2 == "int_type" or data_type2 == "float_type":
                        type3 = "str3"
                    elif data_type2 == "list_type":
                        type3 = "list3"
                        parameters4 = parameters3[0]
                        """第四级"""
                        data_type3 = DataType_processing(parameters4).acquire_dataType()
                        if data_type3 == "str_type" or data_type3 == "int_type" or data_type3 == "float_type":
                            type4 = "str4"
                        elif data_type3 == "list_type":
                            type4 = "list4"
                            parameters5 = parameters4[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        elif data_type3 == "dict_type":
                            type4 = "dict4"
                            parameters5 = list(parameters4.values())[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        else:
                            type4 = "null4"
                    elif data_type2 == "dict_type":
                        type3 = "dict3"
                        parameters4 = list(parameters3.values())[0]
                        """第四级"""
                        data_type3 = DataType_processing(parameters4).acquire_dataType()
                        if data_type3 == "str_type" or data_type3 == "int_type" or data_type3 == "float_type":
                            type4 = "str4"
                        elif data_type3 == "list_type":
                            type4 = "list4"
                            parameters5 = parameters4[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        elif data_type3 == "dict_type":
                            type4 = "dict4"
                            parameters5 = list(parameters4.values())[0]
                            """第五级"""
                            data_type4 = DataType_processing(parameters5).acquire_dataType()
                            if data_type4 == "str_type" or data_type4 == "int_type" or data_type4 == "float_type":
                                type5 = "str5"
                            elif data_type4 == "list_type":
                                type5 = "list5"
                            elif data_type4 == "dict_type":
                                type5 = "dict5"
                            else:
                                type5 = "null5"
                        else:
                            type4 = "null4"
                    else:
                        type3 = "null3"
                else:
                    type2 = "null2"
        if type1:
            list_type.append(type1)
        if type2:
            list_type.append(type2)
        if type3:
            list_type.append(type3)
        if type4:
            list_type.append(type4)
        if type5:
            list_type.append(type5)
        return list_type


    def DictNestDict_Str(self):
        """
        字典嵌套字典转化成字符串
        :return:
        """
        dicti_value = {}
        # 取出列表里嵌套的字典
        for key, value in self.introduction.items():  # 便利出字典测键和值
            str_value = str(value)
            #  字典转化成字符串
            dicti_value[key] = str_value
        # 列表转化成字符串
        self.ReturnString = str(dicti_value)
        return self.ReturnString


    def DictNestlist_Str(self):
        """
        字典嵌套列表转化成字符串
        :return:
        """
        dicti_value = {}
        # 取出列表里嵌套的字典
        for key,  value in self.introduction.items(): # 便利出字典测键和值
            str_value =[str(i) for i in value]
            #  字典转化成字符串
            dicti_value[key]=str_value
        # 列表转化成字符串
        self.ReturnString = str(dicti_value)
        return self.ReturnString



    def listNestlist_Str(self):
        """
        列表嵌套列表转化成字符串
        :return:
        """
        list_value = []
        # 取出列表里嵌套的字典
        for Dict_argument in self.introduction:
            #  字典转化成字符串
            str_value = [str(i) for i in Dict_argument]
            list_value.append(str_value)
        # 列表转化成字符串
        self.ReturnString = [str(i) for i in list_value]
        return self.ReturnString


    def listNestDict_Str(self):
        """
         列表嵌套字典转化成字符串
        :return:
        """
        list_value = []
        # 取出列表里嵌套的字典
        for Dict_argument in self.introduction:
            #  字典转化成字符串
            str_value = str(Dict_argument)
            list_value.append(str_value)
        # 列表转化成字符串
        self.ReturnString = [str(i) for i in list_value]
        return self.ReturnString


    def VariousCharacterTypes_change_str(self):
        """
        各种类型数据转化成字符串
        :return:
        """
        if self.introduction:
            # 判断参数的数据类型
            data_type = DataType_processing(self.introduction).acquire_dataType()
            self.ReturnString = None
            # 如果参数是字符串，直接返回参数
            if data_type == "str_type":
                self.ReturnString = self.introduction
            # 如果参数是列表，转化成字符串返回
            elif data_type == "list_type":
                self.ReturnString = "【"+self.introduction[0]+"】"
                for a in self.introduction:
                    a ="【"+a+"】"
                    if self.ReturnString != a:
                        self.ReturnString = self.ReturnString +"；"+a
            # 如果参数是字典类型，转化成字符串返回
            elif data_type == "dict_type":
                #    取出
                for key, value in self.introduction.items():
                    StrKey = list(self.introduction.keys())[0]
                    StrValue = list(self.introduction.values())[0]
                    StrKey =str(StrKey)
                    StrValue = str(StrValue)
                    if key == StrKey:
                        self.ReturnString = "“" + StrKey + ":" + StrValue + "”"
                        pass
                    else:
                        value = str(value)
                        key = str(key)
                        single = key + ":" + value
                        self.ReturnString = self.ReturnString + "、" + "“" + single + "”"
            elif data_type == None:
                self.ReturnString="为空"
        else:
            self.ReturnString = "为空"
        return self.ReturnString









