from django.http import HttpResponse
import uuid
import time
from .models import emailcheck
from django.core.mail import send_mail

def hello(request):
    return HttpResponse("Hello World!")

def email_verification_code(request):
    if request.method == 'POST':
        email = request.POST['email']  # 邮箱
        code = str(uuid.uuid1().int)[:6]  # 验证码
        timestamp = time.time() + 180  # 过期时间戳
        send_mail("verification code", code, from_email='cerating@163.com', recipient_list=[email])
        check_record = emailcheck.objects.filter(email=email)
        if check_record.exists():  # 如果表内有该邮箱的记录
            check_detail = emailcheck.objects.get(email=email)
            check_detail.code = code
            check_detail.timestamp = timestamp
            check_detail.save()
        else:  # 如果没有该邮箱的记录
            new_record = emailcheck(email=email, code=code, timestamp=timestamp)
            new_record.save()
        return {}
