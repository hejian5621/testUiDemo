#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 各个数据类型的参数处理方法


class DataType_processing:
    """各个数据类型的参数处理"""


    def __init__(self,inputParameter):
        self.inputParameter=inputParameter  # 需要处理的原始参数



    def dictiKeyValue_Newdicti(self, list_list_former_key):
        """
        判断传入字典数据类型的参数里，字典键对应的值是否有空值，如果有就去掉空值，并且替换掉没有空值键的名称。生成新的并且不为空的字典数据类型参数
        :return:
        """
        New_dicti = {}
        for list_former_key in list_list_former_key:  # 便利出需要替换的旧键和新键名
            former_key = list_former_key[0]  # 取出旧键名
            new_key = list_former_key[1]  # 取出新键名
            if former_key in  self.inputParameter:  # 判断旧键名是否在字典中
                value =  self.inputParameter[former_key]  # 如果在就取出对应的值
            else:
                value = None  # 如果没有值为空
            if value:  # 当值不为空的时候
                new_single_dicti = {new_key: value}  # 生成新的字典
            else:
                new_single_dicti = {}  # 当值为空的时候，新字典为空
            New_dicti = dict(New_dicti, **new_single_dicti)  # 合并字典
        return New_dicti


    def fetch_Database(self, key):
        """
         取出字典里指定键名的值
         from privately_owned.method import privately_owned
         value = privately_owned.fetch_Database(self)
        :return:
        """
        if self.parameter:
            assert_that(self.parameter).described_as('传进来的参数不是列表类型').is_instance_of(list)
            n = len(self.parameter)
            assert_that(n).described_as('传进来的列表有多个值').is_equal_to(1)
            dict_value = self.parameter[0]
            value = dict_value[key]
        else:
            value = 0
        return value


    def acquire_dataType(self):
        """
        判断传进来的参数的数据类型
        判断数据类型
        str_type=字符串
        list_type=列表
        dict_type=字典
        int_type=整数
        float_type=浮点
        :return:
        """
        data_type=None
        str_time = datetime.datetime.now()
        strtype = type(self.inputParameter)
        if strtype == type("abc"):  # 判断是否是字符串
            data_type = "str_type"
        elif strtype == type(["a", "b"]):  # 判断是否是列表
            data_type = "list_type"
        elif strtype == type({"a": "b"}):  # 判断是否是字典
            data_type = "dict_type"
        elif strtype == type(1):  # 判断是否是整数
            data_type = "int_type"
        elif strtype == type(1.1):  # 判断是否是小数
            data_type = "float_type"
        elif strtype == type(str_time):  # 判断是否是时间
            data_type = "time_type"
        elif strtype == type(None):  # 判断是否是空
            data_type = "None_type"
        elif strtype == type((1, 2)):  # 判断是否是元祖
            data_type = "tuple_type"
        elif strtype == type(set("a,b")):  # 判断是否是集合
            data_type = "set_type"
        return data_type


    def compile_property_data(self):
        """
        从字典中取出摸个值存入列表中
        :return:
        """
        if self.parameter != ['为空']:
            for self.argument in self.parameter:
                equipment_batch=self.argument["批次"]
                equipment_Name=self.argument["设备名称"]
                equipment_location=self.argument["位置信息"]
                equipment_type=self.argument["设备类型ID"]
                equipment_state=self.argument["设备状态"]
                dictionaries = {'批次':equipment_batch,'设备名称':equipment_Name,'位置信息':equipment_location,'设备类型':equipment_type,'设备状态':equipment_state}
                self.list1.append(dictionaries)
        return self.list1

    def RandomlyExtractListData(self):
        """
         随机取出列表数据
        :return:
        """
        number = 1
        n = len(self.parameter)
        if n > 11:
            number = random.uniform(1, 10)
        elif n < 11:
            number = random.uniform(1, n)
        number = int(number)
        list_parameters1 = random.sample(self.parameter, number)
        return list_parameters1



    def MultipleParameters_list(self,number,dicti_key):
        """
        根据多个列表随机取出每个列表的值生成新的列表嵌字典
        :return:
        """
        """数据初始化"""
        stochastic_n=None;argument1=True;argument2=True;argument3=True;dicti0=None;dicti1=None;dicti2=None;dicti3=None
        random_parameter0=None;random_parameter1=None;random_parameter2=None;random_parameter3=None;list_screening_condition=[]
        screening_condition=None
        # 获取列表长度
        stochastic_n=len(self.parameter)
        # 取出列表的第一个值
        list0 = self.parameter[0]
        # 获取随机数据
        n0 = number[0]
        # 获取key键
        dicti0=dicti_key[0]
        # 获取准确的值
        random_parameter0=random.sample(list0,n0)
        # 判断有没有超过列表的值
        if 2<=stochastic_n:
            list1 = self.parameter[1]
            n1 = number[1]
            dicti1 = dicti_key[1]
            random_parameter1 = random.sample(list1, n1)
            argument1 = True
            if 3 <= stochastic_n:
                list2 = self.parameter[2]
                n2 = number[2]
                dicti2 = dicti_key[2]
                random_parameter2 = random.sample(list2, n2)
                argument2 = True
                if 4 <= stochastic_n:
                    list3 = self.parameter[3]
                    n3 = number[3]
                    dicti3 = dicti_key[3]
                    random_parameter3 = random.sample(list3, n3)
                    argument3 = True
                else:
                    argument3 = False
            else:
                argument2 = False
        else:
            argument1 =False
        for parameter0 in random_parameter0:
            if argument1 == True:
                for parameter1 in random_parameter1:
                    if argument2 == True:
                        for parameter2 in random_parameter2:
                            if argument3 == True:
                                for parameter3 in random_parameter3:
                                    screening_condition={dicti0:parameter0,dicti1:parameter1,dicti2:parameter2,dicti3:parameter3}
                                    list_screening_condition.append(screening_condition)
                            else:
                                screening_condition = {dicti0: parameter0, dicti1: parameter1, dicti2: parameter2}
                                list_screening_condition.append(screening_condition)
                    else:
                        screening_condition = {dicti0: parameter0, dicti1: parameter1}
                        list_screening_condition.append(screening_condition)
            else:
                screening_condition = {dicti0: parameter0}
                list_screening_condition.append(screening_condition)
        return list_screening_condition



    def list_nest_dict_list(self, dict_value):
        """
        列表嵌套字典取出字典的值生成列表
        [{'单位ID': '70b07dc7333f40b4888ee1c1f8fad195', '单位名称': '武汉市第二高级中学', 'COUNT(*)': 11},
         {'单位ID': '8c970aecfe6a478ebdd2be43b4b670e8', '单位名称': '生物城第一高级中学', 'COUNT(*)': 5}]
        :return:列表
         """
        list1=None
        # 取出列表的值
        if self.parameter:
            if self.parameter[0] != "为空":
                # 获取传入的参数的数据类型
                data_type = DataType_processing(self.inputParameter).acquire_dataType()
                if data_type == "str_type" or data_type == "dict_type":
                    print("预期传入的参数应该是列表嵌字典，实际不是：", self.parameter, __file__, sys._getframe().f_lineno)
                    os._exit(0)
                elif data_type == "list_type":
                    for paramete in self.parameter:
                        # 获取传入的参数的数据类型
                        data_type1 = DataType_processing(paramete).acquire_dataType()
                        if data_type1 == "str_type" or data_type1 == "list_type":
                            print("预期传入的参数应该是列表嵌字典，实际不是：", paramete, __file__, sys._getframe().f_lineno)
                            os._exit(0)
                        elif data_type1 == "dict_type":
                            dictValue = paramete[dict_value]
                            list1.append(dictValue)
            else:
                list1 = None
        else:
            list1 = None
        return list1



    def ListDictionary_repetition(self):
        """
        判断列表嵌字典数据类型，有没有重复数据
        self.parameter: 列表返回的实际数据
        self.argument:
        :return:
        """
        testResul = True;testReport = None;new_parameter = [];duplicated = set()
        # 把列表嵌套字典里的字典转化成字符串，变成列表
        for para in self.inputParameter:  #便利出列表嵌套字典里的字典
            new_para = str(para)     # 把字典转化成字符串
            new_parameter.append(new_para)  # 把转化的字符串放入列表
        # 取出重复的值
        for i in range(0, len(new_parameter)):
            if new_parameter[i] in new_parameter[i + 1:]:
                duplicated.add(new_parameter[i])
        # 判断返回的值是否为空
        if duplicated !=set() :
            testResul = False
            testReport=str(duplicated)   # 获取字符串格式测试报告
        return testResul,testReport