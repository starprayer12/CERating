from django.http import HttpResponse
import uuid
import time
from emailcheck.models import emailcheck
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def hello(request):
    return HttpResponse("Hello World!")

@csrf_exempt
def email_verification_code(request):
    if request.method == 'POST':
        print("email1")
        email = request.POST['email']  # 邮箱
        code = str(uuid.uuid1().int)[:6]  # 验证码
        timestamp = time.time() + 180  # 过期时间戳
        mail_host = "smtp.163.com"
        mail_user = "CERating@163.com"
        mail_pass = "SXMAUZBOKGBXDDVQ"
        sender = "CERating@163.com"
        receivers = [email]

        print("email2")
        message = MIMEText(code, 'plain', 'utf-8')
        print("email3")
        message['From'] = mail_user
        message['To'] = email
        subject = 'Verification Code'
        message['Subject'] = Header(subject, 'utf-8')
        smtpObj = smtplib.SMTP()
        print("email4")
        smtpObj.connect(mail_host, 25)
        print("email5")
        smtpObj.set_debuglevel(1)
        print("email6")
        smtpObj.login(mail_user, mail_pass)
        print("email7")
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("email8")
        check_record = emailcheck.objects.filter(email=email)
        if check_record.exists():  # 如果表内有该邮箱的记录
            print("email9")
            check_detail = emailcheck.objects.get(email=email)
            check_detail.code = code
            check_detail.timestamp = timestamp
            check_detail.save()
            print("email10")
        else:  # 如果没有该邮箱的记录
            print("email11")
            new_record = emailcheck(email=email, code=code, timestamp=timestamp)
            new_record.save()
            print("email12")
        return {}
