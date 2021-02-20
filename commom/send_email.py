import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time

def send_email(file):
    sender = '1172445317@qq.com'
    password = 'jgmjsebyereajdbg'
    # 接受邮箱
    receiver = '1172445317@qq.com'

    smtpserver = 'smtp.qq.com'

    subject = file
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    # text/plain的意思是将文件设置为纯文本的形式，浏览器在获取到这种文件时并不会对其进行处理。
    # msg = MIMEText('下雨了，大家关好窗户', 'plain', 'utf-8')
    msg = MIMEMultipart()
    msg.attach(MIMEText(open(file, 'rb').read(), 'html', 'utf-8'))
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['to'] = receiver
    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(file, 'rb').read(), 'html', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment;filename="test.html"'
    msg.attach(att1)
    # print(msg)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error:无法发邮件")


def job():
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# scheduler = BlockingScheduler()
# 在周一到周五6:30执行job()
# scheduler.add_job(job, 'cron', day_of_week='1-5', hour=6, minute=30)

# 在每年 1-3、7-9 月份中的每个星期一、二中的 00:00, 01:00, 02:00 和 03:00 执行 job() 任务
# scheduler .add_job(job, 'cron', month='1-3,7-9',day='0, tue', hour='0-3')

# BlockingScheduler是APScheduler中的调度器，APScheduler 中有两种常用的调度器，
# BlockingScheduler 和 BackgroundScheduler，当调度器是应用中唯一要运行的任务时，
# 使用 BlockingSchedule，如果希望调度器在后台执行，使用 BackgroundScheduler。

if __name__ == '__main__':
    send_email('/util/用户信息(2021-02-04-17).html')
    # scheduler = BlockingScheduler()
    # scheduler.add_job(job, 'date', run_date='2021-02-05 15:08:30')
    # scheduler.start()
    # scheduler.shutdown(wait=False)
