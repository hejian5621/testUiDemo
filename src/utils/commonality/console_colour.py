from privately_owned.method import EachQuantityType_transition_CharacterString


class Complaint_ConsolePrint:
    """控制台打印"""

    def __init__(self,explanatoryNote,argument=None):
        self.explanatoryNote=explanatoryNote
        self.argument = argument



    def  ProcessDivider_one(self):
        print("\033[5;34;41mm&&&&&&&&&&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&&&&&&&&&&&&&&&&&&&")
        print("\033[5;34;41mm&&&&&&&&&&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&&&&&&&&&&&&&&&&&&&")

    def ProcessDivider_two(self):
        print("\033[5;32;40m(((((((((((((((%(%(%(%%(%(%(%(%(%(%(%(%(%(%(%(%(%(%(%))))))))))))))))))))))))))))))))))")
        print("")

    def ProcessDivider_three(self):
        print("\033[5;34;41m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("\033[5;34;41m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    def ProcessDivider_four(self,module):
        loginName=self.explanatoryNote["登录名"] ; roleName=self.explanatoryNote["用户权限"]
        begin_date = self.explanatoryNote["开始日期"] ;finish_date = self.explanatoryNote["结束日期"]
        expect_value = self.explanatoryNote["预期值"];actual__value = self.explanatoryNote["实际值"]
        result = self.explanatoryNote["测试结果"];testReport = self.explanatoryNote["测试报告"]
        list_office = self.explanatoryNote["单位筛选条件"];testPoint =self.explanatoryNote["测试点"]
        str_office = EachQuantityType_transition_CharacterString(list_office).DataTypeConversion_console()
        print("\033[37;40m<$$$$$$%r模块，%r$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>" %(module,testPoint))
        print("\033[1;34;40m测试用户登录名：%r；用户权限：%r；开始日期：%r；结束日期：%r；单位筛选条件：%r" % (loginName, roleName,begin_date,finish_date,str_office))
        print("\033[1;34;40m列表数量比对预期值：", expect_value)
        print("\033[1;34;40m列表数量比对实际值：", actual__value)
        print("\033[1;34;40m测试结果：",result)
        print("\033[1;34;40m测试报告：", testReport)
        print("")


    def ProcessDivider_five(self,type1):
        testPoint = self.explanatoryNote["测试点"];expected = self.explanatoryNote["预期值"]
        actual = self.explanatoryNote["实际值"];result = self.explanatoryNote["测试结果"]
        testReport = self.explanatoryNote["测试报告"]
        print("\033[37;40m<$$$$$$%r$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>"%type1)
        print("\033[1;34;40m外部和内部用户，%r"%testPoint)
        print("\033[1;34;40m预期值：", expected)
        print("\033[1;34;40m实际值：", actual)
        print("\033[1;34;40m测试结果：", result)
        print("\033[1;34;40m测试报告：", testReport)
        print("")


    def ProcessDivider_six(self,type1):
        expected = self.explanatoryNote["预期值"];actual = self.explanatoryNote["实际值"];result = self.explanatoryNote["测试结果"]
        testReport = self.explanatoryNote["测试报告"]
        print("\033[37;40m<$$$$$$%r$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>" % type1)
        print("\033[1;34;40m预期值：", expected)
        print("\033[1;34;40m实际值：", actual)
        print("\033[1;34;40m测试结果：", result)
        print("\033[1;34;40m测试报告：", testReport)
        print("")

    def ProcessDivider_seven(self,procedure,operationUser,initial_argument_set):
        print("\033[5;34;41m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("\033[5;34;41m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("\033[1;34;40m需要执行的工单流程用例：\033[0m\033[4;35;40m%r" % self.explanatoryNote)
        print("\033[1;34;40m正在操作的步骤：\033[0m\033[4;35;40m%r步骤" % procedure)
        print("\033[1;34;40m正在操作步骤的用户信息：\033[0m\033[4;35;40m%r" % operationUser)
        print("\033[1;34;40m上一个步骤返回的参数集：\033[0m\033[4;35;40m%r" % initial_argument_set)


    def ProcessDivider_eight(self,procedure, initial_argument_set,testResult,testReport):
        print("\033[1;34;40m返回“%r”步骤操作后的参数集：\033[0m\033[4;35;40m%r" % (procedure,initial_argument_set))
        print("\033[1;34;40m“%r”步骤操作后的参数结果：%r；测试报告：：\033[0m\033[4;35;40m%r" % (procedure,testResult,testReport))
        print("\033[5;36;43m%%%%%%%%%%%%%%%%%%%%%%%“%r”步骤测试结束%%%%%%%%%%%%%%%%%%%%%%%" % procedure)
        print("")
        print("")

    def ProcessDivider_nine(self, loginName,list_expectvalue,list_actualvalue,testResult, testReport):
        print("\033[1;34;40m%r：\033[0m\033[4;35;40m%r" %(self.explanatoryNote,loginName))
        print("\033[1;34;40m预期值：\033[0m\033[4;35;40m%r" % list_expectvalue)
        print("\033[1;34;40m实际值：\033[0m\033[4;35;40m%r" %list_actualvalue)
        print("\033[1;34;40m测试结果：\033[0m\033[4;35;40m%r" % testResult)
        print("\033[1;34;40m测试报告：\033[0m\033[4;35;40m%r" % testReport)
        print("")
        print("")

    def ProcessDivider_ten(self,list_screening ):
        print("\033[5;34;41m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("\033[5;34;41m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("\033[5;34;41m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("\033[5;34;41m&&&&&&&&&&&&&&&&&%r&&&&&&&&&&&&&&&&&&&&&" %self.explanatoryNote)
        print("\033[1;34;40m测试点：\033[0m\033[4;35;40m%r"%list_screening)


    def ProcessDivider_eleven(self,screening):
        print("")
        print("\033[5;34;43m（（（（（（（（（（（（（（（（）））））））））））））））））")
        print("\033[1;34;40m@@@@@@@@@@@@@@@@@@@@@测试用例：%r@@@@@@@@@@@@@@@@@@@@@@@@@@@"%screening)
        print("\033[5;34;43m（（（（（（（（（（（（（（（（）））））））））））））））））")
        print("")
