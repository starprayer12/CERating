from web.models import Enterprise
from django.http import JsonResponse

def login(request):
    try:
        user = Enterprise.objects.get(email=request.POST['email'])
        import hashlib
        md5 = hashlib.md5()
        s = request.POST['password']
        md5.update(s.encode('utf-8'))
        if user.password == md5.hexdigest():
            print('登录成功')
            data = {'code': 0, 'name': user.name}
            return JsonResponse(data)
        else:
            print("密码错误")
            data = {'code': 2, 'name': ''}
            return JsonResponse(data)
            
    except Exception as err:
        print('邮箱不存在')
        data = {'code': 1, 'name': ''}
        return JsonResponse(data)