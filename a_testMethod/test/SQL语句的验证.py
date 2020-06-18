# -*- coding: utf-8 -*-
# 调出SQL语句
from commonality.database_sql import WorkOrder_quantity_statistics

parameterPacket={"所选单位ID":None,"开始日期":"2015-01-01 00:00:00","结束日期":"2020-01-10 23:59:59","用户ID":"7e15c22f331843dd9134b68c38dfb446"}

p="故障类型-用户管理员-事件"

# '''获取SQL语句'''
sql = WorkOrder_quantity_statistics(p).ReportStatistics_quantityStatistics(parameterPacket)

print(sql)





# # ## '''获取查询结果'''
# result,sql = dataProcessing("groupIDuserID_Sort").user_name(groupID,userID)  # user_mane:用户名称，预期结果
#
# print("result:",result)


