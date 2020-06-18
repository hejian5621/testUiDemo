# 读取服务器的方法
import paramiko




class passShh_connectToServer:
    """通过shh连接服务器"""

    def __init__(self,command):
        self.command=command


    def  gettingData(self):
        """
        获取数据
        :return:
        """
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname='47.106.245.240', port=22, username='root', password='tdx@qwe321')
        # 输入命令    #stdin为输入的命令#  stdout为命令返回的结果 # stderr为命令错误时返回的结果
        stdin, stdout, stderr = ssh.exec_command(self.command)
        res, err = stdout.read(), stderr.read()
        result = res if res else err
        ssh.close()  # 关闭连接
        return result


    def Get_server_time(self):
        """
        获取服务器时间
        %Y-%m-%d %H:%M:%S
        :return:
        """
        dateOrTime=None
        command='date +%r'%self.command
        systemTime1 = passShh_connectToServer(command).gettingData()
        # 转化时间格式为“utf-8”编码
        systemTime=str(systemTime1,'utf-8')
        return systemTime


