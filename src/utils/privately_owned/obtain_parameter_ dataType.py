#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 获取传入的参数数据结构类型
import datetime
from utils.privately_owned.DataType_ParameterProcessing import DataType_processing


class obtain_parameter_DataResultType:


    def __init__(self,parameter,argument=None):
        self.parameter = parameter
        self.argument = argument
        self.data_type=None



    def acquire_dataType(self):
        """
        获取传入的参数的数据类型（单层）
        self.parameter：传入的参数
        :return:str_type:字符串
                list_type:列表
                dict_type:字典
                int_type:整数
                float_type:浮点
        """
        str_time =datetime.datetime.now()
        strtype=type(self.parameter)
        if strtype == type("abc"):  # 判断是否是字符串
            self.data_type = "str_type"
        elif strtype == type(["a","b"]):  # 判断是否是列表
            self.data_type = "list_type"
        elif strtype == type({"a":"b"}):  # 判断是否是字典
            self.data_type = "dict_type"
        elif strtype == type(1):  # 判断是否是整数
            self.data_type = "int_type"
        elif strtype == type(1.1):  # 判断是否是小数
            self.data_type = "float_type"
        elif strtype == type(str_time):  # 判断是否是时间
            self.data_type = "time_type"
        elif strtype == type(None):  # 判断是否是空
            self.data_type = "None_type"
        elif strtype == type((1,2)):  # 判断是否是元祖
            self.data_type = "tuple_type"
        elif strtype == type(set("a,b")):  # 判断是否是集合
            self.data_type = "set_type"
        return self.data_type


    def gain_structure_Data_type(self):
        """
        获取类型嵌套数据结构类型
        :return:
        """
        type1 = None;type2 = None;type3 = None;type4=None;type5=None
        list_type =[]
        # 判断传过来的值是否是空
        if self.parameter:
            # 判断传过来的值数据类型
            data_type = DataType_processing(self.parameter).acquire_dataType()
            """第一级"""
            if data_type == "str_type" or data_type == "int_type" or data_type == "float_type":
                type1 = "str1"
            elif data_type == "list_type":
                type1 = "list1"
                parameters2 = self.parameter[0]
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