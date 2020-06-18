

from relative_location import relative_site

locat=relative_site.location()
print(locat)


table_name="测试"

# 拼接地址
fileAddress = locat + "report\\ChangeTheValue\\testReport_template" + "\\" + table_name


print(fileAddress)