# -*- coding: utf-8 -*-
# 连接测试服务器方法
import time,select,paramiko

now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
now_day = time.strftime('%Y-%m-%d', time.localtime(time.time()))



serverip ='47.106.245.240'
user='root'
pwd ='tdx@qwe123'


# 进行连接
print('------------开始连接服务器(%s)-----------' % serverip)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('------------开始认证......-----------')
client.connect(serverip, 22, username=user, password=pwd, timeout=4)
print('------------认证成功!.....-----------')
# 开启channel 管道
transport = client.get_transport()
channel = transport.open_session()
channel.get_pty()
# 执行命令nohup.log.2017-12-30
tail = 'tail -f ../work/tomcat/tomcat-8081-eosp/logs/catalina.out'
#将命令传入管道中
channel.exec_command(tail)
while True:
    #判断退出的准备状态
    if channel.exit_status_ready():
        break
    try:
        # 通过socket进行读取日志，个人理解，linux相当于客户端，我本地相当于服务端请求获取数据（此处若有理解错误，望请指出。。谢谢）
        rl, wl, el = select.select([channel], [], [])
        if len(rl) > 0:
            recv = channel.recv(1024)
            # 此处将获取的数据解码成gbk的存入本地日志
            print(recv.decode('utf-8', 'ignore'))

    #键盘终端异常
    except KeyboardInterrupt:
        print("Caught control-C")
        channel.send("\x03")  # 发送 ctrl+c
        channel.close()
client.close()




