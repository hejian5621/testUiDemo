#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @当前项目名 : python demo
# 打印进度条方法



class ProgressBar:
    """控制台打印进度条方法"""

    def __init__(self,Entries,amount=None):
        self.Entries=Entries      # 个数
        self.amount = amount       # 总数


    def progressBar_number(self):
        """
        进度条打印，打印个数
        :return:
        """
        sumTotal = None;rateOfProgress = None
        if self.Entries < self.amount:
            sumTotal = "总“" + str(self.amount) + "”条"
            rateOfProgress = "第“%r”条" % self.Entries
            per_str = "\033[1;34;40m\r%r[%s%s]%r" % (sumTotal, "*" * self.Entries, "-" * (self.amount - self.Entries), rateOfProgress)
            print(per_str, end='', flush=True)
        else:
            sumTotal = "总“" + str(self.amount) + "”条"
            rateOfProgress = "数据处理完毕"
            per_str = "\033[1;34;40m\r%r[%s%s]%r" % (sumTotal, "*" * self.Entries, "-" * (self.amount - self.Entries), rateOfProgress)
            print(per_str)
        # time.sleep(0.3)


    def progressBar_percent(self):
        """
        进度条打印，打印百分比
        :return:
        """
        print('percent: {:.0%}'.format(self.Entries /  self.amount), flush=True)