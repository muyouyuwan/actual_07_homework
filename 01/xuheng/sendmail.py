#coding=utf-8
 
import smtplib
from email.mime.text import MIMEText


class MailModel:
 
    def __init__(self):
        self.mail_host = "smtp.126.com"
        self.mail_user = "lanfeng007"
        self.mail_pass = "xuheng.xxx"
        self.postfix = "126.com"

    def write_file(self,what):
        with open("user.txt", "w") as f:
            for key,value in what.items():
                f.writelines(str(key)+','+str(value)+'\n')
                f.flush()

    def check_key(self,content):
        with open("user.txt", "r") as f:
            listStu = {}
            for line in f.readlines() :
                line1 = line.strip().split(',')
                listStu[line1[0]]=line1[1]
                if content in listStu:
                    listStu[content] = int(listStu[content]) + 1
                    self.write_file(listStu)
                    return listStu[content]
                else:
                    listStu.update({content:1})
                    self.write_file(listStu)
                    return listStu[content]

    def send_mail(self, user_list, sub, content):
        if self.check_key(content) > 2:
            return 0
        else:
            me = "hello"+"<"+self.mail_user+"@"+self.postfix+">"
            msg = MIMEText(content, _subtype = 'html', _charset = 'utf-8')
            msg['Subject'] = sub
            msg['From'] = me
            msg['To'] = ';'.join(user_list)
            try:
                server = smtplib.SMTP()
                server.connect(self.mail_host)
                server.login(self.mail_user, self.mail_pass)
                server.sendmail(me, user_list, msg.as_string())
                server.close()
                return True
            except Exception, e:
                print str(e)
                return False




 
mailuser_list=["369134@qq.com", "xuheng@tyread.com"]

mail = MailModel()
if mail.send_mail(mailuser_list, '日志文件大小告警', "/fiodata/DataFiles/outside/NGLogHour/2015-12-09//nginxxf/2015-12-09_192.168.10.194_13.log.zip"):
    print "ok"
else:
    print "fail"