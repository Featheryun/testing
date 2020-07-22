import smtplib
from email.mime.text import MIMEText
from email.header import Header
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time

def send_email(sender, recivers):
    mail_msg = '''<p>Python 邮件发送测试 test_mail</p><p><a href="http:www.baidu.com">百度</a></p>'''
    msg = MIMEText('文本内容---->测试' + mail_msg, 'plain', 'utf-8')
    msg['From'] = Header('test', 'utf-8')
    msg['To'] = Header('测试', 'utf-8')
    subject = 'Python STMP 邮件测试'
    msg['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, recivers, msg.as_string())
        print('发送成功')
    except smtplib.SMTPException:
        print('error:无法发送邮件')


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
    # send_email('1172445317@qq.com', '')
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'date', run_date='2020-07-21 15:08:30')
    scheduler.start()
    scheduler.shutdown(wait=False)
