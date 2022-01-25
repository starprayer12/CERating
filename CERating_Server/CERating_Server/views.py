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
        verification_code = str(uuid.uuid4())[:6]  # 验证码
        c_time = time.time() + 180  # 过期时间戳
        send_mail("verification_code", verification_code, from_email='cerating@163.com', recipient_list=[email])
        check_record = emailcheck.objects.filter(email=email)
        if check_record.exists():  # 如果表内有该邮箱的记录
            check_detail = emailcheck.objects.get(email=email)
            check_detail.verification_code = verification_code
            check_detail.c_time = c_time
            check_detail.save()
        else:  # 如果没有该邮箱的记录
            new_record = emailcheck(email=email, verification_code=verification_code, c_time=c_time)
            new_record.save()
        return {}
