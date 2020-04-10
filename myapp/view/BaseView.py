from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.http import HttpResponse,JsonResponse
from myapp.models import Users


class BaseView(object):
    def homepage(request):
        return render(request, "login.html")

    def page_not_found(request, exception):
        return render(request, "error_page/404.html", {"exception": exception})

    def server_error(request):
        return render(request, "error_page/500.html")

    def userhomepage(request):
        return render(request, "user/userhomepage.html")

    def registerpage(request):
        return render(request, "register.html")

    @csrf_exempt
    def register(request):
        if request.method == "POST":
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            if name and pwd:
                filter_result = Users.objects.filter(username=name)
                if len(filter_result) == 0:
                    Users.objects.create(username=name, password=pwd)
                    return render(request, "login.html", {"error": "注册成功,请登录。"})
                else:
                    return render(request, "register.html", {"error": "用户名已经存在！！！"})
            else:
                return render(request, "register.html", {"error": "出现未知参数！！！"})
        else:
            return render(request, "register.html", {"error": "这不是POST进来的！！！"})

    @csrf_exempt
    def login(request):
        if request.method == "POST":
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            print(name)
            print(pwd)
            print("9999")
            if name and pwd:
                LoginResult = BaseView.login_varify(name, pwd)  # 0-登录成功 1-用户名错误 2-密码错误 3-被禁用 4-管理员登录
                if LoginResult == "0":  # 普通用户登录成功
                    print("普通用户登录成功")  # TODO  普通用户登录成功
                elif LoginResult == "4":
                    print("管理员登录sccess")  # TODO  理员登录sccess
                else:
                    return render(request, "login.html", {"LoginResult": LoginResult})
            else:
                return render(request, "login.html", {"error": "出现未知参数！！！"})
            template = get_template('login.html')
            html = template.render(locals())
            return HttpResponse(html)
        else:
            return render(request, "login.html", {"error": "这不是POST进来的！！！"})

    def login_varify(username, passwoed):
        # 0-登录成功 1-用户名错误 2-密码错误 3-被禁用 4-管理员登录
        flag = "1"
        filter_result = Users.objects.filter(username=username).values('password', 'power', 'apply')
        if filter_result:
            if filter_result[0]['password'] == passwoed:
                if filter_result[0]['power'] == 0:
                    flag = "4"  # 4-管理员登录
                elif filter_result[0]['apply'] == 0:
                    flag = "3"  # 3-用户被禁用
                else:
                    flag = "0"  # 0-登录成功
            else:
                flag = "2"  # 2-密码错误

        return flag
