from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django08 import models, forms
from django.core.mail import EmailMessage
from django.urls import reverse


# Create your views here.
def index(request, pid=None, del_pass=None):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = '如要张贴信息，则每一个字段都要填...'
    if del_pass and pid:
        try:
            post = models.Post.objects.get(id=pid)
        except:
            post = None
        if post:
            if post.del_pass == del_pass:
                post.delete()
                message = "数据删除成功"
            else:
                message = "密码错误"
    elif user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = '成功保存！请记得你的编辑密码[{}]!，信息需经审查后才会显示。'.format(user_pass)
    test = [0,1,2,3]
    return render(request, 'django08/index.html', locals())


def listing(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()
    return render(request, 'django08/listing.html', locals())

def posting(request):
    moods = models.Mood.objects.all()
    message = '如要张贴信息，则每一个字段都要填...'
    return render(request, 'django08/posting.html', locals())


def contact(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = "感谢您的来信，我们会尽速处理您的宝贵意见。"
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
            mail_body = u'''
            网友姓名：{}
            居住城市：{}
            是否在学：{}
            反应意见：如下
            {}'''.format(user_name, user_city, user_school, user_message)

            email = EmailMessage('来自【不吐不快】网站的网友意见',
                                 mail_body,
                                 user_email,
                                 ['skynet.tw@gmail.com'])
            email.send()
        else:
            message = "请检查您输入的信息是否正确！"
    else:
        form = forms.ContactForm()
    return render(request, 'django08/contact.html', locals())


def post2db(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            message = "您的信息已保存，要等管理员启用后才看得到。"
            post_form.save()
            # return HttpResponseRedirect("http://wwww.baidu.com")
            return HttpResponseRedirect(reverse('django08:django08_list'))
        else:
            message = '如要张贴信息，则每一个字段都要填...'
    else:
        post_form = forms.PostForm()
        message = '如要张贴信息，则每一个字段都要填...'

    return render(request, 'django08/post2db.html', locals())

