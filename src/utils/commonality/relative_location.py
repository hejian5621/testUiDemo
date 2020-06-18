# 读取文件位置方法
import os



class relative_site:



    @staticmethod
    def location():
        path  = os.path.dirname(os.path.realpath(__file__))
        n=len("src/utils/commonality")
        path=path[:-n]
        return path



# from relative_location import relative_site
# locat = relative_site.location()
# D:\python demo\ProjectTemplate\