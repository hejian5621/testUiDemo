#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 处理时间格式的方法


import datetime,time
from dateutil.relativedelta import relativedelta




class TimeFormat:
    """时间格式处理"""


    def __init__(self, date_parameter=None,arguments=None):
        self.date_parameter = date_parameter
        self.arguments=arguments
        self.returningData = None
        self.finish_date=[]   # 日期
        self.begin_date=[]
        self.list1=[]
        self.optionDate=None


    def complain_dateParameter_RealDate(self):
        """
        投诉模块--日期参数转换成实际的日期
        :return:
        """
        date = None
        if self.date_parameter == None:  date = "本月"
        elif self.date_parameter == 2:   date = "近七天"
        elif self.date_parameter == 1:   date = "上月"
        elif self.date_parameter == 3:   date = "近三月"
        elif self.date_parameter == 6:   date = "近半年"
        elif self.date_parameter == 7:   date = "本年度"
        elif self.date_parameter == 8:   date = "全部"
        elif self.date_parameter == 9:   date = "随机日期"
        elif self.date_parameter == 10:  date = "当天"
        self.returningData = TimeFormat(date).dateParameter_actualDate()
        return self.returningData


    def dateParameter_actualDate(self):
        """
        选择筛选日期（当天,近七天，本月，上月，近三月，近半年，本年度，全部，随机）
        近七天：今天向前推7天；本月：今天向前推一个月；上月：上月；近三月：从今天推进三个月；
        近半年：今天向前推半年；本年度：本年；全部：从2015-01-01到今天；随机：夸月随机选择
        :param parameter:选择的日期
        :return:optionDate 日期列表
        :return:
        """
        DateMonthYear = datetime.datetime.now().strftime("%Y-%m-%d")       # 当天日期
        if self.date_parameter == "近七天":
            date = (datetime.datetime.now() + datetime.timedelta(days=-7)).strftime("%Y-%m-%d ")
            self.begin_date.append(date)
            self.finish_date.append(DateMonthYear)
        elif self.date_parameter == "当天":
            self.begin_date.append(DateMonthYear)    # 获取开始日期
            self.finish_date.append(DateMonthYear)   # 获取结束日期
        elif self.date_parameter == "本月":
            date1 = datetime.datetime.now().strftime("%Y-%m")
            date = date1 + "-" + "01"
            self.begin_date.append(date)   # 获取开始日期
            self.finish_date.append(DateMonthYear)  # 获取结束日期
        elif self.date_parameter == "上月":
            date1 = (datetime.datetime.now() + relativedelta(months=-1)).strftime("%Y-%m")    # 获取上月日期
            date = date1 + "-" + "01"   # 截取日期
            year, month, day = str(date).split("-");year = int(year);month = int(month);day = int(day)  # 年月日转化成整数
            any_day = datetime.date(year, month, day);next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
            self.begin_date.append(date)    # 获取开始日期
            self.finish_date.append((next_month - datetime.timedelta(days=next_month.day)))   # 获取结束日期
        elif self.date_parameter == "近三月":
            date1 = (datetime.datetime.now() + relativedelta(months=-2)).strftime("%Y-%m")
            date = date1 + "-" + "01"
            self.begin_date.append(date)              # 获取开始日期
            self.finish_date.append(DateMonthYear)    # 获取结束日期
        elif self.date_parameter == "近半年":
            date1 = (datetime.datetime.now() + relativedelta(months=-5)).strftime("%Y-%m")
            date = date1 + "-" + "01"
            self.begin_date.append(date)                  # 获取开始日期
            self.finish_date.append(DateMonthYear)        # 获取结束日期
        elif self.date_parameter == "本年度":
            date1 = datetime.datetime.now().strftime("%Y ")
            date1 = date1.replace(" ","")
            date = date1+"-"+"01" +"-"+"01"
            self.begin_date.append(date)                  # 获取开始日期
            self.finish_date.append(DateMonthYear)        # 获取结束日期
        elif self.date_parameter == "全部":
            date = '2015-01-01'
            self.begin_date.append(date)
            self.finish_date.append(DateMonthYear)
        elif self.date_parameter == "随机日期":
            date1 = '2019-01-01 00:00:00'
            timeArray = time.strptime(date1, "%Y-%m-%d %H:%M:%S")
            date2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            timeArray2 = time.strptime(date2, "%Y-%m-%d %H:%M:%S")
            start = time.mktime(timeArray)  # 生成开始时间戳
            end = time.mktime(timeArray2)  # 生成结束时间戳
            # 随机生成4个日期字符串
            for i in range(2):
                import random
                t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
                date_touple = time.localtime(t)  # 将时间戳生成时间元组
                date1 = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
                self.list1.append(date1)
            self.list1.sort()
            self.begin_date.append(self.list1[0])     # 获取开始日期
            self.finish_date.append(self.list1[1])    # 获取结束日期
        else:
            self.begin_date =None
        if self.begin_date:
            finish_date1=[]
            begin_date1=[]
            for date1 in self.finish_date:
                date1 = str(date1)+" "+"23:59:59"
                finish_date1.append(date1)            # 获取开始日期
            for date2 in self.begin_date:
                date2 = date2+" "+"00:00:00"
                begin_date1.append(date2)             # 获取结束日期
            self.optionDate = {"开始日期": begin_date1, "结束日期": finish_date1}
        else:
            self.optionDate = {"开始日期": None, "结束日期": None}
        return self.optionDate


    def workOrderRepairs_AppointmentTime(self):
        """
        一键报修--预约时间段--时间获取
        参数10表示：8:30-10:00；参数20表示：10:00-11:30；参数30表示：13:00-15:30；参数40表示：15:30-17:30；
        :return:
        """
        AppointmentTimeList=None
        # systemTime = passShh_connectToServer("%Y-%m-%d %H:%M:%S").Get_server_time() # 获取服务器实时时间
        systemTime =time.strftime("%Y-%m-%d %H:%M:%S")              # 获取服务器实时时间
        date=systemTime[:10]                # 截取日期
        hour_minute=systemTime[11:16]       # 截取时和分钟
        if self.date_parameter == date:
            if   hour_minute<"8:30":
                AppointmentTimeList=["10", "20", "30", "40"]
            elif  "8:30" >=hour_minute <"10:00" :
                AppointmentTimeList = ["20", "30", "40"]
            elif  "10:00" >=hour_minute <"13:00" :
                AppointmentTimeList = ["30", "40"]
            elif  "13:00" >=hour_minute <"15:30" :
                AppointmentTimeList = ["40"]
        else:
            AppointmentTimeList = ["10","20","30","40"]
        return AppointmentTimeList






    def timeFormat_StrFormat(self):
        """
        时间格式转化成字符串格式，并且格式化时间字符串
        传入的参数数据类型支持：列表嵌套字典，列表嵌套列表、单独的字符串和单独的时间格式
        :return:
        """
        # 获取传入的参数的数据类型

        # 取出传入参数的值。通过for循环取出参数的值

        # 判断参数值的数据类型。如果值是时间格式，就转化成字符串，并格式化值；如果值是字符串，就直接格式化值

        # 在把格式化的值




    def listNestDict_TimeType_str(self):
        """
        列表嵌套字典，截取时间字符串
        :return:
        """
        for change_data in self.date_parameter:
            for Trans in self.arguments:
                # 取出需要转化的参数
                need_timeType = change_data[Trans]
                # 转化
                succeed_timeType = str(need_timeType)
                change_data[Trans] = succeed_timeType
            self.newData.append(change_data)
        return self.newData


    def CaptureTheAate(self, FormatOfTime):
        """
        处理字典里的时间参数（时间格式转化成字符串）
        :return:
        """
        for change_data in self.need_change_data:
            for Trans in self.Transformation:
                otherStyleTime = None;startTime = None;need_timeType = None
                need_timeType = change_data[Trans]  # 取出需要转化的参数
                dataType = isinstance(need_timeType, datetime.datetime)  # 判断
                if dataType == True:
                    if need_timeType:
                        # 字符串转化成时间格式
                        startTime = time.strptime(need_timeType, "%Y-%m-%d %H:%M:%S")
                        # 转化自己想要的时间格式
                        otherStyleTime = time.strftime(FormatOfTime, startTime)
                    else:
                        otherStyleTime = None
                # 存入参数
                change_data[Trans] = otherStyleTime
            self.newData.append(change_data)
        return self.newData

